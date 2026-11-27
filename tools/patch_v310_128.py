# V310.128 · TEST DES BORDURES DE TOUS LES PONTS (tâche 1 de la file de nuit, R1 R2) : updateDecks rendu accessible au crochet de test window.__W (aucun effet en jeu)
# tests/ponts_bordures.js : chaque tablier, les 2 sens, la voiture braquée vers la bordure gauche puis droite à 10° et 30° (simulation image par image)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep(" AGENCE, notify, resume, DK, DECK_DEFS,", " AGENCE, notify, resume, DK, DECK_DEFS, updateDecks,")
open(p, "w", encoding="utf-8").write(s)
print("OK", n, "remplacements")
