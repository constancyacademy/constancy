// Plans de l'écran d'accueil d'un joueur qui revient : une capture par plan (TCAM.t forcé au milieu de chaque plan) · node accueil_plans.js page.html save.json sortie_ "2,3,6,7"
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4] || '/tmp/pl_', list = (process.argv[5] || '0,1,2,3,4,5,6,7,8,9,10,11,12,13').split(',').map(Number);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:\/\/(?!cdnjs|cdn\.jsdelivr|fonts\.)/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const ok = await p.evaluate(() => !!document.getElementById('cont')).catch(() => false); if (ok) break; }
  await p.evaluate(() => { const g = document.getElementById('guide'); if (g) g.remove(); document.querySelectorAll('#screen').forEach(e => e.style.opacity = '0.15'); });
  for (const i of list) { await p.evaluate(i => { window.__TC.TCAM.t = i * 7 + 3.2; }, i); await p.waitForTimeout(6000); await p.screenshot({ path: out + String(i).padStart(2, '0') + '.png', timeout: 60000 }).catch(() => {}); }
  const seq = await p.evaluate(() => JSON.stringify(window.__TC.TSEQ)); console.log('TSEQ', seq, 'ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
