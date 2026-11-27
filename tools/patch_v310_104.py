# V310.104 · LE REX S'ÉCHAPPE (commande de Thomas du 26/11 20h54, cahier des charges de l'expert, file du 27/11 8h07 tâche 4)
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
CODE = r'''/* V310.104 · « LE REX S'ÉCHAPPE » (commande de Thomas du 26/11 20h54, cahier des charges de l'expert, file du 27/11 8h07 tâche 4) : à partir du Jour 2, une fois par jour réel, quand le joueur roule à moins de 1 500 m du parc · le Rex du parc (le même modèle, rien de chargé en plus) sort par le portail · 1. rejoindre le camion des gardiens (l'appât) · 2. passer devant le Rex et le ramener au portail en restant à 20-75 m devant lui (il marche exactement sur le chemin de la voiture, donc jamais à travers un immeuble) · 3. il rentre, applaudissements, +2 000 $, badge « Dompteur » · trop loin : il s'arrête et rugit, jamais de punition · personne n'est blessé · stat rex-alerte, rex-camion, rex-fini, rex-abandon */
const REXE = { on: false, chk: 0 };
function rexEscEligible() { return P && !CREATOR && G.mode === "play" && !G.onFoot && !G.inside && !G.mission && !G.race && !FIRE.on && !(typeof TX !== "undefined" && TX.on) && !CINE.on && (P.day || 1) >= 2 && !(P.rexE && P.rexE.d === todayStr()) && REX.d && REX.d.g && JUNGLE.gate && !REXE.on; }
function rexRoar(v) { try { jungleSound("roar", v); } catch (e) {} try { navigator.vibrate && navigator.vibrate([40, 30, 80]); } catch (e) {} }
function rexGauge(dp) { let b = document.getElementById("rexGauge"); if (dp == null) { if (b) b.remove(); return; } if (!b) { b = document.createElement("div"); b.id = "rexGauge"; b.style.cssText = "position:fixed;left:50%;top:calc(64px + env(safe-area-inset-top));transform:translateX(-50%);z-index:41;padding:7px 14px;border-radius:999px;background:rgba(12,6,24,.85);color:#fff;font:700 13px Inter,system-ui,sans-serif;border:1px solid rgba(255,255,255,.18);pointer-events:none"; document.body.appendChild(b); } const ok = dp >= 15 && dp <= 75; b.style.borderColor = ok ? "#3fd16b" : "#ff2d55"; b.innerHTML = `🦖 Distance du Rex · <b style="color:${ok ? "#3fd16b" : "#ff6b8a"}">${Math.round(dp)} m</b>`; }
function rexEscStart() { const d = REX.d, [gx, gz] = JUNGLE.gate, [cx, cz] = REX.c; let ux = gx - cx, uz = gz - cz; const L = Math.hypot(ux, uz) || 1; ux /= L; uz /= L;
  const rx = gx + ux * 130, rz = gz + uz * 130, tx = gx + ux * 55 + uz * 16, tz = gz + uz * 55 - ux * 16; if (isWater(rx, rz) || isWater(tx, tz)) return false;
  REXE.on = true; REXE.st = "camion"; REXE.t = 0; REXE.gate = [gx, gz]; REXE.dir = [ux, uz]; REXE.trail = []; REXE.far = 0; REXE.lost = 0; REXE.warn = -99; REXE.d = d; REXE.tx = tx; REXE.tz = tz;
  P.rexE = { d: todayStr() }; saveNow(); d.esc = true; d.g.visible = true; d.g.position.set(rx, GH(rx, rz) - 0.15, rz); d.g.rotation.y = Math.atan2(ux, uz);
  try { const m = makeCar({ id: "trafic", color: 0x2f8f4f }, { model: MODELS.firetruck3 ? "firetruck3" : "firetruck" }); if (m) { m.position.set(tx, GH(tx, tz) + 0.02, tz); m.rotation.y = Math.atan2(-ux, -uz); scene.add(m); REXE.truck = m; } } catch (e) {}
  destBeacon.position.set(tx, 0, tz); destBeacon.visible = true; stat("rex-alerte"); rexRoar(0.9); try { sfx.ping(); } catch (e) {}
  const o = G.car; help(`<b>Alerte radio :</b> « Le Rex est sorti de la ZONE 0 ! » Va au camion des gardiens, à ${Math.round(Math.hypot(tx - o.x, tz - o.z) / 10) * 10} m, pour prendre l'appât.`, 8); return true; }
function rexEscEnd(ok) { const d = REXE.d; REXE.on = false; REXE.st = "fin"; destBeacon.visible = false; rexGauge(null); if (REXE.truck) { scene.remove(REXE.truck); REXE.truck = null; }
  if (ok) { stat("rex-fini"); addCash(2000); try { addXP(200); } catch (e) {} try { sfx.win(); } catch (e) {} P.badges = P.badges || {}; if (!P.badges.dompteur) { P.badges.dompteur = 1; setTimeout(() => notify("gold", "<b>Badge · Dompteur</b>", 7), 1800); }
    try { const c = SND.ctx; if (c) for (let k = 0; k < 6; k++) stadeClap(c, c.currentTime + k * 0.12, 0.45); } catch (e) {}
    help(`<b>Le Rex est rentré.</b> Le portail se referme. Les gardiens applaudissent. <b style="color:var(--cash)">+$2 000</b>`, 7); try { feedPost("parc", "Le Rex est sorti du parc ce soir. Un livreur l'a ramené tout seul. Respect. 🦖", { toast: true }); } catch (e) {}
    REXE.home = 6; saveNow(); return; }
  stat("rex-abandon"); help("Les gardiens l'ont endormi et ramené. Personne n'est blessé.", 5); if (d) d.esc = false; }
function updateRexEsc(dt) {
  if (REXE.home > 0) { const d = REXE.d, p = d.g.position, [cx, cz] = REX.c, dx = cx - p.x, dz = cz - p.z, L = Math.hypot(dx, dz); REXE.home -= dt; if (L > 3) { const st = Math.min(L, 7 * dt); p.x += dx / L * st; p.z += dz / L * st; p.y = GH(p.x, p.z) - 0.15; d.g.rotation.y = Math.atan2(dx, dz); if (d.pw) rexStep(d, dt); } if (REXE.home <= 0) d.esc = false; return; }
  if (!REXE.on) { REXE.chk += dt; if (REXE.chk > 2) { REXE.chk = 0; try { if (rexEscEligible()) { const [gx, gz] = JUNGLE.gate, o = G.car; if (Math.hypot(o.x - gx, o.z - gz) < 1500) rexEscStart(); } } catch (e) { console.warn("rex", e); } } return; }
  const d = REXE.d, o = G.onFoot ? G.me : G.car, p = d.g.position; REXE.t += dt; d.g.visible = true; const dp = Math.hypot(o.x - p.x, o.z - p.z);
  if (REXE.st === "camion") { REXE.idle = (REXE.idle || 0) + dt; if (REXE.idle > 9) { REXE.idle = 0; if (dp < 400) rexRoar(Math.max(0.15, 1 - dp / 400)); }
    if (Math.hypot(o.x - REXE.tx, o.z - REXE.tz) < 13) { REXE.st = "guide"; stat("rex-camion"); destBeacon.position.set(REXE.gate[0], 0, REXE.gate[1]); try { sfx.ping(); } catch (e) {} help("<b>Appât chargé.</b> Passe devant le Rex et ramène-le au portail du parc. Reste entre 20 et 75 m devant lui.", 8); }
    if (dp > 2500) { REXE.lost += dt; if (REXE.lost > 60) rexEscEnd(false); } else REXE.lost = 0; return; }
  if (REXE.st !== "guide") return;
  const tr = REXE.trail; if (dp < 75) { const last = tr[tr.length - 1]; if (!last || Math.hypot(o.x - last[0], o.z - last[1]) > 2.5) tr.push([o.x, o.z]); }
  if (dp > 75) { REXE.far += dt; if (REXE.far > 1.2 && REXE.t - REXE.warn > 8) { REXE.warn = REXE.t; rexRoar(0.8); help("Le Rex s'arrête et rugit. <b>Reviens devant lui.</b>", 4); } } else REXE.far = 0;
  if (dp > 16 && dp <= 75 && tr.length) { let spd = Math.min(14, 5 + (dp - 16) * 0.22) * dt, moved = false;
    while (spd > 0 && tr.length) { const [ax, az] = tr[0], dx = ax - p.x, dz = az - p.z, L = Math.hypot(dx, dz); if (L <= spd) { p.x = ax; p.z = az; spd -= L; tr.shift(); } else { p.x += dx / L * spd; p.z += dz / L * spd; spd = 0; const ta = Math.atan2(dx, dz); let da = ta - d.g.rotation.y; da = Math.atan2(Math.sin(da), Math.cos(da)); d.g.rotation.y += da * Math.min(1, dt * 4); } moved = true; }
    if (moved) { p.y = GH(p.x, p.z) - 0.15; if (d.pw) rexStep(d, dt); d.stp = (d.stp || 0) + dt * 1.25; if (d.stp > 1) { d.stp = 0; try { giantStep(dp, true); } catch (e) {} } } }
  if (G.onFoot) { const me = G.me, R2 = d.g.scale.x * 4.2, dd = Math.hypot(me.x - p.x, me.z - p.z); if (dd < R2 && dd > 0.01) { me.x = p.x + (me.x - p.x) / dd * R2; me.z = p.z + (me.z - p.z) / dd * R2; } }
  rexGauge(dp); if (Math.hypot(p.x - REXE.gate[0], p.z - REXE.gate[1]) < 24) rexEscEnd(true);
  else if (dp > 600) { REXE.lost += dt; if (REXE.lost > 45) rexEscEnd(false); } else REXE.lost = 0; }
'''
rep('const FIRE = { on: false };', CODE + 'const FIRE = { on: false };')
rep('try { updateFire(dt); } catch (e) { console.warn("feu", e); }', 'try { updateFire(dt); } catch (e) { console.warn("feu", e); } try { updateRexEsc(dt); } catch (e) { console.warn("rex", e); }')
rep('JUNGLE.dinos.forEach(d => { d.g.visible = near; if (!near) return;', 'JUNGLE.dinos.forEach(d => { if (d.esc) return; d.g.visible = near; if (!near) return;')
rep('function freeOffer() {', 'function freeOffer() { if (REXE.on) return null;')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271830';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
