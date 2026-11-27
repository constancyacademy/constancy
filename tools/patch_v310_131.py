# V310.131 · CRAZYGAMES : ÉCRAN « ▶ PLAY » LÉGER COMME POKI (expert 27/11 nuit, tâche 1 · Thomas : « Il faut vraiment qu'on n'ait plus ce genre de bug »)
# Constat de CrazyGames sur la V310.117 : 24,2 Mo téléchargés avant le début du jeu et 22,8 s de chargement (au-dessus de 20 Mo, pas de page d'accueil mobile)
# Sur la porte cg, la ville, les modèles et les sons ne partent qu'après le premier toucher sur l'écran « ▶ PLAY » (même écran que Poki, V310.97) ;
# le SDK CrazyGames reçoit loadingStop dès que cet écran est prêt (le jeu est jouable : un toucher), gameplayStart à l'entrée en jeu comme avant · stats cg-titre, cg-play
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('const PKH = (PORTAL === "pk" && !CREATOR) ? new Promise(ok => {',
    'const PKH = ((PORTAL === "pk" || PORTAL === "cg") && !CREATOR) ? new Promise(ok => { /* V310.131 : aussi sur CrazyGames */')
rep('window.__pkTitle = 1; stat("pk-titre"); try { PSDK.pk && PSDK.pk.gameLoadingFinished(); } catch (e) {} }',
    'window.__pkTitle = 1; stat(PORTAL + "-titre"); try { PSDK.pk && PSDK.pk.gameLoadingFinished(); } catch (e) {} if (PORTAL === "cg") { window.__cgTitle = Date.now(); try { if (PSDK.cg && !PSDK.ready) { PSDK.ready = true; PSDK.cg.game.loadingStop(); } } catch (e) {} } }')
rep('window.__pkWait = 0; window.__pkT = Date.now(); stat("pk-play");',
    'window.__pkWait = 0; window.__pkT = Date.now(); stat(PORTAL + "-play");')
rep('PSDK.cg = window.CrazyGames.SDK; try { if (!PSDK.ready) PSDK.cg.game.loadingStart(); } catch (e) {}',
    'PSDK.cg = window.CrazyGames.SDK; try { if (window.__cgTitle) { if (!PSDK.ready) { PSDK.ready = true; PSDK.cg.game.loadingStop(); } } else if (!PSDK.ready) PSDK.cg.game.loadingStart(); } catch (e) {} /* V310.131 : écran « Play » déjà là = jeu prêt */')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611280015';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
