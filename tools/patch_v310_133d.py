# V310.133 (suite 3) · POINT 4 DE LA BUSINESS (28/11 10h00) · PREMIÈRE LIVRAISON ÉVIDENTE, plateformes seulement (83 joueurs cg en jeu, 26 à la 1re mission)
# - grosse flèche violette au-dessus de la voiture, qui montre le chemin du GPS jusqu'au client (toujours visible, elle tourne avec le trajet)
# - bandeau en haut : « Livre ta première commande · suis la flèche violette »
# - rappel au bout de 15 s sans rouler (3 fois au plus) : comment rouler, au clavier ou au pouce
# - plus de grand titre « Tu es à … » au milieu de l'écran pendant cette 1re livraison
import os
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('try { updateXmas(dt); } catch (e) { console.warn("noel", e); }', 'try { updateXmas(dt); } catch (e) { console.warn("noel", e); } try { updateR3Guide(dt); } catch (e) { console.warn("fleche r3", e); }')
rep('function r3Pulse(on) {', '''/* V310.133 · POINT 4 (BUSINESS 28/11 10h00) : sur les plateformes, la 1re livraison se comprend sans lire · flèche 3D au-dessus de la voiture vers le prochain point du GPS, bandeau court en haut, rappel après 15 s à l'arrêt */
const R3A = { g: null, t: 0, dir: null, idle: 0, n: 0, ban: null, on: false };
function r3Arrow() { if (R3A.g) return R3A.g; const sh = new THREE.Shape([[0, 1.7], [1.25, 0.15], [0.48, 0.15], [0.48, -1.3], [-0.48, -1.3], [-0.48, 0.15], [-1.25, 0.15]].map(([x, y]) => new THREE.Vector2(x, y))); const geo = new THREE.ShapeGeometry(sh); geo.rotateX(-Math.PI / 2);
  const mk = (c, o, sc, ro) => { const m = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: o, depthTest: false, depthWrite: false, side: THREE.DoubleSide, fog: false })); m.scale.setScalar(sc); m.renderOrder = ro; return m; };
  const g = new THREE.Group(), tilt = new THREE.Group(); tilt.rotation.x = 1.0; tilt.add(mk(0x14062a, 0.55, 1.16, 998)); const f = mk(0xc77dff, 0.97, 1, 999); f.position.y = 0.02; tilt.add(f); g.add(tilt); g.visible = false; g.frustumCulled = false; scene.add(g); R3A.g = g; return g; }
function r3Ban(on) { if (on && !R3A.ban) { const d = document.createElement("div"); d.id = "r3Ban"; d.style.cssText = "position:fixed;left:50%;top:calc(74px + env(safe-area-inset-top));transform:translateX(-50%);z-index:45;pointer-events:none;white-space:nowrap;max-width:94vw;overflow:hidden;text-overflow:ellipsis;padding:8px 18px;border-radius:999px;background:rgba(20,6,42,.78);border:2px solid #c77dff;color:#fff;font:800 clamp(14px,2.3vw,20px) Inter,system-ui,sans-serif;box-shadow:0 6px 24px rgba(199,125,255,.35);transition:opacity .4s"; d.innerHTML = '<b style="color:#c77dff">▲</b> <span>Livre ta première commande · suis la flèche violette</span>'; document.body.appendChild(d); R3A.ban = d; try { stat("r3-fleche-vue"); } catch (e) {} } if (!on && R3A.ban) { R3A.ban.remove(); R3A.ban = null; } }
function updateR3Guide(dt) { const M = G.mission, on = !!(PORTAL && !CREATOR && M && M.r3 && M.type === "livraison" && G.mode === "play" && !G.inside && !CINE.on && P && (P.deliveries || 0) === 0);
  if (!on) { if (R3A.on) { R3A.on = false; if (R3A.g) R3A.g.visible = false; r3Ban(false); } return; } R3A.on = true; r3Ban(true); const g = r3Arrow(), o = target(), dd = Math.hypot(M.dx - o.x, M.dz - o.z);
  R3A.t -= dt; if (R3A.t <= 0) { R3A.t = 0.4; let tx = M.dx, tz = M.dz; try { const r = gpsRoute(); if (r && r.pts) { for (const q of r.pts) { if (Math.hypot(q[0] - o.x, q[1] - o.z) > 14) { tx = q[0]; tz = q[1]; break; } } } } catch (e) {} R3A.dir = Math.atan2(-(tx - o.x), -(tz - o.z)); }
  const y0 = (!G.onFoot && carMesh ? carMesh.position.y : (meMesh ? meMesh.position.y : 0)) || 0; g.visible = !G.onFoot && dd > 18; const ch = G.onFoot ? 0 : (G.car.h || 0); g.position.set(o.x + Math.sin(ch) * 2.5, y0 + 3.0 + Math.sin(performance.now() / 260) * 0.2, o.z + Math.cos(ch) * 2.5); g.scale.setScalar(1.05); /* au-dessus de la voiture, un peu devant */ if (R3A.dir != null) { let a = R3A.dir - g.rotation.y; a = Math.atan2(Math.sin(a), Math.cos(a)); g.rotation.y += a * Math.min(1, dt * 6); }
  const still = G.onFoot ? (G.me.speed || 0) < 0.5 : Math.abs(G.car.v || 0) < 0.8; const nw = performance.now(); if (!still || !R3A.i0) R3A.i0 = nw; R3A.idle = (nw - R3A.i0) / 1000; /* temps réel */
  if (R3A.idle > 15 && R3A.n < 3) { R3A.n++; R3A.i0 = nw; try { stat("r3-rappel-15s-" + R3A.n); } catch (e) {} help(TOUCH_DEV() ? "Glisse le pouce vers le haut pour rouler. Suis la flèche violette." : "Reste appuyé sur ↑ ou W pour rouler. Suis la flèche violette.", 6); try { sfx.ping(); } catch (e) {} } }
function r3Pulse(on) {''')
rep('if (n && n !== ZT.cur && ZT.ct > 1.2 && !document.getElementById("rexGauge")', 'if (n && n !== ZT.cur && ZT.ct > 1.2 && !document.getElementById("r3Ban") && !document.getElementById("rexGauge")')
open(p, "w", encoding="utf-8").write(s); print("OK", n, "remplacements")
