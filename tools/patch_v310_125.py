# V310.125 · ORDINATEUR, MOINS D'APPELS DE DESSIN (suite de Thomas 17h03, 30 i/s une fois sur deux)
# Mesuré (V310.124, compteur ?fps=1 et relevé par type d'objet, centre-ville, vue 16/9) : 1 450 appels de dessin par image sur ordinateur contre 970 sur téléphone,
# dont 505 morceaux de ville fusionnés (un par matière et par carré de 200 m)
# Sur ordinateur (souris), les carrés de fusion passent à 400 m : même ville, mêmes matières, 4 fois moins de morceaux par matière · téléphone inchangé (200 m, tri plus fin pour sa mémoire)
# Mesuré au même endroit : centre 1 447 → 1 205 appels, tour 1 255 → 1 101, sud 1 147 → 1 008 (triangles +8 %, sans effet visible)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('const ck = mat.uuid + "|" + Math.floor((x + 3000) / 200) + "," + Math.floor((z + 3000) / 200);',
    'const CS = TOUCH_DEV() ? 200 : 400, ck = mat.uuid + "|" + Math.floor((x + 3000) / CS) + "," + Math.floor((z + 3000) / CS); /* V310.125 : sur ordinateur, carrés de 400 m (1 450 → 1 200 appels de dessin au centre-ville) */')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272250';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
