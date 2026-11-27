# V310.115 · « L'ÉRUPTION » (idée de Thomas du 25/11, point 20 : « volcan derrière le parc des dinos qui explose ») · sans violence
# Jour 2 et plus, une fois par jour, à moins de 1 600 m de l'île-volcan, quand rien ne se passe : le volcan se réveille (grondements, écran qui tremble selon la distance), fontaine de lave, colonne de cendres, bombes de lave qui retombent dans la mer avec un panache de vapeur, lueur du cratère qui pulse · mission : le prendre en photo (bouton 📷) pendant les 90 s · +1 500 $, badge Reporter du volcan
# ?volcan=1 la déclenche 6 s après l'entrée en jeu, quelle que soit la distance (pour filmer) · stats volcan-eveil, volcan-photo, volcan-fin
import re, sys, json
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
CODE = r'''/* V310.115 · « L'ÉRUPTION » (Thomas, 25/11 : « volcan derrière le parc des dinos qui explose ») : l'île-volcan se réveille, fontaine de lave, cendres, bombes de lave dans la mer · mission photo · formes simples, aucune lumière ajoutée */
const VOL = { on: false };
function volEligible() { const v = SAVANE.volc; if (!v || !P || CREATOR || G.mode !== "play" || G.inside || G.mission || G.race || FIRE.on || REXE.on || CY.on || CINE.on || (typeof TX !== "undefined" && TX.on) || (P.day || 1) < 2 || (P.volE && P.volE.d === todayStr())) return false; const o = G.onFoot ? G.me : G.car; return Math.hypot(o.x - v.x, o.z - v.z) < 1600; }
function volStart(force) { const v = SAVANE.volc; if (!v || (!force && !volEligible())) return false; VOL.on = true; VOL.t = 0; VOL.ok = false; VOL.nxt = 2; P.volE = { d: todayStr() }; saveNow(); stat("volcan-eveil");
  const top = 230 * 0.646 - 9, grp = new THREE.Group(); grp.name = "eruption"; grp.position.set(v.x, 0, v.z); scene.add(grp); VOL.grp = grp; VOL.top = top - 6; VOL.mats = []; VOL.maps = [fireTex("fire"), fireTex("smoke")];
  const mk = (i, add, col) => { const m = new THREE.SpriteMaterial({ map: VOL.maps[i], transparent: true, depthWrite: false, fog: false, blending: add ? THREE.AdditiveBlending : THREE.NormalBlending, color: col }); VOL.mats.push(m); const q = new THREE.Sprite(m); q.frustumCulled = false; q.visible = false; grp.add(q); return q; };
  VOL.lava = []; for (let k = 0; k < 30; k++) VOL.lava.push({ s: mk(0, true, 0xffffff), life: 0 });
  VOL.ash = []; for (let k = 0; k < 18; k++) VOL.ash.push({ s: mk(1, false, 0x3a3634), u: k / 18, ox: (Math.random() - 0.5) * 40, oz: (Math.random() - 0.5) * 40 });
  VOL.bomb = []; for (let k = 0; k < 10; k++) VOL.bomb.push({ s: mk(0, true, 0xffb060), st: mk(1, false, 0xdddddd), life: 0, sl: 0 });
  VOL.dur = 90; const o = G.onFoot ? G.me : G.car, d = Math.round(Math.hypot(o.x - v.x, o.z - v.z) / 10) * 10; try { boomSnd(); } catch (e) {} try { shakeAdd(Math.max(0.15, 0.7 - d / 2600)); } catch (e) {}
  help(`<b>Le volcan se réveille !</b> L'île, à ${d} m. Prends l'éruption en photo (bouton 📷) avant qu'elle se calme.`, 9); return true; }
function volLaunch(q, fast) { q.life = 1.6 + Math.random() * 1.6; const a = Math.random() * 6.283, h = fast ? 0.5 : 0.25; q.p = new THREE.Vector3(Math.cos(a) * 4, VOL.top, Math.sin(a) * 4); q.v = new THREE.Vector3(Math.cos(a) * (6 + Math.random() * 10) * h * 2, 45 + Math.random() * 40, Math.sin(a) * (6 + Math.random() * 10) * h * 2); q.s.visible = true; }
function volEnd(ok) { VOL.fin = 8; if (ok) return; stat("volcan-fin"); help("Le volcan se rendort. Il reviendra.", 4); }
function volClean() { VOL.on = false; if (VOL.grp) scene.remove(VOL.grp); VOL.grp = null; (VOL.mats || []).forEach(m => { try { m.dispose(); } catch (e) {} }); (VOL.maps || []).forEach(t => { try { t.dispose(); } catch (e) {} }); VOL.mats = VOL.maps = null; VOL.fin = null; try { const v = SAVANE.volc; if (v && v.sp) v.sp.scale.set(90, 90, 1); } catch (e) {} }
function volPhoto() { try { if (!VOL.on || VOL.ok || VOL.fin != null) return; const v = SAVANE.volc, q = new THREE.Vector3(v.x, VOL.top + 30, v.z).project(camera); if (Math.abs(q.x) > 0.95 || Math.abs(q.y) > 0.95 || q.z > 1) { help("Le volcan n'est pas dans la photo. Tourne la vue vers l'île.", 3); return; } VOL.ok = true; stat("volcan-photo"); addCash(1500); try { addXP(150); } catch (e) {} P.badges = P.badges || {}; if (!P.badges.volcan) { P.badges.volcan = 1; setTimeout(() => notify("gold", "<b>Badge · Reporter du volcan</b>", 7), 1800); } setTimeout(() => { try { help(`<b>La photo de l'année.</b> L'éruption dans la boîte. <b style="color:var(--cash);white-space:nowrap">+$1 500</b>`, 6); feedPost("ville", "Quelqu'un a pris le volcan en pleine éruption. Cette photo tourne partout. 🌋", { toast: true }); } catch (e) {} }, 900); saveNow(); } catch (e) {} }
function updateVolcano(dt) { if (!VOL.on) { if (VOL.q == null) VOL.q = /[?&]volcan=1/.test(location.search); if (VOL.q && !VOL.forced && G.mode === "play" && G.playT0 && performance.now() - G.playT0 > 6000 && SAVANE.volc) { G.mission = null; if (volStart(true)) VOL.forced = 1; } return; }
  VOL.t += dt; const T = performance.now() / 1000, v = SAVANE.volc, o = G.onFoot ? G.me : G.car, D = Math.hypot(o.x - v.x, o.z - v.z); let k = 1; if (VOL.fin != null) { VOL.fin -= dt; k = Math.max(0, VOL.fin / 8); if (VOL.fin <= 0) { volClean(); return; } } else if (VOL.t > VOL.dur) volEnd(VOL.ok);
  try { if (v.sp) { const pl = 1 + 0.35 * Math.sin(T * 7) + 0.2 * Math.sin(T * 13); v.sp.scale.setScalar(90 + 110 * k * pl); } } catch (e) {}
  VOL.nxt -= dt; if (VOL.nxt <= 0 && k > 0.5) { VOL.nxt = 6 + Math.random() * 5; try { boomSnd(); } catch (e) {} try { shakeAdd(Math.max(0.08, 0.55 - D / 3000)); } catch (e) {} }
  VOL.lava.forEach(q => { if (q.life <= 0) { if (k > 0.3) volLaunch(q, false); else { q.s.visible = false; return; } } q.life -= dt; q.v.y -= 30 * dt; q.p.addScaledVector(q.v, dt); q.s.position.copy(q.p); q.s.scale.setScalar(9 + (1.6 - Math.min(1.6, q.life)) * 6); q.s.material.opacity = Math.min(1, q.life) * k; });
  VOL.ash.forEach(q => { const u = (q.u + VOL.t * 0.035) % 1; q.s.visible = true; q.s.position.set(q.ox * (1 + u * 4) + Math.sin(T * 0.2 + q.u * 9) * 20 * u, VOL.top + 10 + u * 380, q.oz * (1 + u * 4)); q.s.scale.setScalar(40 + u * 160); q.s.material.opacity = 0.8 * (1 - u) * Math.min(1, VOL.t / 3) * k; });
  VOL.bomb.forEach(q => { if (q.life <= 0 && q.sl <= 0) { if (k > 0.5 && Math.random() < dt * 0.8) { volLaunch(q, true); q.v.x *= 3.2; q.v.z *= 3.2; q.v.y *= 1.15; q.life = 9; } else { q.s.visible = false; q.st.visible = false; return; } }
    if (q.life > 0) { q.life -= dt; q.v.y -= 30 * dt; q.p.addScaledVector(q.v, dt); q.s.position.copy(q.p); q.s.scale.setScalar(7); q.s.material.opacity = k; if (q.p.y < 0) { q.life = 0; q.s.visible = false; q.sl = 2.5; q.st.visible = true; q.st.position.set(q.p.x, 4, q.p.z); } }
    if (q.sl > 0) { q.sl -= dt; const u = 1 - q.sl / 2.5; q.st.position.y = 4 + u * 25; q.st.scale.setScalar(12 + u * 30); q.st.material.opacity = 0.7 * (1 - u) * k; if (q.sl <= 0) q.st.visible = false; } }); }
'''
rep("const FIRE = { on: false };", CODE + "const FIRE = { on: false };")
rep('try { updateCyclone(dt); } catch (e) { console.warn("cyclone", e); }', 'try { updateCyclone(dt); } catch (e) { console.warn("cyclone", e); } try { updateVolcano(dt); } catch (e) { console.warn("volcan", e); }')
rep('try { if (cyEligible()) { cyStart(); if (CY.on) return "cyclone"; } } catch (e) {}', 'try { if (cyEligible()) { cyStart(); if (CY.on) return "cyclone"; } } catch (e) {} try { if (volEligible()) { volStart(); if (VOL.on) return "volcan"; } } catch (e) {} /* V310.115 : l\'éruption du jour près de l\'île-volcan */')
rep('function freeOffer() { if (REXE.on || CY.on) return null;', 'function freeOffer() { if (REXE.on || CY.on || VOL.on) return null;')
rep('sfx.ping(); stat("photo-prise");', 'sfx.ping(); stat("photo-prise"); try { volPhoto(); } catch (e) {}')
open(p, "w", encoding="utf-8").write(s)
j = "assets/i18n/en.json"; d = json.load(open(j, encoding="utf-8"))
d.update({"Le volcan se réveille !": "The volcano is waking up!", "L'île, à # m. Prends l'éruption en photo (bouton 📷) avant qu'elle se calme.": "The island, # m away. Take a photo of the eruption (📷 button) before it calms down.", "Le volcan se rendort. Il reviendra.": "The volcano goes back to sleep. It will be back.",
 "Le volcan n'est pas dans la photo. Tourne la vue vers l'île.": "The volcano isn't in the photo. Turn the view toward the island.", "Badge · Reporter du volcan": "Badge · Volcano Reporter", "La photo de l'année.": "Photo of the year.", "L'éruption dans la boîte.": "The eruption, captured.", "Quelqu'un a pris le volcan en pleine éruption. Cette photo tourne partout. 🌋": "Someone caught the volcano mid-eruption. This photo is everywhere. 🌋"})
json.dump(d, open(j, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271915';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
