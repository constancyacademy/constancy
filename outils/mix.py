"""V2 voix : phrase dès 0,12 s, ralentie, fondus en puissance constante, « Constancy dot F R » adouci, nouvelle musique.
Usage : python3 mix.py <voix.mp3> <musique.wav> <durée reel s> <tempo phrase> <sortie.wav> [écart max]
(copie de claude/constancy-outil-mix-voix-v2.txt, 24/11 16h30, avec le point 3b)"""
import sys, subprocess, numpy as np, json, re

SR = 48000
vf, mf, T, tempo, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]


def dec(path, af=None, ch=1):
    cmd = ['ffmpeg', '-v', 'error', '-i', path]
    if af: cmd += ['-af', af]
    cmd += ['-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-']
    a = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).copy()
    return a.reshape(-1, ch) if ch > 1 else a


def lufs(x):
    """Sonie intégrée approchée (filtre K simplifié : passe-haut 100 Hz + plateau aigu)."""
    import tempfile, wave, os
    fn = tempfile.mktemp(suffix='.wav')
    y = x if x.ndim == 2 else np.stack([x, x], 1)
    with wave.open(fn, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype('<i2').tobytes())
    r = subprocess.run(['ffmpeg', '-i', fn, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    os.remove(fn)
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1])


def qsin_in(n): return np.sin(np.linspace(0, np.pi / 2, n))       # puissance constante
def qsin_out(n): return np.cos(np.linspace(0, np.pi / 2, n))


# 1. Voix brute, adoucie (plateau aigu -2,5 dB à 6 kHz, compression douce 2,5:1)
v = dec(vf, 'highshelf=f=6000:g=-2.5,acompressor=threshold=-24dB:ratio=2.5:attack=15:release=220:makeup=1')
fr = int(0.05 * SR)
lv = np.array([20 * np.log10(np.sqrt((v[i:i + fr] ** 2).mean()) + 1e-9) for i in range(0, len(v) - fr, fr)])
start = np.argmax(lv > -45) * fr
# attaque du « Constancy » chuchoté : premier bloc fort (0,5 s au-dessus de -26 dB) après la phrase
wst = None
for i in range(int((start + 0.5 * SR) / fr), len(lv) - 10):
    if lv[i:i + 10].mean() > -26 and lv[i - 1] < -35:
        wst = i * fr; break
sil = 0
if wst:
    j = wst // fr - 1
    while j > 0 and lv[j] < -45: sil += 1; j -= 1
assert wst, 'attaque du chuchoté introuvable'
gap_start = wst - sil * fr
P = v[start:gap_start]
W = v[wst - int(0.03 * SR):]
# 2. Phrase ralentie (naturel, hauteur gardée)
import tempfile, wave, os
fn = tempfile.mktemp(suffix='.wav')
with wave.open(fn, 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(P, -1, 1) * 32767).astype('<i2').tobytes())
P = dec(fn, f'atempo={tempo}'); os.remove(fn)
# 3. Niveaux : phrase -21 LUFS, chuchoté -22,5 LUFS (plus de saut brutal)
# 2b. Légère réverbération sur la phrase (24/11 16h22 : jamais de fin coupée net, plus discrète que sur « Constancy »)
_rng = np.random.default_rng(3); _n = int(1.1 * SR)
_ir = _rng.standard_normal(_n) * np.exp(-np.arange(_n) / SR * 4.2)
_ir = np.convolve(_ir, np.ones(16) / 16, 'same'); _ir = np.concatenate([np.zeros(int(0.018 * SR)), _ir]); _ir /= np.sqrt((_ir ** 2).sum())
_dry = len(P); _tail = int(0.85 * SR)
_x = np.concatenate([P, np.zeros(_tail)])
_nf = 1 << (len(_x) + len(_ir)).bit_length()
_wet = np.fft.irfft(np.fft.rfft(_x, _nf) * np.fft.rfft(_ir, _nf), _nf)[:len(_x)]
_wet *= np.sqrt((P ** 2).mean()) / (np.sqrt((_wet[:_dry] ** 2).mean()) + 1e-12)
P = _x + 0.28 * _wet
P_dry_len = _dry
P *= 10 ** ((-21 - lufs(P)) / 20)
W *= 10 ** ((-22.5 - lufs(W[:int(3.5 * SR)])) / 20)
# 4. Fondus puissance constante
P[:int(0.18 * SR)] *= qsin_in(int(0.18 * SR))
P[-int(0.6 * SR):] *= qsin_out(int(0.6 * SR))   # sortie en puissance constante sur la queue de réverbération
W[:int(0.30 * SR)] *= qsin_in(int(0.30 * SR))
gap = min(sil * fr / SR, float(sys.argv[6]) if len(sys.argv) > 6 else 0.55)
t0 = 0.12
N = int(T * SR)
voice = np.zeros(N)
p0 = int(t0 * SR); voice[p0:p0 + len(P)] += P[:max(0, N - p0)]
w0 = p0 + P_dry_len + int(gap * SR)   # le chuchoté part après la phrase sèche, la queue se fond dessous
seg = W[:max(0, N - w0)]; voice[w0:w0 + len(seg)] += seg
fo = int(0.9 * SR); voice[-fo:] *= qsin_out(fo)
# fin du cœur (dernier bloc fort du chuchoté)
wl = np.array([20 * np.log10(np.sqrt((W[i:i + fr] ** 2).mean()) + 1e-9) for i in range(0, len(W) - fr, fr)])
core_end = (w0 + (np.where(wl > wl.max() - 18)[0].max() + 1) * fr) / SR
# 5. Musique : -27 LUFS, baissée encore de 3 dB sous la voix, enveloppe lissée 0,35 s
m = dec(mf, ch=2)[:N]
if len(m) < N: m = np.vstack([m, np.zeros((N - len(m), 2))])
m *= 10 ** ((-27 - lufs(m)) / 20)
act = (np.abs(voice) > 10 ** (-40 / 20)).astype(float)
k = int(0.35 * SR); act = np.convolve(act, np.ones(k) / k, 'same')
duck = 1 - 0.29 * np.clip(act * 3, 0, 1)
m *= duck[:, None]
m[:int(0.25 * SR)] *= qsin_in(int(0.25 * SR))[:, None]
m[-fo:] *= qsin_out(fo)[:, None]
mix = m + np.stack([voice, voice], 1)
# 6. Sonie finale -18 LUFS, crêtes sous -2 dB
mix *= 10 ** ((-18 - lufs(mix)) / 20)
pk = np.abs(mix).max()
if pk > 0.79:
    mix = np.tanh(mix / 0.79) * 0.79
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix, -1, 1) * 32767).astype('<i2').tobytes())
print(json.dumps({'phrase_debut': t0, 'phrase_fin': round(t0 + P_dry_len / SR, 2), 'chuchote_debut': round(w0 / SR, 2),
                  'coeur_fin': round(core_end, 2), 'duree': T, 'marge_fin': round(T - core_end, 2), 'crete': round(20 * np.log10(np.abs(mix).max()), 1)}))
