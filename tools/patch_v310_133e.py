# V310.133 (suite 4) · DATA (point 3 de la BUSINESS, 28/11) : chaque ligne anonyme des plateformes envoie aussi le total gagné (&tg=) et le nombre de livraisons (&lv=) · le cash (&cash=) part déjà depuis la V310.73 : si la colonne « Cash ($) » reste à 0, c'est le script (action=pl) qui ne l'écrit pas
import os
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read()
a = '+ "&cash=" + Math.round((P && P.cash) || 0)'
assert s.count(a) == 1, "REFUS"
s = s.replace(a, a + ' + "&tg=" + Math.round((P && P.earned) || 0) + "&lv=" + ((P && P.deliveries) || 0) /* V310.133 */')
open(p, "w", encoding="utf-8").write(s); print("OK 1 remplacement")
