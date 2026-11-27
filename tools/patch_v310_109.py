# V310.109 · « LA CITERNE » (commande BUSINESS du 26/11 20h58, missions spectaculaires, point 2 · Thomas : « Faut créer des explosions… sans pour autant qu'on promulgue la violence »)
# Pendant l'incendie de Mamie Josette, une citerne de gaz est garée devant l'immeuble · au moment où Mamie sort, elle explose : boule de feu, onde de choc au sol, débris, colonne de fumée, éclair, écran qui tremble, grondement, sirènes · personne n'est blessé · carcasse noire qui brûle jusqu'à la fin · stat feu-citerne-boum
# Rien de chargé en plus : formes simples (boîtes, cylindres), textures de feu et de fumée déjà là, aucune lumière ajoutée (pas de recompilation des shaders)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
FN = r'''/* V310.109 · « LA CITERNE » (commande BUSINESS du 26/11 20h58 · Thomas : « des explosions… sans violence ») : une citerne de gaz garée devant l'immeuble en feu explose au moment où Mamie sort · personne n'est blessé · formes simples, aucune lumière ajoutée */
function fireTank(sp) { if (FIRE.tank || !FIRE.grp) return; const g = new THREE.Group(); FIRE.tGeo = FIRE.tGeo || []; const add = (geo, col, x, y, z, rz) => { FIRE.tGeo.push(geo); const m = new THREE.Mesh(geo, new THREE.MeshLambertMaterial({ color: col })); m.position.set(x, y, z); if (rz) m.rotation.z = rz; g.add(m); return m; };
  add(new THREE.BoxGeometry(9.4, 0.5, 2.3), 0x26262b, 0, 0.95, 0); add(new THREE.CylinderGeometry(1.15, 1.15, 6.6, 18), 0xd9dde2, -1.2, 2.35, 0, Math.PI / 2); add(new THREE.CylinderGeometry(1.18, 1.18, 0.9, 18), 0xff2d95, -1.2, 2.35, 0, Math.PI / 2); add(new THREE.CylinderGeometry(1.18, 1.18, 0.35, 18), 0xff2d95, -3.6, 2.35, 0, Math.PI / 2);
  add(new THREE.BoxGeometry(2.4, 2.3, 2.3), 0xc8202a, 3.4, 2.1, 0); add(new THREE.BoxGeometry(0.08, 0.9, 1.9), 0x1b2a3a, 4.62, 2.6, 0);
  const wg = new THREE.CylinderGeometry(0.55, 0.55, 0.4, 12); FIRE.tGeo.push(wg); const wm = new THREE.MeshLambertMaterial({ color: 0x111114 }); [[3.4, 1.25], [3.4, -1.25], [-0.6, 1.25], [-0.6, -1.25], [-2.8, 1.25], [-2.8, -1.25]].forEach(([x, z]) => { const w = new THREE.Mesh(wg, wm); w.rotation.x = Math.PI / 2; w.position.set(x, 0.55, z); g.add(w); });
  const x = sp.dx - 9, z = sp.dz + sp.side * 3.2; g.position.set(x, GH(x, z) + 0.02, z); g.rotation.y = Math.PI; FIRE.grp.add(g); FIRE.tank = g; FIRE.tankC = g.children[1]; } /* garée contre le trottoir, à 9 m de la porte, citerne côté porte : dans le champ de la caméra quand Mamie sort, même en portrait */
function boomSnd() { const c = SND.ctx; if (!c || !SND.on) return; const t = c.currentTime, out = c.createGain(); out.gain.value = 1; out.connect(c.destination); const s = c.createBufferSource(); s.buffer = SND.boomB || (SND.boomB = noiseBuf(2.6, q => Math.exp(-q * 3.2))); const lp = c.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.setValueAtTime(1800, t); lp.frequency.exponentialRampToValueAtTime(160, t + 1.8); s.connect(lp); lp.connect(out); s.start(t);
  const o = c.createOscillator(), g = c.createGain(); o.frequency.setValueAtTime(62, t); o.frequency.exponentialRampToValueAtTime(24, t + 1.2); g.gain.setValueAtTime(0.9, t); g.gain.exponentialRampToValueAtTime(0.0001, t + 1.4); o.connect(g); g.connect(out); o.start(t); o.stop(t + 1.5); }
function fireBoom() { const t0 = FIRE.tank; if (!t0 || FIRE.boom) return; const c = new THREE.Vector3(); (FIRE.tankC || t0).getWorldPosition(c); c.y = Math.max(c.y, GH(c.x, c.z) + 2.4); stat("feu-citerne-boum");
  const fm = new THREE.SpriteMaterial({ map: fireTex("fire"), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false }), sm = new THREE.SpriteMaterial({ map: fireTex("smoke"), transparent: true, depthWrite: false, fog: false }); const B = FIRE.boom = { t: 0, c, ball: [], smoke: [], deb: [] };
  for (let k = 0; k < 26; k++) { const q = new THREE.Sprite(fm.clone()); q.frustumCulled = false; q.position.copy(c); FIRE.grp.add(q); const a = Math.random() * 6.283, e = Math.random() * 1.2; B.ball.push({ s: q, v: new THREE.Vector3(Math.cos(a) * Math.cos(e), Math.sin(e) + 0.4, Math.sin(a) * Math.cos(e)).multiplyScalar(6 + Math.random() * 9), sz: 3 + Math.random() * 4 }); }
  for (let k = 0; k < 14; k++) { const q = new THREE.Sprite(sm.clone()); q.frustumCulled = false; q.position.copy(c); q.material.opacity = 0; FIRE.grp.add(q); B.smoke.push({ s: q, d: 0.3 + k * 0.12, ox: (Math.random() - 0.5) * 8, oz: (Math.random() - 0.5) * 8 }); }
  const rg = new THREE.RingGeometry(0.8, 1.6, 40); FIRE.tGeo.push(rg); const ring = new THREE.Mesh(rg, new THREE.MeshBasicMaterial({ color: 0xffd9a0, transparent: true, opacity: 0.9, depthWrite: false, side: THREE.DoubleSide, fog: false })); ring.rotation.x = -Math.PI / 2; ring.position.set(c.x, GH(c.x, c.z) + 0.15, c.z); FIRE.grp.add(ring); B.ring = ring;
  const dg = new THREE.BoxGeometry(0.5, 0.25, 0.7); FIRE.tGeo.push(dg); const dm = [new THREE.MeshLambertMaterial({ color: 0x2a2a2e }), new THREE.MeshLambertMaterial({ color: 0xbfc4ca })]; for (let k = 0; k < 12; k++) { const m = new THREE.Mesh(dg, dm[k % 3 ? 0 : 1]); m.position.copy(c); FIRE.grp.add(m); const a = Math.random() * 6.283; B.deb.push({ m, v: new THREE.Vector3(Math.cos(a) * (5 + Math.random() * 8), 9 + Math.random() * 9, Math.sin(a) * (5 + Math.random() * 8)), r: new THREE.Vector3(Math.random() * 9, Math.random() * 9, 0) }); }
  t0.traverse(o => { if (o.isMesh && o.material && o.material.color) o.material.color.multiplyScalar(0.16); }); for (let k = 0; k < 4; k++) { const f = new THREE.Sprite(fm.clone()); f.frustumCulled = false; f.position.set(c.x - 3 + k * 1.6, c.y + 0.4, c.z); FIRE.grp.add(f); FIRE.flames.push({ s: f, ph: Math.random() * 6 }); }
  try { shakeAdd(1.1); } catch (e) {} try { boomSnd(); } catch (e) {} try { crash(1); } catch (e) {} G.fireSir = Math.max(G.fireSir || 0, 10);
  try { const v = document.createElement("div"); v.style.cssText = "position:fixed;inset:0;z-index:37;pointer-events:none;background:radial-gradient(circle at 50% 45%,rgba(255,220,150,.7),rgba(255,90,20,.32) 55%,rgba(0,0,0,0) 80%);transition:opacity .9s ease-out"; document.body.appendChild(v); requestAnimationFrame(() => requestAnimationFrame(() => { v.style.opacity = "0"; })); setTimeout(() => v.remove(), 1100); } catch (e) {} }
function fireBoomStep(dt) { const B = FIRE.boom; B.t += dt; const t = B.t;
  B.ball.forEach(q => { if (q.dead) return; q.s.position.addScaledVector(q.v, dt); q.v.multiplyScalar(Math.max(0, 1 - dt * 2.2)); q.v.y += 2.5 * dt; q.s.scale.setScalar(q.sz * (0.4 + Math.min(1, t / 0.25) * 1.6 + t * 0.8)); q.s.material.opacity = Math.max(0, 1 - Math.max(0, t - 0.5) / 1.1); if (t > 1.7) { q.dead = 1; q.s.visible = false; } });
  B.smoke.forEach(q => { const u = t - q.d; if (u < 0) return; q.s.position.set(B.c.x + q.ox * (1 + u * 0.2), B.c.y + 2 + u * 6, B.c.z + q.oz * (1 + u * 0.2)); q.s.scale.setScalar(5 + u * 5); q.s.material.opacity = Math.max(0, Math.min(0.85, u * 1.5) * (1 - u / 9)); if (u > 9) q.s.visible = false; });
  if (B.ring && B.ring.visible) { B.ring.scale.setScalar(1 + t * 38); B.ring.material.opacity = Math.max(0, 0.9 * (1 - t / 0.9)); if (t > 0.9) B.ring.visible = false; }
  B.deb.forEach(q => { if (q.stop) return; q.v.y -= 22 * dt; q.m.position.addScaledVector(q.v, dt); q.m.rotation.x += q.r.x * dt; q.m.rotation.y += q.r.y * dt; const gy = GH(q.m.position.x, q.m.position.z) + 0.12; if (q.m.position.y < gy && q.v.y < 0) { q.m.position.y = gy; q.stop = 1; } }); }
'''
rep("function fireEnd(ok) {", FN + "function fireEnd(ok) {")
# citerne posée dès le départ de l'incendie
rep("  FIRE.win = new THREE.Vector3(sp.cx + 2.4, fy + 0.6, sp.dz - sp.side * 1.2);", "  FIRE.win = new THREE.Vector3(sp.cx + 2.4, fy + 0.6, sp.dz - sp.side * 1.2); try { fireTank(sp); } catch (e) {} /* V310.109 : la citerne de gaz garée devant */")
# boum quand Mamie sort
rep("fireSmokeVeil(0.6); fireBurst(); setTimeout(() => fireSmokeVeil(0), 500); setTimeout(() => fireEnd(true), 1300); }, 650); }",
    "fireSmokeVeil(0.6); fireBurst(); setTimeout(() => fireSmokeVeil(0), 500); setTimeout(() => { try { fireBoom(); } catch (e) {} }, 1100); setTimeout(() => fireEnd(true), 2300); }, 650); } /* V310.109 : la citerne saute 1,1 s après la sortie de Mamie, le message de sauvetage vient après */")
