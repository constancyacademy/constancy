const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { window.__farDebug = 1; Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); const PP = T.P; if (PP) PP.nightStart = false; W.creatorSetHour(14); });
  for (let k = 0; k < 200; k++) { const r = await p.evaluate(() => !!(window.__zonesPretes)); if (r) break; await p.waitForTimeout(1000); }
  const R = await p.evaluate(async () => { const W = window.__W(), T = window.__T(), G = W.G, P = W.P, wait = ms => new Promise(ok => setTimeout(ok, ms)); const out = {};
    if (!G.onFoot) { try { G.wantExit = true; } catch (e) {} for (let i = 0; i < 20 && !G.onFoot; i++) await wait(300); }
    out.aPied = !!G.onFoot; out.gare = !!G.parked; if (!G.parked) return out;
    G.me.x = G.parked.x + 70; G.me.z = G.parked.z; await wait(400);
    T.phoneShop(); await wait(300); const bt = document.querySelector('[data-deliver="' + P.car + '"]'); out.bouton = !!bt; const d0 = Math.hypot(G.parked.x - G.me.x, G.parked.z - G.me.z);
    if (bt) { bt.click(); await wait(500); } out.avant = Math.round(d0); out.apres = +Math.hypot(G.parked.x - G.me.x, G.parked.z - G.me.z).toFixed(1); out.mesh = !!(G.parked.mesh && G.parked.mesh.parent); out.meshPos = G.parked.mesh ? +Math.hypot(G.parked.mesh.position.x - G.me.x, G.parked.mesh.position.z - G.me.z).toFixed(1) : null;
    G.me.x = G.parked.x + 5; await wait(200); T.phoneShop(); await wait(300); out.boutonPres = !!document.querySelector('[data-deliver="' + P.car + '"]'); try { W.resume && W.resume(); } catch (e) {}
    return out; });
  console.log(JSON.stringify(R)); await p.screenshot({ path: out + '/apres.png' }); await b.close(); })();
