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
  const shotP = (async () => { for (let k = 0; k < 300; k++) { await p.waitForTimeout(300); if (await p.evaluate(() => window.__shotNow === 1).catch(() => false)) { await p.screenshot({ path: out + '/taxi.png' }); break; } } })();
  const R = await p.evaluate(async () => { const T = window.__T(), W = window.__W(), G = W.G, P = T.P; const out = {}; const wait = ms => new Promise(ok => setTimeout(ok, ms));
    if (G.onFoot && G.parked) { try { T.finishEnter({ own: true }); } catch (e) {} await wait(800); }
    // 1) en voiture, incendie déjà fait aujourd'hui → taxi attendu
    G.mission = null; P.tx = null; P.day = Math.max(2, P.day || 1); P.fire = { day: P.day }; G.freeT = 44.8; for (let i = 0; i < 40 && !T.TX.on && !T.FIRE.on; i++) await wait(250);
    out.voiture = { taxi: T.TX.on, feu: T.FIRE.on, stats: (window.__stats || []).filter(x => /rien-a-faire|interaction/.test(x)) };
    // 2) même chose, incendie possible → feu attendu en premier
    if (T.TX.on) { T.TX.t = 0.01; await wait(1500); } P.fire = null; G.mission = null; G.freeT = 44.8; for (let i = 0; i < 40 && !T.FIRE.on; i++) await wait(250);
    out.feu = { feu: T.FIRE.on, taxi: T.TX.on, stats: (window.__stats || []).filter(x => /rien-a-faire|interaction|feu-vu|taxi-vu/.test(x)) };
    if (T.FIRE.on) { T.FIRE.fade = 0.05; for (let i = 0; i < 40 && T.FIRE.on; i++) await wait(250); } out.feuFini = !T.FIRE.on; try { W.toggleCar(); } catch (e) { out.errSortie = e.message; } await wait(1500); out.aPied = G.onFoot; G.mission = null; P.fire = { day: P.day }; G.freeT = 44.8; for (let i = 0; i < 40 && !(G.mission && G.mission.type === 'voisin'); i++) await wait(250); out.chk = { aPied: G.onFoot, started: G.started, story: T.storyStep ? !!T.storyStep() : 'nc', inside: G.inside, mode: G.mode, voisT: G.voisT, feuFini: out.feuFini }; out.pied = { mission: G.mission && G.mission.type, stats: (window.__stats || []).filter(x => /interaction|rien-a-faire/.test(x)) };
    return out; });
  console.log(JSON.stringify(R, null, 1)); await b.close(); })();
