# Bouton « ▶ JOUER GRATUIT · constancy.fr » (main qui tape, pulsation) + carte de fin 2 s
# (idées de Thomas du 22/11, claude/constancy-reels-clic-22-11.txt). Suite d'images RGBA 1080 x 1920 à 30 i/s.
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1080, 1920
FG = '/tmp/fnt/ebg700.ttf'; FI = '/tmp/fnt/inter600.ttf'; FE = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
PINK = (255, 63, 164, 255); DARK = (22, 14, 32, 255)
CARD = {'jeu': [('Commente JEU', 'p', 132), ("Je t'envoie le lien", 'w', 86), ('+ 5 000 $ offerts.', 'w', 86)],
        'q': [('Lien en bio', 'p', 132), ('Gratuit', 'w', 86), ('Sans téléchargement.', 'w', 86)]}
CARD['yt'] = CARD['q']
def _emoji(ch, size):
    ef = ImageFont.truetype(FE, 109); e = Image.new('RGBA', (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(e).text((10, 10), ch, font=ef, embedded_color=True); e = e.crop(e.getbbox())
    r = size / max(e.size); return e.resize((int(e.size[0] * r), int(e.size[1] * r)), Image.LANCZOS)
def pill(cy):
    """Pilule de base (sans échelle), renvoie (image RGBA plein cadre, boîte)."""
    f = ImageFont.truetype(FI, 50); im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    t1 = 'JOUER GRATUIT'; t2 = ' · '; t3 = 'constancy.fr'
    w1, w2, w3 = (d.textlength(t, font=f) for t in (t1, t2, t3))
    ico = 64; gap = 22; tw = ico + gap + w1 + w2 + w3; ph = 124; pw = int(tw + 96)
    x0 = (W - pw) // 2; y0 = cy - ph // 2; box = (x0, y0, x0 + pw, y0 + ph)
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(glow).rounded_rectangle(box, radius=ph // 2, outline=(255, 63, 164, 255), width=16)
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(16)))
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 10, x0 + pw, y0 + ph + 10), radius=ph // 2, fill=(0, 0, 0, 110))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(12))); d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, radius=ph // 2, fill=(255, 255, 255, 250), outline=PINK, width=6)
    x = x0 + 48; icy = cy
    d.ellipse((x, icy - ico // 2, x + ico, icy + ico // 2), fill=PINK)
    d.polygon([(x + ico * 0.38, icy - ico * 0.24), (x + ico * 0.38, icy + ico * 0.24), (x + ico * 0.74, icy)], fill=(255, 255, 255, 255))
    x += ico + gap; bb = d.textbbox((0, 0), t1, font=f); ty = cy - (bb[1] + bb[3]) / 2
    d.text((x, ty), t1, font=f, fill=DARK); x += w1
    d.text((x, ty), t2, font=f, fill=(150, 140, 160, 255)); x += w2
    d.text((x, ty), t3, font=f, fill=PINK)
    return im, box
def card(ver, cy):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    L = CARD[ver]; fonts = [ImageFont.truetype(FG, s) for _, _, s in L]
    ws = [d.textlength(t, font=f) for (t, _, _), f in zip(L, fonts)]; hs = [int(s * 1.12) for _, _, s in L]
    pw = int(max(ws) + 120); ph = sum(hs) + 90; x0 = (W - pw) // 2; y0 = cy - ph // 2
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 12, x0 + pw, y0 + ph + 12), radius=44, fill=(0, 0, 0, 150))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(18)))
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(glow).rounded_rectangle((x0, y0, x0 + pw, y0 + ph), radius=44, outline=PINK, width=14)
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(14))); d = ImageDraw.Draw(im)
    d.rounded_rectangle((x0, y0, x0 + pw, y0 + ph), radius=44, fill=(12, 9, 20, 238), outline=PINK, width=6)
    y = y0 + 40
    for (t, c, s), f, w_, h_ in zip(L, fonts, ws, hs):
        d.text(((W - w_) / 2, y), t, font=f, fill=PINK if c == 'p' else (255, 255, 255, 255)); y += h_
    return im
def ease(x): x = max(0., min(1., x)); return x * x * (3 - 2 * x)
def make(out, total, ver, cy=None, card_len=2.0, card_cy=None, period=1.2, card_tail=0.0):
    os.makedirs(out, exist_ok=True); cy = cy or int(H * 0.735); card_cy = card_cy or int(H * 0.50)
    base, (bx0, by0, bx1, by1) = pill(cy); hand = _emoji('\U0001F446', 132); cd = card(ver, card_cy)
    n = round(total * 60)
    tipx = bx0 + (bx1 - bx0) * 0.74; tipy = by1 - 18
    for i in range(n):
        t = i / 60.; ph = (t % period) / period
        # main : arrive (0-0,30), appuie (0,30-0,42), repart (0,42-0,75), absente ensuite
        if ph < 0.30: k = ease(ph / 0.30); off = 70 * (1 - k); a = k
        elif ph < 0.42: off = 0; a = 1
        elif ph < 0.75: k = ease((ph - 0.42) / 0.33); off = 70 * k; a = 1 - k
        else: off = 70; a = 0
        press = math.exp(-((ph - 0.36) / 0.06) ** 2)
        sc = 1.0 + 0.022 * math.sin(2 * math.pi * t / period * 2) * 0.5 + 0.018 - 0.05 * press
        fr = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        bw = int(W * sc); bh = int(H * sc); b2 = base.resize((bw, bh), Image.BILINEAR)
        ox = int(540 - 540 * sc); oy = int(cy - cy * sc); fr.alpha_composite(b2, (ox, oy)) if ox >= 0 and oy >= 0 else fr.alpha_composite(b2.crop((-ox if ox < 0 else 0, -oy if oy < 0 else 0, (-ox if ox < 0 else 0) + W, (-oy if oy < 0 else 0) + H)), (max(ox, 0), max(oy, 0)))
        if 0.36 <= ph < 0.85:
            k = (ph - 0.36) / 0.49; r = 18 + 70 * k; al = int(200 * (1 - k))
            rp = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(rp).ellipse((tipx - r, tipy - r * 0.7, tipx + r, tipy + r * 0.7), outline=(255, 63, 164, al), width=6)
            fr = Image.alpha_composite(fr, rp)
        if a > 0.01:
            hd = hand.copy(); hd.putalpha(hd.getchannel('A').point(lambda v: int(v * a)))
            fr.alpha_composite(hd, (int(tipx - hd.size[0] * 0.42), int(tipy + off - 6)))
        tc = total - card_len - card_tail
        if t >= tc - 1e-6 and t < total - card_tail - 1e-6:
            k = ease((t - tc) / 0.18); c2 = cd if k >= 1 else cd.copy()
            if k < 1: c2.putalpha(c2.getchannel('A').point(lambda v: int(v * k)))
            fr = Image.alpha_composite(fr, c2)
        fr.save(f'{out}/f{i:04d}.png', compress_level=1)
    return n
if __name__ == '__main__':
    import sys
    make(sys.argv[1], float(sys.argv[2]), sys.argv[3])
