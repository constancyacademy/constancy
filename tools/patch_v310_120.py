# V310.120 · ESPAGNOL, PORTUGAIS (BRÉSIL), ALLEMAND : les 368 textes anglais ajoutés en V310.119, traduits à la main (tools/i18n_v310_120_x.json) dans assets/i18n/es.json, pt.json, de.json · aucun code touché
import json, re
X = json.load(open("tools/i18n_v310_120_x.json", encoding="utf-8")); n = {}
for L, d in X.items():
    f = "assets/i18n/%s.json" % L; cur = json.load(open(f, encoding="utf-8")); n[L] = 0
    for k, v in d.items():
        if k not in cur: cur[k] = v; n[L] += 1
    json.dump(cur, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272145';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n)
