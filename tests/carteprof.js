// Carte 3D : à-coups (images longues) et fonctions chères pendant : zoom au plus près, glisser dézoomé, fermeture · node tools/carteprof.js page save
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); });
  for (let k = 0; k < 150; k++) { const d = await p.evaluate(() => window.__T().DEFER.done); if (d) break; await p.waitForTimeout(2000); }
  await p.waitForTimeout(3000);
  await p.evaluate(() => { window.__fr = []; let l = performance.now(); const f = () => { const n = performance.now(); window.__fr.push(n - l); l = n; requestAnimationFrame(f); }; requestAnimationFrame(f); });
  const cdp = await ctx.newCDPSession(p); await cdp.send('Profiler.enable'); await cdp.send('Profiler.setSamplingInterval', { interval: 500 });
  const phase = async (name, fn, ms) => { await p.evaluate(() => { window.__fr.length = 0; }); await cdp.send('Profiler.start'); await p.evaluate(fn); await p.waitForTimeout(ms); const { profile } = await cdp.send('Profiler.stop'); const fr = await p.evaluate(() => window.__fr.slice());
    const self = {}; const dt = profile.timeDeltas || []; const byId = new Map(profile.nodes.map(n => [n.id, n])); (profile.samples || []).forEach((id, i) => { const n = byId.get(id); const k = (n.callFrame.functionName || '(anon)') + ':' + n.callFrame.lineNumber; self[k] = (self[k] || 0) + (dt[i] || 0) / 1000; });
    const top = Object.entries(self).filter(([k]) => !/^\((idle|program|garbage)/.test(k)).sort((a, b) => b[1] - a[1]).slice(0, 8).map(([k, v]) => k + ' ' + v.toFixed(0) + 'ms').join(' · ');
    const s = fr.slice().sort((a, b) => a - b), med = s[Math.floor(s.length / 2)] || 0, long = fr.filter(x => x > Math.max(3 * med, 120)).length;
    console.log(`${name} : ${fr.length} images, médiane ${med.toFixed(0)} ms, pire ${Math.max(...fr).toFixed(0)} ms, à-coups ${long} · ${top}`); };
  await phase('ouverture', () => window.__T().openMap3D(), 4000);
  await phase('zoom au plus près', () => { const M3 = window.__T().M3; M3.dW = 40; }, 4000);
  await phase('glisser au plus près', () => { const M3 = window.__T().M3; let i = 0; const iv = setInterval(() => { M3.tx = M3.x + 40; M3.tz = M3.z + 10; if (++i > 30) clearInterval(iv); }, 100); }, 4000);
  await phase('dézoom', () => { const M3 = window.__T().M3; M3.dW = 2600; }, 4000);
  await phase('glisser dézoomé', () => { const M3 = window.__T().M3; let i = 0; const iv = setInterval(() => { M3.tx = M3.x - 120; M3.tz = M3.z - 60; if (++i > 30) clearInterval(iv); }, 100); }, 4000);
  await phase('fermeture', () => window.__T().m3Close(), 4000);
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
