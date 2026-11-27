# V310.110 · « NOUVEAU CETTE SEMAINE » DANS LE JEU (commande BUSINESS 27/11 13h55, point 3 : « Une nouveauté visible par semaine minimum, annoncée dans le jeu ») · constancy.fr et plateformes
# Un joueur qui revient (Jour 2 ou plus) reçoit une fois la bulle des nouveautés, 8 s après être en jeu, jamais pendant une mission, une scène ou à l'intérieur · stat nouveaute-vue-<semaine>
# Pour annoncer la semaine suivante : changer NEWS.id et NEWS.t (une ligne)
import re, sys, json
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
A = "setInterval(() => { try { pgAdBtn(); } catch (e) {} }, 2000);"
rep(A, A + '''
/* V310.110 · « Nouveau cette semaine » (commande BUSINESS du 27/11 13h55, point 3) : un joueur qui revient reçoit une fois la bulle des nouveautés de la semaine, 8 s après être en jeu, hors mission, scène et intérieur · changer NEWS.id et NEWS.t chaque semaine */
const NEWS = { id: "2026-s48", t: "<b>Nouveau cette semaine</b> · Le Rex s'échappe du parc : ramène-le avant tout le monde. · L'incendie de Mamie Josette : attention à la citerne." };
setInterval(() => { try { if (!P || CREATOR || G.mode !== "play" || (P.day || 1) < 2 || P.news === NEWS.id || G.mission || G.inside || CINE.on || (typeof REXE !== "undefined" && REXE.on) || FIRE.on || !G.playT0 || performance.now() - G.playT0 < 8000 || [...document.querySelectorAll(".panel")].some(e => e.getClientRects().length)) return; P.news = NEWS.id; saveNow(); stat("nouveaute-vue-" + NEWS.id); notify("gold", NEWS.t, 9); } catch (e) {} }, 2000);''')
open(p, "w", encoding="utf-8").write(s)
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
d.update({"Nouveau cette semaine": "New this week", "· Le Rex s'échappe du parc : ramène-le avant tout le monde. · L'incendie de Mamie Josette : attention à la citerne.": "· The Rex escaped from the park: bring it back before anyone else. · Grandma Josette's fire: watch out for the gas tanker."})
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271900';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
