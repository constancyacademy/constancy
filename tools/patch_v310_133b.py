# V310.133 (suite) · CrazyGames : les arbres 3D de près (flamboyants, palmiers royaux, cocotiers) se téléchargent une fois en jeu · avant, les mêmes arbres en photo (déjà le cas au loin)
import os
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('zones: ["mont", "parc", "lieux"] };', 'zones: ["mont", "parc", "lieux"], w: [] };\nfunction cgAfter(f) { if (CGL.on && !CGL.p) CGL.w.push(f); else f(); }')
rep('CGL.t0 = performance.now(); try { stat("cg-suite-debut"); } catch (e) {}', 'CGL.t0 = performance.now(); try { stat("cg-suite-debut"); } catch (e) {} CGL.p = 1; CGL.w.splice(0).forEach(f => { try { f(); } catch (e) {} });')
rep('  new THREE.GLTFLoader().load(V.glb, gl => {', '  cgAfter(() => new THREE.GLTFLoader().load(V.glb, gl => {')
rep('V.near.count = 0; V.near.frustumCulled = false; scene.add(V.near); V.t = 1; }, undefined, () => {}); }', 'V.near.count = 0; V.near.frustumCulled = false; scene.add(V.near); V.t = 1; }, undefined, () => {})); }')
rep('scene.add(PALMX.near); PALMX.t = 1; }, undefined, () => {});\n}', 'scene.add(PALMX.near); PALMX.t = 1; }, undefined, () => {}));\n}')
rep('new THREE.GLTFLoader().load("assets/veg_palm.json", gl => {', 'cgAfter(() => new THREE.GLTFLoader().load("assets/veg_palm.json", gl => {')
open(p, "w", encoding="utf-8").write(s); print("OK", n, "remplacements")
