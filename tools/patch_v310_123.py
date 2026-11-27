# V310.123 · CARTE 3D SUR TÉLÉPHONE : plus de mer partout en dézoomant à la première ouverture
# Trouvé (tests/carte3d.js, iPhone simulé) : à 1 500 m et 4 000 m, la carte ne montrait QUE la mer, sans aucune terre
# Cause : les photos satellite de la carte ne commencent à se charger qu'à l'ouverture de la carte ; la vue dézoomée est construite tout de suite, avant la fin du chargement, et retombe sur un fond bleu uni ;
# une fois les photos arrivées, la reconstruction n'avait jamais lieu tant qu'on restait dézoomé (et 60 s d'attente sur téléphone) · maintenant : la photo est redessinée dans la même texture dès qu'elle est là
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep("Object.values(SATIMG).every(v => typeof v !== \"object\" || (v.complete && v.naturalWidth))) { M3.ovNk = -9; M3.ovMiss = false; }",
    "Object.values(SATIMG).every(v => typeof v !== \"object\" || (v.complete && v.naturalWidth))) { M3.ovMiss = false; /* V310.123 : photos arrivées après la première vue (que de la mer) : la photo de la carte est redessinée tout de suite dans la même texture, même dézoomé et même sur téléphone (avant : bloqué tant qu'on restait dézoomé) */ try { SATIMG.miss = 0; const c = satShot(-2200, -3600, 5200, TOUCH_DEV() ? 1536 : 2048); if (!SATIMG.miss && M3.ovTex) { satEdgeFade(c); M3.ovTex.image = c; M3.ovTex.needsUpdate = true; M3.ovNk = nightK; } else M3.ovNk = -9; } catch (e) { M3.ovNk = -9; } }")
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272330';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
