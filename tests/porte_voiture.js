// Sortie de l'appart (intro « door ») : la voiture est-elle loin de la porte ? · node porte_voiture.js page_avec___TC.html save.json
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:\/\/(?!cdnjs|cdn\.jsdelivr|fonts\.)/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  console.log('MODE', await p.evaluate(() => window.__W().G.mode + ' ' + typeof window.__W().meMesh));
  await p.evaluate(() => { const g = document.getElementById('guide'); if (g) g.remove(); window.__TC.sih(); }); await p.waitForTimeout(2500);
  await p.evaluate(() => { const G = window.__W().G, s = window.__TC.st(); if (G.parked) { G.parked.x = s.home[0] + 6; G.parked.z = s.home[1] + 4; if (G.parked.mesh) { G.parked.mesh.position.x = G.parked.x; G.parked.mesh.position.z = G.parked.z; } } }); await p.evaluate(() => window.__TC.lh()); await p.waitForTimeout(3000);
  const st = await p.evaluate(() => window.__TC.st()); const d = st.pk ? Math.hypot(st.pk[0] - st.me[0], st.pk[1] - st.me[1]) : -1, dh = st.pk ? Math.hypot(st.pk[0] - st.home[0], st.pk[1] - st.home[1]) : -1;
  await p.screenshot({ path: '/tmp/porte.png' }).catch(() => {});
  console.log('INTRO', st.g, '· voiture à', d.toFixed(1), 'm du joueur ·', dh.toFixed(1), 'm de la porte · ERR', errs.length ? errs.slice(0, 2).join(' | ') : 'none'); await b.close(); })();
