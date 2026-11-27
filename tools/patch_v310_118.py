# V310.118 · NOËL (commande BUSINESS 27/11 13h55, point 3 : « décor progressif dès le 1/12, sapin géant sur la place, cadeaux sous le sapin chaque jour, neige le 20/12 ») · constancy.fr et plateformes
# Actif du 1er décembre au 6 janvier (date réelle du joueur), sinon rien n'est construit · ?noel=<jour> pour tester ou filmer (ex. ?noel=20)
# Jour 1+ : sapin géant de 23 m dans le parc juste au sud du Dépôt (-28, 140), planté dans le bassin de la fontaine (formes simples), guirlande de 150 lumières rose, cyan, or et blanc qui scintille, étoile dorée · Jour 8+ : 12 cadeaux au pied · Jour 20+ : neige autour du joueur (hors intérieurs)
# Chaque jour, s'approcher du sapin (à pied dans le parc, ou en voiture dans une des 4 rues qui le bordent, 27 m) donne le cadeau du jour (300 $ + 50 $ par jour de décembre, 2 000 $ au plus) · bulle d'annonce une fois par jour pour les joueurs qui ont déjà livré · rien avant 12 s de jeu (aucun bug au début) · stats noel-sapin, noel-annonce, noel-cadeau
import re, sys, json
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
CODE = r'''/* V310.118 · NOËL (commande BUSINESS du 27/11 13h55) : du 1er décembre au 6 janvier, sapin géant dans le parc au sud du Dépôt, guirlande, étoile, cadeaux au pied dès le 8, neige dès le 20, un cadeau du jour sous le sapin · formes simples, aucune lumière ajoutée · ?noel=<jour> pour tester */
const XM = { built: false, off: false, X: -28, Z: 140 };
function xmasDay() { const q = /[?&]noel=(\d+)/.exec(location.search); if (q) return +q[1]; const d = new Date(); if (d.getMonth() === 11) return d.getDate(); if (d.getMonth() === 0 && d.getDate() <= 6) return 31 + d.getDate(); return 0; }
function xmasBuild() { XM.built = true; const D = XM.day, y0 = GH(XM.X, XM.Z), g = new THREE.Group(); g.name = "sapin"; g.position.set(XM.X, y0, XM.Z);
  const gm = new THREE.MeshLambertMaterial({ color: 0x1d5a33, emissive: 0x0b2414, side: THREE.DoubleSide }), tm = new THREE.MeshLambertMaterial({ color: 0x5a3a22 }); const tr = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 1.2, 4, 10), tm); tr.position.y = 2; g.add(tr);
  const LY = [[7.8, 7, 5.5], [6.6, 6.5, 8.8], [5.4, 6, 11.8], [4.2, 5.5, 14.6], [3.0, 5, 17.2], [1.8, 4.5, 19.8]]; LY.forEach(([r, h, y]) => { const c = new THREE.Mesh(new THREE.ConeGeometry(r, h, 20, 1, true), gm); c.position.y = y; g.add(c); });
  const N = 152, cols = [0xff2d95, 0x3fe0ff, 0xffd36e, 0xffffff], sg = new THREE.SphereGeometry(0.17, 6, 5), dm = new THREE.Object3D(); XM.lights = cols.map(c => { const m = new THREE.InstancedMesh(sg, new THREE.MeshBasicMaterial({ color: c }), N / cols.length); m.frustumCulled = false; g.add(m); return m; }); const cnt = [0, 0, 0, 0];
  const RS = LY.reduce((t, l) => t + l[0], 0); let k = 0; LY.forEach(([R, h, y], li) => { const n = li === LY.length - 1 ? N - k : Math.round(N * R / RS); for (let q = 0; q < n && k < N; q++, k++) { const f = 0.05 + 0.6 * ((q * 0.618) % 1), a = q * 2.39996 + li, r = R * (1 - f) + 0.12; dm.position.set(Math.cos(a) * r, y - h / 2 + f * h, Math.sin(a) * r); dm.updateMatrix(); const ci = k % 4; XM.lights[ci].setMatrixAt(cnt[ci]++, dm.matrix); } }); XM.lights.forEach(m => { m.instanceMatrix.needsUpdate = true; });
  const st = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTexture(), color: 0xffd36e, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending })); st.scale.set(7, 7, 1); st.position.y = 22.6; g.add(st); XM.star = st;
  if (D >= 8) { const bg = new THREE.BoxGeometry(1, 1, 1), rb = new THREE.BoxGeometry(1.03, 1.03, 0.16), rm = new THREE.MeshLambertMaterial({ color: 0xfff3c4 }), pc = [0xff2d95, 0x3fe0ff, 0xffd36e, 0x8b5cf6, 0xffffff, 0xe11d48]; for (let k = 0; k < 12; k++) { const a = k / 12 * 6.283 + 0.3, r = 8.6 + (k % 3) * 0.9, sz = 0.9 + (k % 4) * 0.35, m = new THREE.Mesh(bg, new THREE.MeshLambertMaterial({ color: pc[k % pc.length] })); m.scale.setScalar(sz); m.position.set(Math.cos(a) * r, sz / 2, Math.sin(a) * r); m.rotation.y = a; const r1 = new THREE.Mesh(rb, rm), r2 = new THREE.Mesh(rb, rm); r2.rotation.y = Math.PI / 2; m.add(r1); m.add(r2); g.add(m); } }
  scene.add(g); XM.g = g; stat("noel-sapin"); }
function xmasSnowInit() { const N = 1400, pos = new Float32Array(N * 3); for (let i = 0; i < N; i++) { pos[i * 3] = (Math.random() - 0.5) * 70; pos[i * 3 + 1] = Math.random() * 40; pos[i * 3 + 2] = (Math.random() - 0.5) * 70; } const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(pos, 3)); XM.snow = new THREE.Points(g, new THREE.PointsMaterial({ color: 0xffffff, map: (() => { const c = document.createElement("canvas"); c.width = c.height = 32; const x = c.getContext("2d"), gr = x.createRadialGradient(16, 16, 1, 16, 16, 15); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(0.5, "rgba(240,246,255,0.7)"); gr.addColorStop(1, "rgba(230,240,255,0)"); x.fillStyle = gr; x.fillRect(0, 0, 32, 32); return new THREE.CanvasTexture(c); })(), size: 0.42, transparent: true, opacity: 0.95, depthWrite: false })); XM.snow.frustumCulled = false; scene.add(XM.snow); }
function updateXmas(dt) { if (XM.off) return; if (XM.day == null) { XM.day = xmasDay(); if (!XM.day) { XM.off = true; return; } } if (G.mode !== "play" || !G.playT0 || performance.now() - G.playT0 < 12000) return;
  if (!XM.built) { try { xmasBuild(); } catch (e) { XM.off = true; console.warn("noel", e); return; } } const T = performance.now() / 1000;
  if (XM.star) XM.star.material.opacity = 0.75 + 0.25 * Math.sin(T * 3); if (XM.lights) { const k = Math.floor(T * 1.6) % 4; XM.lights.forEach((m, i) => { m.visible = i !== k || Math.sin(T * 9) < 0.5; }); }
  if (P && !CREATOR && (P.deliveries || 0) > 0 && P.xmasA !== todayStr() && !G.mission && !CINE.on && !G.inside && performance.now() - G.playT0 > 20000) { P.xmasA = todayStr(); saveNow(); stat("noel-annonce"); notify("gold", "🎄 <b>Le sapin de Noël</b> est dans le parc juste au sud du Dépôt. Un cadeau t'attend dessous chaque jour.", 8); }
  const o = G.onFoot ? G.me : G.car; if (P && !CREATOR && P.xmasG !== todayStr() && !CINE.on && Math.hypot(o.x - XM.X, o.z - XM.Z) < 27) { P.xmasG = todayStr(); const amt = Math.min(2000, 300 + 50 * XM.day); addCash(amt, true); try { cashFly(amt); } catch (e) {} saveNow(); stat("noel-cadeau"); try { sfx.win(); } catch (e) {} notify("gold", `🎁 <b>Cadeau du jour sous le sapin</b> · +$${amt}. Reviens demain, il y en a un nouveau.`, 7); }
  if (XM.day >= 20) { if (!XM.snow) xmasSnowInit(); const sn = XM.snow; sn.visible = !G.inside; if (sn.visible) { sn.position.set(camera.position.x, camera.position.y - 12, camera.position.z); const a = sn.geometry.attributes.position, A = a.array; for (let i = 0; i < A.length; i += 3) { A[i + 1] -= dt * (2 + (i % 7) * 0.15); A[i] += Math.sin(T + i) * dt * 0.3; if (A[i + 1] < 0) A[i + 1] += 40; } a.needsUpdate = true; } } }
'''
rep("const FIRE = { on: false };", CODE + "const FIRE = { on: false };")
rep('try { updateCiterne(dt); } catch (e) { console.warn("citerne", e); }', 'try { updateCiterne(dt); } catch (e) { console.warn("citerne", e); } try { updateXmas(dt); } catch (e) { console.warn("noel", e); }')
open(p, "w", encoding="utf-8").write(s)
T = {"Le sapin de Noël": ["The Christmas tree", "El árbol de Navidad", "A árvore de Natal", "Der Weihnachtsbaum"],
     "est dans le parc juste au sud du Dépôt. Un cadeau t'attend dessous chaque jour.": ["is in the park just south of the Depot. A gift waits under it every day.", "está en el parque, justo al sur del Depósito. Cada día te espera un regalo debajo.", "está no parque, logo ao sul do Depósito. Todo dia tem um presente te esperando embaixo.", "steht im Park gleich südlich vom Depot. Jeden Tag wartet ein Geschenk darunter."],
     "Cadeau du jour sous le sapin": ["Today's gift under the tree", "Regalo del día bajo el árbol", "Presente do dia embaixo da árvore", "Geschenk des Tages unter dem Baum"],
     "· +$#. Reviens demain, il y en a un nouveau.": ["· +$#. Come back tomorrow, there's a new one.", "· +$#. Vuelve mañana, habrá otro.", "· +$#. Volte amanhã, vai ter outro.", "· +$#. Komm morgen wieder, dann gibt es ein neues."]}
en = json.load(open("assets/i18n/en.json", encoding="utf-8"))
for k, v in T.items(): en[k] = v[0]
json.dump(en, open("assets/i18n/en.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
for i, L in enumerate(["es", "pt", "de"]):
    f = "assets/i18n/%s.json" % L; d = json.load(open(f, encoding="utf-8"))
    for k, v in T.items(): d[v[0]] = v[i + 1]
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272030';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
