"""Nappe sensuelle originale (R&B lent / ambient) pour les réels avec la voix.
Usage : python3 synth.py <prog A|B|C|D> <durée s> <sortie.wav> [beat 0/1]
(copie de claude/constancy-outil-mix-voix-v2.txt, 24/11)"""
import sys, numpy as np, wave

SR = 48000
PROGS = {
    # (racine basse, notes de l'accord) en MIDI · 4 accords
    'A': [(45, [60, 64, 67, 71]), (41, [57, 60, 64, 67]), (38, [57, 60, 62, 65]), (40, [59, 62, 64, 67])],  # Am9 Fmaj9 Dm9 Em7
    'B': [(36, [64, 67, 71, 74]), (45, [60, 64, 67, 71]), (41, [60, 64, 65, 69]), (43, [62, 64, 67, 69])],  # Cmaj9 Am9 Fmaj7 G6
    'C': [(38, [60, 64, 65, 69]), (46, [62, 65, 69, 70]), (43, [58, 62, 65, 69]), (45, [62, 64, 67, 69])],  # Dm9 Bbmaj7 Gm9 A7sus
    'D': [(42, [61, 64, 68, 69]), (38, [62, 66, 69, 73]), (47, [61, 62, 66, 69]), (49, [59, 64, 68, 71])],  # F#m9 Dmaj7 Bm9 C#m7
}
mf = lambda m: 440.0 * 2 ** ((m - 69) / 12)


def saw(f, t, fc=900.0, hmax=3200.0):
    out = np.zeros_like(t)
    k = 1
    while k * f < hmax:
        out += np.sin(2 * np.pi * k * f * t + k * 0.7) / k / (1 + (k * f / fc) ** 2)
        k += 1
    return out


def env(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    e[:na] = np.sin(np.linspace(0, np.pi / 2, na)) ** 2
    e[-nr:] *= np.cos(np.linspace(0, np.pi / 2, nr)) ** 2
    return e


def main():
    prog, dur, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    beat = len(sys.argv) > 4 and sys.argv[4] == '1'
    rng = np.random.default_rng(7)
    N = int((dur + 2.5) * SR)
    L = np.zeros(N); R = np.zeros(N)
    chords = PROGS[prog]
    seg = dur / 4
    for i, (root, notes) in enumerate(chords):
        s0 = int(max(0, i * seg - 0.35) * SR)
        ln = int((seg + 0.9) * SR)
        t = np.arange(ln) / SR
        e = env(ln, 0.55 if i else 0.05, 0.9)
        lfo = 1 + 0.08 * np.sin(2 * np.pi * 0.23 * t)
        for j, m in enumerate(notes):
            for d, pan in ((-9, 0.15), (-3, 0.4), (3, 0.6), (9, 0.85)):
                v = saw(mf(m) * 2 ** (d / 1200), t) * e * lfo * 0.05
                L[s0:s0 + ln] += v * (1 - pan); R[s0:s0 + ln] += v * pan
        # sous-basse
        sb = np.sin(2 * np.pi * mf(root - 12 if root > 40 else root) * t) * env(ln, 0.25, 0.9) * 0.22
        L[s0:s0 + ln] += sb; R[s0:s0 + ln] += sb
        # piano électrique doux, deux notes égrenées
        for k, m in enumerate((notes[1], notes[3] + 12)):
            st = s0 + int((0.35 + k * seg / 2) * SR); kl = int(1.8 * SR); tk = np.arange(kl) / SR
            f = mf(m)
            ep = (np.sin(2 * np.pi * f * tk) + 0.25 * np.sin(2 * np.pi * 2 * f * tk) * np.exp(-tk * 6)) * np.exp(-tk * 2.2)
            ep *= np.minimum(1, tk / 0.004) * 0.09
            if st + kl <= N:
                L[st:st + kl] += ep * 0.7; R[st:st + kl] += ep * 1.0
    if beat:
        bpm = 68.0; b = 60 / bpm
        tt = np.arange(int(0.5 * SR)) / SR
        kick = np.sin(2 * np.pi * (45 + 40 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 7) * 0.35
        nz = rng.standard_normal(int(0.18 * SR))
        snap = np.convolve(nz, np.ones(6) / 6, 'same') * np.exp(-np.arange(len(nz)) / SR * 28) * 0.06
        hat = np.diff(rng.standard_normal(int(0.04 * SR)), prepend=0) * np.exp(-np.arange(int(0.04 * SR)) / SR * 120) * 0.025
        bt = 0.0
        while bt < dur + 1:
            for off, s in ((0, kick), (1.0, snap), (1.5, kick * 0.6), (2.0, snap)):
                p = int((bt + off * b) * SR)
                if p + len(s) < N: L[p:p + len(s)] += s; R[p:p + len(s)] += s
            for h in range(8):
                p = int((bt + h * b / 2 + (0.06 if h % 2 else 0)) * SR)
                if p + len(hat) < N: L[p:p + len(hat)] += hat * 0.8; R[p:p + len(hat)] += hat
            bt += 4 * b
    # réverbération (IR synthétique 2,4 s)
    irn = int(2.4 * SR)
    ir = rng.standard_normal(irn) * np.exp(-np.arange(irn) / SR * 2.6)
    ir = np.convolve(ir, np.ones(24) / 24, 'same'); ir /= np.sqrt((ir ** 2).sum())
    def conv(x):
        n = len(x) + irn; nf = 1 << (n - 1).bit_length()
        return np.fft.irfft(np.fft.rfft(x, nf) * np.fft.rfft(ir, nf), nf)[:len(x)]
    L = L + 0.45 * conv(L); R = R + 0.45 * conv(R)
    st = np.stack([L, R], 1)[:int(dur * SR)]
    st = np.tanh(st * 1.2) / 1.2
    st /= np.abs(st).max() / 0.5
    with wave.open(out, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype('<i2').tobytes())


main()
