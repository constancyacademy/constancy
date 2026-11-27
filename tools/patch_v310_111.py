# V310.111 · INVITATION À NOTER LE JEU (commande BUSINESS 27/11 13h55, point 3 : « UNE seule fois, juste après l'achat de la coupé néon, pas pendant une mission ») · plateformes seulement (constancy.fr n'a pas de note)
# Une ligne sur la carte du rendez-vous qui suit la coupé néon (montrée une seule fois par partie) · stat note-invite-<porte>
import re, sys, json
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('${canInst ? \'<button class="rdvb alt" id="rdvInst" type="button">Ajouter à l\\\'écran d\\\'accueil</button>\' : ""}<button class="rdvx" id="rdvX" type="button" aria-label="Fermer">×</button>`;',
    '${canInst ? \'<button class="rdvb alt" id="rdvInst" type="button">Ajouter à l\\\'écran d\\\'accueil</button>\' : ""}${PORTAL && PORTALS[PORTAL] && !P.rateAsk ? `<div class="cw" style="margin-top:8px">⭐ Tu aimes Constancy ? Une note sous le jeu sur <b>${PORTALS[PORTAL].n}</b> nous aide énormément.</div>` : ""}<button class="rdvx" id="rdvX" type="button" aria-label="Fermer">×</button>`; if (PORTAL && PORTALS[PORTAL] && !P.rateAsk) { P.rateAsk = 1; stat("note-invite-" + PORTALS[PORTAL].s); } /* V310.111 (commande BUSINESS 27/11 13h55) : une seule invitation à noter, juste après la coupé néon, sur les plateformes */')
open(p, "w", encoding="utf-8").write(s)
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
d.update({"⭐ Tu aimes Constancy ? Une note sous le jeu sur": "⭐ Enjoying Constancy? A rating below the game on", "nous aide énormément.": "helps us a lot."})
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271930';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