# animation
rep("  if (FIRE.parts) FIRE.parts.forEach(q => {", "  if (FIRE.boom) try { fireBoomStep(dt); } catch (e) {}\n  if (FIRE.parts) FIRE.parts.forEach(q => {")
# nettoyage (géométries propres à la citerne)
rep("if (FIRE.truck) { scene.remove(FIRE.truck); FIRE.truck = null; } FIRE.on = false; return; } }",
    "if (FIRE.truck) { scene.remove(FIRE.truck); FIRE.truck = null; } (FIRE.tGeo || []).forEach(g => { try { g.dispose(); } catch (e) {} }); FIRE.tGeo = null; FIRE.tank = null; FIRE.boom = null; FIRE.on = false; return; } }")
# message de fin : la citerne
rep('help(`<b>Mamie Josette est sauvée.</b> « C\'est toi qui passes tous les matins ! » <b style="color:var(--cash)">+$1 500</b>`, 7);',
    'help(FIRE.boom ? `<b>Mamie Josette est sauvée.</b> La citerne a sauté juste derrière vous. Personne n\'est blessé. <b style="color:var(--cash);white-space:nowrap">+$1 500</b>` : `<b>Mamie Josette est sauvée.</b> « C\'est toi qui passes tous les matins ! » <b style="color:var(--cash)">+$1 500</b>`, 7);')
open(p, "w", encoding="utf-8").write(s)
import json
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
d.update({"La citerne a sauté juste derrière vous. Personne n'est blessé.": "The gas tanker blew up right behind you. Nobody got hurt.", "Mamie Josette est sauvée.": d.get("Mamie Josette est sauvée.", "Grandma Josette is safe.")})
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271830';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
