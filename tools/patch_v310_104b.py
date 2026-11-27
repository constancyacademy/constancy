# V310.104 (suite) · Rex : jauge qui ne chevauche plus le titre « Tu es à… », textes anglais des plateformes, post du fil sans « ce soir »
import json, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:80]))
    s = s.replace(a, b); n += 1
rep('Le Rex est sorti du parc ce soir.', "Le Rex est sorti du parc aujourd'hui.")
rep('if (n && n !== ZT.cur && ZT.ct > 1.2) { ZT.cur = n;', 'if (n && n !== ZT.cur && ZT.ct > 1.2 && !document.getElementById("rexGauge")) { ZT.cur = n; /* V310.104 : pas de titre de zone sous la jauge du Rex */')
rep('b.id = "rexGauge";', 'b.id = "rexGauge"; try { if (ZT.el) ZT.el.style.opacity = 0; } catch (e) {}')
open(p, "w", encoding="utf-8").write(s)
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
d.update({
 "Alerte radio :": "Radio alert:",
 "« Le Rex est sorti de la ZONE # ! » Va au camion des gardiens, à # m, pour prendre l'appât.": "“The Rex broke out of ZONE #!” Drive to the rangers' truck, # m away, to pick up the bait.",
 "🦖 Distance du Rex ·": "🦖 Rex distance ·",
 "Appât chargé.": "Bait loaded.",
 "Passe devant le Rex et ramène-le au portail du parc. Reste entre # et # m devant lui.": "Get in front of the Rex and lead it back to the park gate. Stay # to # m ahead of it.",
 "Le Rex s'arrête et rugit.": "The Rex stops and roars.",
 "Reviens devant lui.": "Get back in front of it.",
 "Le Rex est rentré.": "The Rex is back.",
 "Le portail se referme. Les gardiens applaudissent.": "The gate closes. The rangers cheer.",
 "Badge · Dompteur": "Badge · Rex Tamer",
 "Les gardiens l'ont endormi et ramené. Personne n'est blessé.": "The rangers put it to sleep and brought it back. Nobody got hurt.",
 "Le Rex est sorti du parc aujourd'hui. Un livreur l'a ramené tout seul. Respect. 🦖": "The Rex got out of the park today. A delivery driver brought it back on his own. Respect. 🦖",
})
for k in ["# m", "+$#"]: print(k, "->", d.get(k))
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("OK", n)
