# V310.119 · PLATEFORMES EN ANGLAIS, BALAYAGE COMPLET (file de nuit : « balayage des derniers textes français restants sur les plateformes »)
# Relevé statique du code (acorn : chaînes et gabarits, nombres → #, coupé aux balises) contre assets/i18n/en.json : 369 textes du jeu encore en français
# (marchands de la fête foraine, Concession, Agence, téléphone, défis, voisin, supérette, gadgets, crédits, panneaux de l'aéroport…) · ajoutés tels quels (tools/i18n_v310_119_en.json)
# Écrans propres à constancy.fr (mail, mot de passe, installation, mode créateur, paiement) laissés de côté · aucun code touché
import json, re
f = "assets/i18n/en.json"; en = json.load(open(f, encoding="utf-8")); add = json.load(open("tools/i18n_v310_119_en.json", encoding="utf-8")); n = 0
for k, v in add.items():
    if k not in en: en[k] = v; n += 1
json.dump(en, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272130';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "textes ajoutés ·", len(en), "au total")
