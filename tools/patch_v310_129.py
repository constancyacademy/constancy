# V310.129 · POTEAUX DES ROUTES DE CAMPAGNE (tâche 2 de la file de nuit, R4 R5 · Thomas 27/11 17h10 : « des poteaux au milieu de la route » et « quand on les percute, ils ne tombent pas »)
# Poteaux en bois de la vieille route des Collines (D10) et de la route des Pins (D2), posés à 3,5 m du bord de LEUR route :
#  1. là où une autre route passe (carrefours, virages serrés, nationale, route du Mont), le poteau tombait dans la chaussée · maintenant on ne pose pas un poteau à moins de 2 m du bord d'une route (le câble va directement au suivant)
#  2. ils n'avaient aucune collision (on passait au travers) · maintenant : à l'arrêt ou au pas ils retiennent la voiture ; percutés au-dessus de 15 km/h, ils penchent puis tombent en 0,75 s du côté opposé à la voiture,
#     les câbles suivent leur sommet, la voiture garde 75 % de sa vitesse, choc de bois, secousse · ils restent couchés jusqu'au rechargement · un seul objet pour tous les poteaux (instances)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
OLD = '''  ["D10", "D2"].forEach(id => { const Q = RDX.list.find(q => q.D.id === id); if (!Q) return; const wood = periMats().wood, pts = []; for (let i = 3; i < Q.P.length; i += 11) { const [x, z] = Q.P[i], [bx, bz] = Q.P[Math.min(Q.P.length - 1, i + 1)], tx = bx - x, tz = bz - z, tl = Math.hypot(tx, tz) || 1, px = x - tz / tl * (Q.w / 2 + 3.5), pz = z + tx / tl * (Q.w / 2 + 3.5), y = GH(px, pz), c = { x: px, z: pz, y, ry: Math.atan2(tx, tz) };
      periPut(c, wood, new THREE.CylinderGeometry(0.16, 0.2, 9, 6), 0, 4.5, 0); periPut(c, wood, BX(2.4, 0.16, 0.16), 0, 8.4, 0); pts.push([px, y + 8.3, pz]); }
    const V = []; for (let i = 0; i < pts.length - 1; i++) { const [ax, ay, az] = pts[i], [bx2, by, bz2] = pts[i + 1]; for (let k = 0; k < 6; k++) { const t0 = k / 6, t1 = (k + 1) / 6, sg = t => -0.9 * Math.sin(Math.PI * t); V.push(ax + (bx2 - ax) * t0, ay + (by - ay) * t0 + sg(t0), az + (bz2 - az) * t0, ax + (bx2 - ax) * t1, ay + (by - ay) * t1 + sg(t1), az + (bz2 - az) * t1); } }
    const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.Float32BufferAttribute(V, 3)); scene.add(new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: 0x2a2622 }))); });'''
NEW = '''  /* V310.129 (Thomas 27/11 17h10 : poteaux au milieu de la route, qui ne tombent pas) : jamais à moins de 2 m du bord d'une route, retiennent la voiture, tombent si on les percute, câbles qui suivent */
  ["D10", "D2"].forEach(id => { const Q = RDX.list.find(q => q.D.id === id); if (!Q) return; const wood = periMats().wood, pts = []; for (let i = 3; i < Q.P.length; i += 11) { const [x, z] = Q.P[i], [bx, bz] = Q.P[Math.min(Q.P.length - 1, i + 1)], tx = bx - x, tz = bz - z, tl = Math.hypot(tx, tz) || 1, px = x - tz / tl * (Q.w / 2 + 3.5), pz = z + tx / tl * (Q.w / 2 + 3.5), y = GH(px, pz);
      if (roadDist(px, pz) < 2 || (typeof NAT !== "undefined" && nearNat(px, pz) < 9) || nearMRoad(px, pz) < 8 || onHighway(px, pz)) { WPOLE.skip++; continue; }
      const q = { x: px, z: pz, y, ry: Math.atan2(tx, tz), th: 0, st: 0, ax: 0, az: 0, road: WPOLE.roads.length, k: pts.length }; WPOLE.list.push(q); pts.push(q); }
    const V = new Float32Array(Math.max(0, pts.length - 1) * 36), g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(V, 3)); const R = { pts, V, g }; WPOLE.roads.push(R); for (let i = 0; i < pts.length - 1; i++) wpoleWire(R, i); g.computeBoundingSphere();
    const ls = new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: 0x2a2622 })); ls.frustumCulled = false; scene.add(ls); });
  try { wpoleBuild(); } catch (e) { console.warn("poteaux", e); }'''
