# V310.114 · 60 I/S SUR ORDINATEUR, SUITE (Thomas 27/11 17h03) : le filtre de couleur CSS posé sur toute l'image 3D (saturation, contraste) oblige le navigateur à recopier tout l'écran à chaque image · sur un écran Retina, c'est 4 fois plus de pixels qu'un écran normal
# Sur ordinateur, quand la fluidité tombe sous 52 i/s, ce filtre est désormais le PREMIER retiré (avant le halo et la définition) · s'il revient et fait retomber la fluidité dans les 15 s, il reste retiré pour la partie
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('if (PF.up && now - PF.up.t < 15000) { const u = PF.up; PF.up = null; if (u.fx) {',
    'if (PF.up && now - PF.up.t < 15000) { const u = PF.up; PF.up = null; if (u.grade) { cv.classList.add("nograde"); PF.gradeLock = 1; } else if (u.fx) {')
rep('        else if (FXR.on && PF.pr <= 1.5 + 0.01) { FXR.on = false; FXR.auto = true; }',
    '        else if ((PF.fine == null ? (PF.fine = !!(window.matchMedia && matchMedia("(pointer:fine)").matches)) : PF.fine) && !cv.classList.contains("nograde")) cv.classList.add("nograde"); /* V310.114 : sur ordinateur, le filtre CSS plein écran part en premier */\n        else if (FXR.on && PF.pr <= 1.5 + 0.01) { FXR.on = false; FXR.auto = true; }')
rep('if (cv.classList.contains("nograde")) cv.classList.remove("nograde"); else if (PF.pr < Math.min(1.0, PF.cap || 9) - 0.01)',
    'if (cv.classList.contains("nograde") && !PF.gradeLock) { cv.classList.remove("nograde"); PF.up = { t: now, grade: 1 }; } else if (PF.pr < Math.min(1.0, PF.cap || 9) - 0.01)')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271900';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
