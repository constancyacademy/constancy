# V310.117 · LANGUES SUR LES PLATEFORMES (commande BUSINESS 27/11 13h55, point 4 : « Espagnol, portugais (Brésil) et allemand, en plus de l'anglais, sur les plateformes, langue choisie selon la langue du navigateur, anglais par défaut »)
# Les textes passent d'abord par en.json (français → anglais, comme avant), puis par es.json, pt.json ou de.json (anglais → langue du joueur) · 1 366 textes traduits à la main (traductions naturelles, pas mot à mot) · un texte absent reste en anglais
# Choix : ?lang=es|pt|de, sinon la langue du navigateur sur une plateforme · constancy.fr reste en français
import re, sys, json
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
LINE = [l for l in s.split('\n') if l.startswith('const I18N = { d: null, cache: new Map(), NUM:')][0]
rep(LINE,
    LINE.replace('{ d: null, cache:', '{ d: null, x: null, cache:').replace('miss: new Set() };', 'miss: new Set(), miss2: new Set() };') + '\n/* V310.117 · espagnol, portugais (Brésil) et allemand sur les plateformes (commande BUSINESS du 27/11 13h55, point 4) : 2e dictionnaire anglais → langue du joueur, choisi par ?lang= ou la langue du navigateur · constancy.fr reste en français */\nconst LANG2 = (() => { try { if (LANG !== "en") return ""; const q = /[?&]lang=(es|pt|de)\\b/.exec(location.search); if (q) return q[1]; if (!PORTAL) return ""; const L = String((navigator.languages && navigator.languages[0]) || navigator.language || "").toLowerCase(); const m = /^(es|pt|de)/.exec(L); return m ? m[1] : ""; } catch (e) { return ""; } })(); window.CST_LANG2 = LANG2;')
rep('  if (I18N.cache.size > 20000) I18N.cache.clear(); I18N.cache.set(t, r); return r; }',
    '  if (I18N.x) { const k2 = r.trim(); if (k2 && /[a-zA-Z]{2}/.test(k2)) { const n2 = k2.match(I18N.NUM) || [], key2 = k2.replace(I18N.NUM, "#"), e2 = I18N.x[key2]; if (e2 != null) { let i = 0; const o2 = e2.replace(/#/g, () => (n2[i++] != null ? n2[i - 1] : "#")); r = r.replace(k2, o2); } else if (I18N.miss2.size < 3000) I18N.miss2.add(key2); } }\n  if (I18N.cache.size > 20000) I18N.cache.clear(); I18N.cache.set(t, r); return r; }')
rep('if (LANG === "en") { try { document.documentElement.lang = "en"; } catch (e) {}', 'if (LANG === "en") { try { document.documentElement.lang = LANG2 || "en"; } catch (e) {}')
rep('fetch("assets/i18n/en.json").then(r => r.json()).then(d => { I18N.d = d;', 'Promise.all([fetch("assets/i18n/en.json").then(r => r.json()), LANG2 ? fetch("assets/i18n/" + LANG2 + ".json").then(r => r.json()).catch(() => null) : null]).then(([d, x]) => { I18N.d = d; I18N.x = x || null;')
rep('  window.__i18nMiss = () => [...I18N.miss]; }', '  window.__i18nMiss = () => [...I18N.miss]; window.__i18nMiss2 = () => [...I18N.miss2]; }')
open(p, "w", encoding="utf-8").write(s)
A = json.load(open("/tmp/i18n/all.json", encoding="utf-8"))
for L in ["es", "pt", "de"]:
    f = "assets/i18n/%s.json" % L
    try: old = json.load(open(f, encoding="utf-8"))
    except Exception: old = {}
    old.update(A[L]); json.dump(old, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(L, len(old), "textes")
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272130';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
