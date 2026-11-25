const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { window.__farDebug = 1; Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); const PP = T.P; if (PP) PP.nightStart = false; W.creatorSetHour(14); });
  for (let k = 0; k < 200; k++) { const r = await p.evaluate(() => !!(window.__zonesPretes && window.__FARW && window.__FARW.ready)); if (r) break; await p.waitForTimeout(1000); }
  const shotP = (async () => { for (let k = 0; k < 200; k++) { await p.waitForTimeout(300); if (await p.evaluate(() => window.__shotNow === 1).catch(() => false)) { await p.screenshot({ path: out + '/ld_carte.png' }); break; } } })();
  const R = await p.evaluate(async () => { const T = window.__T(), W = window.__W(), X = window.__X(), G = W.G, P = T.P; const out = {};
    if (G.onFoot && G.parked) { try { T.finishEnter({ own: true }); } catch (e) {} await new Promise(ok => setTimeout(ok, 600)); }
    G.mission = null; P.deliveries = Math.max(1, P.deliveries || 0); P.ld = null; out.ok = T.ldOk();
    // le joueur au milieu d'une avenue, cap vers l'intérieur de la ville, une voiture de la circulation à côté
    const c = G.car; c.x = -HALF_X(); function HALF_X() { return 400 - 8 - 56 * 2; } c.z = -400 + 8 + 56 * 3; c.h = Math.PI / 2; c.v = 0; c.jy = null; G.snapCam = true;
    const a = X.traffic.find(q => q.mesh.visible && !q.frozen && !(q.mesh.userData && q.mesh.userData.patrol)); if (!a) return { err: 'pas de voiture' }; a.x = c.x + Math.sin(c.h + Math.PI / 2) * 3.4; a.z = c.z + Math.cos(c.h + Math.PI / 2) * 3.4; a.h = c.h; a.speed = 0; a.vEff = 0;
    T.ldCard(a); window.__shotNow = 1; await new Promise(ok => setTimeout(ok, 2500)); out.carte = !!document.getElementById('ldCard'); window.__shotNow = 1; out.texte = (document.getElementById('ldCard') || {}).textContent;
    document.getElementById('ldGo').click(); out.course = !!G.race; await new Promise(ok => setTimeout(ok, 1200)); out.compte = (document.getElementById('ldCd') || {}).textContent;
    const R0 = G.race; out.dist = R0 ? Math.round(Math.hypot(R0.x - c.x, R0.z - c.z)) : null; out.vRival = R0 ? R0.vR : null;
    window.__auto = () => ({ fwd: 1, side: 0, brake: false }); window.__shotNow = 0; const t0 = performance.now(); while (G.race && performance.now() - t0 < 1000) { await new Promise(ok => setTimeout(ok, 200)); }
    window.__auto = null; out.fin = { cash: P.cash, ld: P.ld, help: (document.getElementById('help') || {}).textContent }; out.stats = (window.__stats || []).filter(x => /course-ligne/.test(x)); return out; });
  console.log(JSON.stringify(R, null, 1)); await p.screenshot({ path: out + '/ld_fin.png' }); await b.close(); })();
