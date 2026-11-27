# V310.113 · « Nouveau cette semaine » : le cyclone rejoint le Rex et la citerne (nouvel identifiant, la bulle revient une fois pour tout le monde)
import re, sys, json
p = "index.html"; s = open(p, encoding="utf-8").read()
a = 'const NEWS = { id: "2026-s48", t: "<b>Nouveau cette semaine</b> · Le Rex s\'échappe du parc : ramène-le avant tout le monde. · L\'incendie de Mamie Josette : attention à la citerne." };'
assert s.count(a) == 1
s = s.replace(a, 'const NEWS = { id: "2026-s48b", t: "<b>Nouveau cette semaine</b> · Un cyclone sur la ville : mets 3 habitants à l\'abri. · Le Rex s\'échappe du parc. · L\'incendie de Mamie Josette et sa citerne." };')
open(p, "w", encoding="utf-8").write(s)
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
d["· Un cyclone sur la ville : mets # habitants à l'abri. · Le Rex s'échappe du parc. · L'incendie de Mamie Josette et sa citerne."] = "· A cyclone hits the city: get # residents to safety. · The Rex escaped from the park. · Grandma Josette's fire and the gas tanker."
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271845';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK")
