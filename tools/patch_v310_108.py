# V310.108 · PLATEFORMES EN ANGLAIS : textes français vus par un joueur qui REVIENT (Jour 2) relevés par tests en jeu (window.__i18nMiss) : guide, série de jours, défi du jour, 1re mission, lieux de la carte
import json, re
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
U = {"ici": "here", "carte": "map", "Vue immersive": "Immersive view", "Clique": "Click", "Raccourci : touche V.": "Shortcut: V key.", "Monter, descendre": "Get in, get out", "Sortir": "Get out", "Raccourci : touche F.": "Shortcut: F key.", "Le": "The", "menu": "menu", "Raccourci : Échap.": "Shortcut: Esc.", "Ton": "Your", "téléphone": "phone",
 "#/# · Admire la ville": "#/# · Enjoy the view", "#/# · Se déplacer": "#/# · Moving around", "#/# · Ton objectif": "#/# · Your goal", "#/# · Carte et GPS": "#/# · Map and GPS", "#/# · Vue immersive": "#/# · Immersive view", "#/# · Monter, descendre": "#/# · Get in, get out", "#/# · Ton perso": "#/# · Your character", "#/# · Ton téléphone": "#/# · Your phone",
 "Barbe à papa": "Cotton candy", "Crêpes": "Crepes", "Motocross · à louer": "Motocross · for rent", "Glaces": "Ice cream", "Limonade": "Lemonade", "Gaufres": "Waffles", "Autos tamponneuses": "Bumper cars", "Tasses folles": "Teacups", "Boutique": "Shop",
 "jour d'affilée": "day in a row", "Défi du jour · Conduite propre": "Daily challenge · Clean driving", "Série :": "Streak:", "# jour": "# day", "d'affilée · Bonus à # jours ($#) et # jours ($#)": "in a row · Bonus at # days ($#) and # days ($#)", "# sur # · # défi réussi au total": "# of # · # challenges completed in total", "· vraie vie": "· real life",
 "Va au": "Go to the", "Dépôt (violet)": "Depot (purple)", "✓ +# $ dans ta poche": "✓ +$# in your pocket", "Ouvrir · +# $": "Open · +$#",
 "Mission # · Livre ton premier kebab.": "Mission # · Deliver your first kebab.", "Mission · livraison du kebab": "Mission · kebab delivery", "Livre le colis au point violet": "Deliver the package to the purple dot",
 "📩 Confirme ton adresse dans l'e-mail": "📩 Confirm your address in the email", "« Confirme ton adresse · Constancy »": "“Confirm your address · Constancy”", "Continuer · jour # · $#": "Continue · day # · $#",
 "Animal endormi · gardes en intervention": "Animal asleep · rangers on site", "Stade de baseball · Constancy Stars": "Baseball stadium · Constancy Stars", "Pic Blanc": "White Peak", "Tour de guet": "Watchtower", "Appartement vue mer": "Sea-view apartment", "Sommet · Mont Constancy": "Summit · Mount Constancy", "Mont Constancy": "Mount Constancy"}
n = sum(1 for k in U if k not in d); d.update(U)
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271800';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "nouvelles traductions,", len(U), "au total")
