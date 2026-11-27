# V310.124 · 30 OU 60 I/S SUR ORDINATEUR (Thomas, 27/11 17h03 : « une fois sur deux, on a des images en 30 fps et pas en 60 ») : MESURER CHEZ LES VRAIS JOUEURS
# 1. une mesure par partie, 40 s après l'entrée en jeu puis à 3 min (10 s chacune) : statistique « fps-<pc|tel>-<60|45|30|20>-pr<définition> » puis « fps3m-… »
#    (sur ordinateur : on saura combien de parties tournent à 30, et à quelle définition)
# 2. compteur ?fps=1 plus complet : définition rendue, densité d'écran, filtre de couleur ôté ou non, halo, nombre de crans retirés
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep("function fpsTick(dt) { if (!FPSC.on) return;",
    "/* V310.124 : une mesure de fluidité par partie chez les vrais joueurs (40 s puis 3 min après l'entrée en jeu, 10 s chacune) */\n"
    "const FPSM = { k: 0, n: 0, t0: 0 };\n"
    "function fpsMeasure(dt) { const now = performance.now(); if (FPSM.k > 1 || G.mode !== \"play\" || !G.playT0 || document.hidden || G.map3d) { FPSM.n = 0; FPSM.t0 = 0; return; } if (now - G.playT0 < (FPSM.k ? 180000 : 40000)) return; if (!FPSM.t0) { FPSM.t0 = now; FPSM.n = 0; return; } FPSM.n++; if (now - FPSM.t0 < 10000) return;\n"
    "  const f = FPSM.n / ((now - FPSM.t0) / 1000), b = f >= 52 ? 60 : f >= 38 ? 45 : f >= 26 ? 30 : 20, fine = !!(window.matchMedia && matchMedia(\"(pointer:fine)\").matches), pr = renderer ? renderer.getPixelRatio() : 0; try { stat((FPSM.k ? \"fps3m-\" : \"fps-\") + (fine ? \"pc\" : \"tel\") + \"-\" + b + \"-pr\" + pr.toFixed(2)); } catch (e) {} window.__fpsM = (window.__fpsM || []).concat([{ f: +f.toFixed(1), pr, dpr: devicePixelRatio, w: innerWidth, h: innerHeight }]); FPSM.k++; FPSM.n = 0; FPSM.t0 = 0; }\n"
    "function fpsTick(dt) { try { fpsMeasure(dt); } catch (e) {} if (!FPSC.on) return;")
rep("FPSC.el.textContent = `${f.toFixed(0)} i/s\\n${ri ? ri.render.calls : 0} dessins · ${ri ? Math.round(ri.render.triangles / 1000) : 0} k tri\\nmém ${mem}`;",
    "{ const PF = loop.pf || {}; FPSC.el.textContent = `${f.toFixed(0)} i/s\\n${ri ? ri.render.calls : 0} dessins · ${ri ? Math.round(ri.render.triangles / 1000) : 0} k tri\\nmém ${mem}\\ndéf ${renderer ? renderer.getPixelRatio().toFixed(2) : \"?\"} / écran ${devicePixelRatio} · ${Math.round(innerWidth * innerHeight * Math.pow(renderer ? renderer.getPixelRatio() : 1, 2) / 1e5) / 10} Mpx\\nfiltre ${cv.classList.contains(\"nograde\") ? \"ôté\" : \"oui\"} · halo ${typeof FXR !== \"undefined\" && FXR.on ? \"oui\" : \"non\"}${PF.cap ? \" · plafond \" + PF.cap.toFixed(2) : \"\"}`; }")
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272240';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