rep(OLD, NEW)
CODE = r'''/* V310.129 · poteaux en bois des routes de campagne : collision, chute quand on les percute, câbles qui suivent */
var WPOLE = { list: [], roads: [], grid: new Map(), skip: 0, im: null, falling: [] }, _wpO = new THREE.Object3D(), _wpQ = new THREE.Quaternion(), _wpA = new THREE.Vector3(), _wpV = new THREE.Vector3();
function wpoleTop(q) { _wpV.set(0, 8.3, 0); if (q.th) { _wpA.set(q.ax, 0, q.az); _wpQ.setFromAxisAngle(_wpA, q.th); _wpV.applyQuaternion(_wpQ); } return [q.x + _wpV.x, q.y + _wpV.y, q.z + _wpV.z]; }
function wpoleWire(R, i) { const A = wpoleTop(R.pts[i]), B = wpoleTop(R.pts[i + 1]), V = R.V, o = i * 36; for (let k = 0; k < 6; k++) { const t0 = k / 6, t1 = (k + 1) / 6, sg = t => -0.9 * Math.sin(Math.PI * t), j = o + k * 6; V[j] = A[0] + (B[0] - A[0]) * t0; V[j + 1] = A[1] + (B[1] - A[1]) * t0 + sg(t0); V[j + 2] = A[2] + (B[2] - A[2]) * t0; V[j + 3] = A[0] + (B[0] - A[0]) * t1; V[j + 4] = A[1] + (B[1] - A[1]) * t1 + sg(t1); V[j + 5] = A[2] + (B[2] - A[2]) * t1; } }
function wpoleMatrix(i) { const q = WPOLE.list[i]; _wpO.position.set(q.x, q.y, q.z); _wpO.quaternion.setFromAxisAngle(_wpA.set(0, 1, 0), q.ry); if (q.th) { _wpQ.setFromAxisAngle(_wpA.set(q.ax, 0, q.az), q.th); _wpO.quaternion.premultiply(_wpQ); } _wpO.scale.set(1, 1, 1); _wpO.updateMatrix(); WPOLE.im.setMatrixAt(i, _wpO.matrix); }
function wpoleBuild() { const L = WPOLE.list; if (!L.length) return; const a = new THREE.CylinderGeometry(0.16, 0.2, 9, 6); a.translate(0, 4.5, 0); const b = new THREE.BoxGeometry(2.4, 0.16, 0.16); b.translate(0, 8.4, 0);
  WPOLE.im = new THREE.InstancedMesh(THREE.BufferGeometryUtils.mergeBufferGeometries([a.toNonIndexed(), b.toNonIndexed()]), periMats().wood, L.length); WPOLE.im.frustumCulled = false; L.forEach((q, i) => { wpoleMatrix(i); const k = Math.floor(q.x / 16) + "," + Math.floor(q.z / 16); if (!WPOLE.grid.has(k)) WPOLE.grid.set(k, []); WPOLE.grid.get(k).push(i); }); WPOLE.im.instanceMatrix.needsUpdate = true; scene.add(WPOLE.im); }
function hitWoodPoles(c) { if (!WPOLE.im || c.z > -400) return; const fx = Math.sin(c.h), fz = Math.cos(c.h); for (const k0 of [1.45, 0]) { const ox = c.x + fx * k0, oz = c.z + fz * k0, gx = Math.floor(ox / 16), gz = Math.floor(oz / 16);
  for (let a = gx - 1; a <= gx + 1; a++) for (let b = gz - 1; b <= gz + 1; b++) { const l = WPOLE.grid.get(a + "," + b); if (!l) continue; for (const i of l) { const q = WPOLE.list[i]; if (q.st) continue; const dx = q.x - ox, dz = q.z - oz, d = Math.hypot(dx, dz), m = 1.15 + 0.2; if (d > m) continue;
      const av = Math.abs(c.v); if (av < 4.2) { const nx = dx / (d || 1), nz = dz / (d || 1); c.x -= nx * (m - d); c.z -= nz * (m - d); continue; }
      const mx = fx * Math.sign(c.v || 1), mz = fz * Math.sign(c.v || 1); q.st = 1; q.t = 0; const L = Math.hypot(mx, mz) || 1; q.ax = mz / L; q.az = -mx / L; WPOLE.falling.push(i); c.v *= 0.75;
      try { noiseHit(0.3, 420, 0.6, 0.18); } catch (e) {} try { shakeAdd(Math.min(0.5, 0.15 + av / 60)); } catch (e) {} try { navigator.vibrate && navigator.vibrate(30); } catch (e) {} if (!WPOLE.s) { WPOLE.s = 1; try { stat("poteau-tombe"); } catch (e) {} } } } } }
function updateWoodPoles(dt) { if (!WPOLE.falling.length) return; for (let f = WPOLE.falling.length - 1; f >= 0; f--) { const i = WPOLE.falling[f], q = WPOLE.list[i]; q.t += dt; q.th = Math.min(1.42, 1.42 * Math.pow(q.t / 0.75, 2)); if (q.th >= 1.42) { q.st = 2; WPOLE.falling.splice(f, 1); try { noiseHit(0.22, 260, 0.5, 0.25); } catch (e) {} }
    wpoleMatrix(i); const R = WPOLE.roads[q.road]; if (q.k > 0) wpoleWire(R, q.k - 1); if (q.k < R.pts.length - 1) wpoleWire(R, q.k); R.g.attributes.position.needsUpdate = true; } WPOLE.im.instanceMatrix.needsUpdate = true; }
'''
rep("const FIRE = { on: false };", CODE + "const FIRE = { on: false };")
rep("hitPosts(c, c.v, c.h, 1.1);\n  for (const k of [L, -L, 0])", "hitPosts(c, c.v, c.h, 1.1); try { hitWoodPoles(c); } catch (e) {}\n  for (const k of [L, -L, 0])")
rep('try { updateXmas(dt); } catch (e) { console.warn("noel", e); }', 'try { updateXmas(dt); } catch (e) { console.warn("noel", e); } try { updateWoodPoles(dt); } catch (e) {}')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611280010';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
