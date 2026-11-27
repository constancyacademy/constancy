// V310.127 · pont de la voie rapide du Mont : la voiture lancée à 22 m/s contre le parapet (12°, 35°, 70°, et en entrant en biais au début du pont) doit glisser et repartir, jamais passer par-dessus (maxX ≤ 6,4) ni rester arrêtée · node tests/pont_mont.js page.html save.json
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
 const b = await chromium.launch({ args: ['--allow-file-access-from-files','--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--mute-audio'] });
 const ctx = await b.newContext({ viewport: { width: 800, height: 500 } }); await ctx.route(/^https?:/, r => r.abort());
 await ctx.addInitScript(s => { try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
 const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
 await p.goto('file://' + page + '?nostat=1&autostart=1&portail=itch');
 for (let k = 0; k < 260; k++) { await p.waitForTimeout(1000); const m = await p.evaluate(() => { try { for (const id of ['cont','wgo','gNext','chestGo']) { const e = document.getElementById(id); if (e && e.getClientRects().length) e.click(); } const g = document.getElementById('guide'); if (g) g.remove(); const T = window.__T(); if (T.G.mode === 'guide') T.G.mode = 'play'; return T.G.mode + '|' + !!window.__zonesPretes + '|' + T.DK.ready; } catch (e) { return 'x ' + e.message; } }); if (/^play\|true\|true/.test(m) && k > 8) break; }
 await p.waitForTimeout(3000);
 const res = [];
 await p.evaluate(() => { window.__loopStop = true; });
 for (const [z0, ang] of [[-450, 12], [-450, 35], [-450, 70], [-404, 35], [-404, 60]]) {
  const r = await p.evaluate(([z0, ang]) => { const T = window.__T(), G = T.G; if (G.onFoot) { try { T.toggleCar(); } catch (e) {} } G.mission = null;
   const c = G.car, A = ang * Math.PI / 180; c.x = 3.5; c.z = z0; c.jy = null; c.h = Math.PI - A; c.v = 22; c.s = 0; c._lx = c.x; c._lz = c.z; c.air = 0;
   window.__auto = () => ({ fwd: 1, side: 0, brake: false });
   const out = []; let minY = 99, maxX = 0;
   for (let f = 1; f <= 90; f++) { T.updateCar(1 / 30); maxX = Math.max(maxX, Math.abs(c.x)); minY = Math.min(minY, T.GH(c.x, c.z)); if (f === 10 || f === 30 || f === 90) { const dh = Math.abs(((c.h - Math.PI + Math.PI * 3) % (Math.PI * 2)) - Math.PI); out.push({ s: +(f / 30).toFixed(2), v: +c.v.toFixed(1), x: +c.x.toFixed(2), z: +c.z.toFixed(0), cap: +(dh * 180 / Math.PI).toFixed(0) }); } }
   window.__auto = null; return { out, maxX: +maxX.toFixed(2), minSol: +minY.toFixed(1) }; }, [z0, ang]);
  res.push({ z0, ang, ...r });
 }
 console.log(JSON.stringify(res)); console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })();
