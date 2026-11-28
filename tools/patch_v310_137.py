# V310.137 · URGENCE (Thomas, 28/11 15h14 : « écran noir sur ordinateur », appli installée et site) · reproduit dans le Chrome de l'iMac (vraie carte graphique) :
# à chaque image, three.js r128 plante dans le rendu (« Cannot read properties of undefined (reading 'position') », uniforms des lumières) : un matériau garde un programme compilé
# pour un autre nombre de lumières (bogue connu de r128 quand deux rendus ont le même numéro d'état des lumières) → rien n'est dessiné, écran noir, interface normale.
# Correctif : si le rendu plante, tous les matériaux de la scène sont recompilés (une fois toutes les 0,5 s au plus) et l'image suivante repart · le bloom n'est coupé qu'après 3 échecs.
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('try { FXR.comp.render(); return; } catch (e) { FXR.on = false; FXR.fail = true; }',
    'try { FXR.comp.render(); return; } catch (e) { if (renderHeal(e) && RHEAL.n < 3) return; FXR.on = false; FXR.fail = true; }')
rep('  renderer.render(scene, camera); }',
    '  try { renderer.render(scene, camera); } catch (e) { renderHeal(e); } }\n'
    '/* V310.137 · écran noir sur ordinateur : un rendu qui plante recompile tous les matériaux au lieu de laisser l\'écran noir */\n'
    'const RHEAL = { n: 0, t: 0 };\n'
    'function renderHeal(e) { const now = performance.now(); if (now - RHEAL.t < 500) return false; RHEAL.t = now; RHEAL.n++; try { console.warn("rendu réparé", RHEAL.n, e && e.message); } catch (er) {} try { if (RHEAL.n === 1) stat("rendu-repare"); if (RHEAL.n === 10) stat("rendu-repare-10"); } catch (er) {}\n'
    '  try { scene.traverse(o => { const m = o.material; if (!m) return; (Array.isArray(m) ? m : [m]).forEach(x => { if (x) x.needsUpdate = true; }); }); } catch (er) {} return true; }')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611281540';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
