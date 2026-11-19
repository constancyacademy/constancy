import numpy as np, json, subprocess, os
SR = 44100
rng = np.random.default_rng(7)
def env(n, a=0.002, d=0.2, s=0.0, curve=6):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-curve * np.maximum(0, t - a) / max(d, 1e-4))
    return np.maximum(e, s * (t < d * 3))
def note(m): return 440 * 2 ** ((m - 69) / 12)
def kick(dur=0.45, f0=150, f1=42, drive=2.5):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 28); ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t * 7); x += 0.6 * np.exp(-t * 300) * rng.standard_normal(n) * 0.3
    return np.tanh(drive * x)
def b808(m, dur=0.8, glide_from=None):
    n = int(dur * SR); t = np.arange(n) / SR
    f = np.full(n, note(m))
    if glide_from is not None: f = note(m) + (note(glide_from) - note(m)) * np.exp(-t * 18)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t * 2.2) * np.minimum(1, t / 0.004)
    return np.tanh(3 * x) * 0.9
def snare(dur=0.25, tone=190):
    n = int(dur * SR); t = np.arange(n) / SR
    noise = rng.standard_normal(n) * np.exp(-t * 22)
    body = np.sin(2 * np.pi * tone * t) * np.exp(-t * 30)
    return np.tanh(1.8 * (0.7 * noise + 0.6 * body))
def clap(dur=0.3):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for off in (0, 0.011, 0.022):
        k = int(off * SR); m = n - k; tt = np.arange(m) / SR
        x[k:] += rng.standard_normal(m) * np.exp(-tt * 40)
    x += rng.standard_normal(n) * np.exp(-t * 12) * 0.35
    return np.tanh(1.5 * x) * 0.8
def hat(dur=0.05, open_=False):
    d = 0.25 if open_ else dur; n = int(d * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n); x = np.diff(np.concatenate([[0], x]))
    return x * np.exp(-t * (9 if open_ else 70)) * 0.35
def cowbell(m, dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sign(np.sin(2 * np.pi * note(m) * t)) + 0.7 * np.sign(np.sin(2 * np.pi * note(m) * 1.48 * t))
    return x * np.exp(-t * 9) * 0.22
def saw(f, n, det=(0, -0.11, 0.11)):
    t = np.arange(n) / SR; x = 0
    for d in det: x = x + 2 * ((t * f * 2 ** (d / 12)) % 1) - 1
    return x / len(det)
def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); s = 0.0
    for i in range(len(x)): s = (1 - a) * x[i] + a * s; y[i] = s
    return y
def lp_fast(x, fc):
    # one-pole filter via IIR using scipy for speed
    from scipy.signal import lfilter
    a = np.exp(-2 * np.pi * fc / SR); return lfilter([1 - a], [1, -a], x)
def stab(ms, dur, fc=2400):
    n = int(dur * SR); x = sum(saw(note(m), n) for m in ms) / len(ms)
    x = lp_fast(x, fc) * env(n, 0.003, dur * 0.5, curve=3)
    return np.tanh(2 * x) * 0.5
def riser(dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n); x = lp_fast(x, 800) * 0 + x
    return x * (t / dur) ** 2 * 0.25
def impact(dur=1.6):
    n = int(dur * SR); t = np.arange(n) / SR
    boom = np.sin(2 * np.pi * (35 + 80 * np.exp(-t * 6)) * t) * np.exp(-t * 2.5)
    crash = rng.standard_normal(n) * np.exp(-t * 3.5) * 0.4
    return np.tanh(2.2 * (boom + lp_fast(crash, 6000)))
def place(buf, x, at, g=1.0):
    i = int(at * SR); j = min(len(buf), i + len(x));
    if i < len(buf): buf[i:j] += g * x[: j - i]
def sidechain(buf, beats, depth=0.6, rel=0.18):
    t = np.arange(len(buf)) / SR; g = np.ones(len(buf))
    for b in beats:
        m = t >= b; g[m] = np.minimum(g[m], 1 - depth * np.exp(-(t[m] - b) / rel))
    return buf * g
def master(mix, name, beats, drops, bpm):
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.98
    mix = np.tanh(1.6 * mix) / np.tanh(1.6)
    fade = int(0.02 * SR); mix[-fade:] *= np.linspace(1, 0, fade)
    st = np.stack([mix, mix], 1)
    import wave
    w = (st * 32767 * 0.95).astype(np.int16)
    p = f'/home/claude/mus/{name}.wav'
    with wave.open(p, 'wb') as f: f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(w.tobytes())
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-af', 'loudnorm=I=-9:TP=-1:LRA=7', '-ar', '44100', '-b:a', '256k', f'/home/claude/mus/{name}.mp3'], check=True)
    json.dump({'bpm': bpm, 'beats': [round(b, 3) for b in beats], 'drops': drops}, open(f'/home/claude/mus/{name}.json', 'w'))

DUR = 16.0
def grid(bpm, start=0.0): b = 60 / bpm; return [start + i * b for i in range(int((DUR - start) / b) + 1) if start + i * b < DUR]

