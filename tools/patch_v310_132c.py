# V310.132 (suite 2) · Playgama : le petit bouton « Watch an ad » se posait sur la carte de l'objectif (en haut à droite, depuis V310.99) → il se place juste en dessous
import os
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read()
a = 'document.body.appendChild(b); stat("pub-pg-vue"); } b.style.display = ""; }'
assert s.count(a) == 1, "REFUS"
s = s.replace(a, 'document.body.appendChild(b); stat("pub-pg-vue"); } b.style.display = ""; try { const mg = document.getElementById("mainGoal"), r = mg && mg.offsetParent && mg.getClientRects().length ? mg.getBoundingClientRect() : null; b.style.top = r && r.bottom > 0 && r.right > innerWidth - 240 ? Math.round(r.bottom + 8) + "px" : "calc(118px + env(safe-area-inset-top))"; } catch (e) {} }')
open(p, "w", encoding="utf-8").write(s); print("OK 1 remplacement")
