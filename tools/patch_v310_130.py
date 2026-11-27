# V310.130 · MONTANTS AU FORMAT DE LA LANGUE SUR LES PLATEFORMES (tâche 3 de la file de nuit, R32 R33 · vu par l'expert sur pg : « +600 $ » et « 1150 $ of 12 000 $ » en anglais)
# Anglais : « +$600 », « $1,150 of $12,000 » (dollar devant, virgule des milliers), partout : textes traduits, textes sans lettres (« +600 $ ») et compteurs (fmt, fmtSp)
# + D9 (tâche 4) : voir plus bas
# Espagnol, portugais, allemand : séparateur de milliers de la langue (1.150) · constancy.fr inchangé (français)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('const fmt = n => Math.round(n).toLocaleString("fr-FR");',
    'const NUM_LOC = LANG === "en" ? ({ es: "es-ES", pt: "pt-BR", de: "de-DE" }[LANG2] || "en-US") : "fr-FR"; /* V310.130 : nombres au format de la langue du joueur */\nconst fmt = n => Math.round(n).toLocaleString(NUM_LOC);')
rep('const fmtSp = n => String(Math.round(n)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\u202f");',
    'const fmtSp = n => NUM_LOC === "fr-FR" ? String(Math.round(n)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\u202f") : Math.round(n).toLocaleString(NUM_LOC);')
rep("  if (I18N.cache.size > 20000) I18N.cache.clear(); I18N.cache.set(t, r); return r; }",
    "  if (LANG === \"en\" && r && /\\d/.test(r) && /\\$/.test(r)) r = i18nMoney(r); /* V310.130 */\n  if (I18N.cache.size > 20000) I18N.cache.clear(); I18N.cache.set(t, r); return r; }\n"
    "/* V310.130 : montants au format de la langue : « +600 $ » → « +$600 », « 1 150 $ » → « $1,150 » en anglais ; espagnol, portugais, allemand : « 1.150 $ » */\n"
    "function i18nMoney(r) { const L = { es: \"es-ES\", pt: \"pt-BR\", de: \"de-DE\" }[LANG2] || \"en-US\", num = x => { const v = Number(String(x).replace(/[\\u00a0\\u202f ,]/g, \"\")); return isFinite(v) ? v.toLocaleString(L) : x; };\n"
    "  if (L === \"en-US\") return r.replace(/([+\\-−]?)(\\d{1,3}(?:[\\u00a0\\u202f ,]\\d{3})+|\\d+)[\\u00a0\\u202f ]?\\$/g, (m, sg, v) => sg + \"$\" + num(v)).replace(/\\$(\\d{1,3}(?:[\\u00a0\\u202f ]\\d{3})+|\\d{4,})(?!\\d)/g, (m, v) => \"$\" + num(v));\n"
    "  return r.replace(/(\\d{1,3}(?:[\\u00a0\\u202f ,]\\d{3})+|\\d{4,})(?=[\\u00a0\\u202f ]?\\$)/g, v => num(v)).replace(/\\$(\\d{1,3}(?:[\\u00a0\\u202f ]\\d{3})+|\\d{4,})(?!\\d)/g, (m, v) => \"$\" + num(v)); }")
# D9 (tâche 4 de la file de nuit) : sur les portes des plateformes, plus aucune étape du site (rêve, perso, mur, inscription, confirmation) envoyée à l'entonnoir du script : elles n'existent pas pour ces joueurs (perso créé tout seul, pas de mur)
rep("for (const [re, k] of FUNNEL) if (re.test(name)) { if (k === \"reve\") funnelHit(\"jouer\");",
    "for (const [re, k] of FUNNEL) if (re.test(name)) { if (PORTAL && /^(reve|perso|mur|murtape|murquitte|inscrit|confirme|confrenvoi|confquitte|confretour|confdt)/.test(k)) return; /* V310.130 · D9 : étapes du site jamais envoyées depuis les plateformes */ if (k === \"reve\") funnelHit(\"jouer\");")
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611280030';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
