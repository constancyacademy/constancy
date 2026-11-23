// Bretelle du Mall : du sol (20, 1150) on roule plein sud, la voiture doit monter à 8 m et finir sur le Périphérique, puis tourner à l'est et rouler dessus
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 700, height: 700 } }); await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 200; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } W.creatorSetHour(14); });
  await p.waitForTimeout(2000);
  await p.evaluate(() => { const G = window.__W().G, c = G.car; c.x = 20; c.z = 1140; c.h = 0; c.v = 0; c.jy = null; c._lx = c.x; c._lz = c.z; window.__norender = 1; window.__auto = () => ({ fwd: 0.7, side: 0, brake: false }); window.__log = []; window.__li = setInterval(() => window.__log.push([Math.round(c.x), Math.round(c.z), +(c.jy || 0).toFixed(1), +(c.v || 0).toFixed(1)]), 400); });
  await p.waitForFunction(() => window.__log.length >= 30, null, { timeout: 600000 });
  await p.evaluate(() => { const G = window.__W().G, c = G.car; window.__auto = () => ({ fwd: 0.7, side: c.z > 1296 && Math.abs(Math.sin(c.h)) < 0.95 ? -1 : 0, brake: false }); });
  await p.waitForFunction(() => window.__log.length >= 50, null, { timeout: 600000 });
  const log = await p.evaluate(() => { clearInterval(window.__li); return window.__log; });
  console.log(log.map(q => q.join(',')).join(' | '));
  const W = log[log.length - 1]; console.log('FIN', JSON.stringify(W), W[2] > 6 ? 'OK sur le Périphérique' : 'ÉCHEC');
  await p.evaluate(() => { window.__norender = 0; const c = window.__W().G.car; window.__camK = () => ({ p: [c.x - 30, (c.jy || 0) + 14, c.z - 30], t: [c.x, c.jy || 0, c.z], fov: 55 }); }); await p.waitForTimeout(4000); await p.screenshot({ path: '/tmp/pc/rampe.png', timeout: 240000 });
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