# 1 · PHONK DRIFT (145 BPM, cowbell, 808 saturé)
def phonk():
    bpm = 145; b = 60 / bpm; buf = np.zeros(int(DUR * SR)); beats = grid(bpm)
    place(buf, impact(), 0, 0.9)
    cow = [75, 75, 78, 75, 73, 75, 70, 73]
    for i, t in enumerate(beats):
        bar_i = i % 8
        if bar_i in (0, 3, 5): place(buf, kick(f0=170, drive=4), t, 1.0)
        if bar_i in (2, 6): place(buf, clap(), t, 0.8)
        place(buf, hat(), t, 0.5); place(buf, hat(), t + b / 2, 0.35)
        place(buf, cowbell(cow[bar_i]), t, 0.9); place(buf, cowbell(cow[(bar_i + 3) % 8]), t + b / 2, 0.5)
        if bar_i == 0: place(buf, b808(37, b * 3, glide_from=44), t, 0.9)
        if bar_i == 5: place(buf, b808(34, b * 2), t, 0.85)
    for t in beats[30:32]:
        for k in range(4): place(buf, hat(0.03), t + k * b / 4, 0.4)
    return buf, beats, bpm
# 2 · TRAP 808 (140 BPM, roulements de charleston, glides)
def trap():
    bpm = 140; b = 60 / bpm; buf = np.zeros(int(DUR * SR)); beats = grid(bpm)
    place(buf, impact(), 0, 0.9)
    lead = [72, 75, 79, 77, 75, 72, 70, 72]
    for i, t in enumerate(beats):
        k = i % 8
        if k in (0, 3, 6): place(buf, kick(f0=140, f1=38), t, 1.0)
        if k in (2, 6): place(buf, snare(tone=220), t, 0.9); place(buf, clap(), t, 0.5)
        if k in (0, 3): place(buf, b808(36 if k == 0 else 39, b * 2.5, glide_from=48 if i % 16 == 3 else None), t, 1.0)
        roll = 4 if k in (3, 7) else 2
        for r in range(roll): place(buf, hat(0.035), t + r * b / roll, 0.45)
        if i % 2 == 0: place(buf, stab([lead[(i // 2) % 8]], b * 0.9, fc=3500), t, 0.35)
    return buf, beats, bpm
# 3 · ELECTRO HOUSE (128 BPM, 4 temps, accords saw, sidechain)
def house():
    bpm = 128; b = 60 / bpm; buf = np.zeros(int(DUR * SR)); beats = grid(bpm)
    place(buf, impact(), 0, 0.8)
    syn = np.zeros_like(buf); chords = [[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 55, 59]]
    for i, t in enumerate(beats):
        place(buf, kick(f0=160, f1=48, drive=3), t, 1.0)
        if i % 2 == 1: place(buf, clap(), t, 0.85)
        place(buf, hat(open_=True), t + b / 2, 0.45)
        for s in range(4): place(buf, hat(0.03), t + s * b / 4, 0.2)
        ch = chords[(i // 8) % 4]
        place(syn, stab(ch + [ch[0] + 12], b * 0.45, fc=3200), t + b / 2, 0.9)
        place(syn, stab([ch[0] - 12], b * 0.9, fc=900), t, 0.8)
    syn = sidechain(syn, beats, 0.75, 0.12)
    return buf + syn, beats, bpm
# 4 · DRUM & BASS (174 BPM, breakbeat, basse reese)
def dnb():
    bpm = 174; b = 60 / bpm; buf = np.zeros(int(DUR * SR)); beats = grid(bpm)
    place(buf, impact(), 0, 0.85)
    pat = {0: 'k', 2: 's', 5: 'k', 6: 's'}  # en croches
    eighth = b / 2; n8 = int(DUR / eighth)
    for j in range(n8):
        t = j * eighth; k = j % 8
        if pat.get(k) == 'k': place(buf, kick(f0=180, f1=50, drive=3.5), t, 1.0)
        if pat.get(k) == 's': place(buf, snare(tone=200), t, 1.0)
        place(buf, hat(0.03), t, 0.35)
    bass = np.zeros_like(buf); seq = [38, 38, 41, 36]
    for i in range(0, len(beats), 4):
        t = beats[i]; n = int(b * 4 * SR); x = saw(note(seq[(i // 4) % 4]), n, det=(0, -0.25, 0.25))
        x = (0.6 * lp_fast(x, 380) + 0.4 * lp_fast(x, 900) * np.sin(np.arange(n) / SR * 6) ** 2) * 1.8
        place(bass, np.tanh(x), t, 0.7)
    return buf + bass, beats, bpm
# 5 · SYNTHWAVE PUNCH (118 BPM, caisse claire gated, arpège)
def synthwave():
    bpm = 118; b = 60 / bpm; buf = np.zeros(int(DUR * SR)); beats = grid(bpm)
    place(buf, impact(), 0, 0.85)
    arp = [57, 64, 69, 72, 69, 64]; prog = [0, -4, -2, -5]
    for i, t in enumerate(beats):
        place(buf, kick(f0=150, f1=45, drive=2.8), t, 1.0)
        if i % 2 == 1:
            s = snare(0.4, 180); n = len(s); s[int(0.18 * SR):] *= 0.0; place(buf, s, t, 1.0)
        place(buf, hat(0.04), t + b / 2, 0.4)
        tr = prog[(i // 4) % 4]
        for a in range(4): place(buf, stab([arp[(i * 4 + a) % 6] + tr + 12], b / 4 * 0.9, fc=4200), t + a * b / 4, 0.32)
        place(buf, stab([45 + tr - 12, 45 + tr], b * 0.95, fc=700), t, 0.7)
    return buf, beats, bpm
TRACKS = {'mus_01_phonk_drift': phonk, 'mus_02_trap_808': trap, 'mus_03_electro_house': house, 'mus_04_drum_and_bass': dnb, 'mus_05_synthwave_punch': synthwave}
for name, fn in TRACKS.items():
    buf, beats, bpm = fn(); master(buf, name, beats, [0.0], bpm); print('ok', name)
