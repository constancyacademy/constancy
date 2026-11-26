// Joueur d'un portail qui REVIENT (2e visite, partie déjà sauvée) : entre-t-il en jeu sans toucher ? · node portail_retour.js dossier_du_zip sortie_
const { chromium } = require('playwright'); const path = require('path');
(async () => { const dir = path.resolve(process.argv[2]), out = process.argv[3] || '/tmp/pr_';
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort()); await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + dir + '/index.html?nostat=1');
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 }); console.log('VISITE 1 EN JEU');
  await p.waitForTimeout(15000); await p.evaluate(() => { try { window.saveNow && saveNow(); } catch (e) {} });
  const t0 = Date.now(); await p.reload();
  let ok = false; for (let k = 0; k < 150; k++) { await p.waitForTimeout(2000); const s = await p.evaluate(() => ({ st: (window.__stats || []).includes('partie-lancee'), pl: (document.querySelector('#plLoad') || {}).innerText || '', vis: !!document.querySelector('#plLoad') })).catch(() => ({})); if (s.st) { ok = true; break; } if (k % 10 === 9) console.log('ATTENTE', ((Date.now() - t0) / 1000).toFixed(0) + 's', JSON.stringify(s).slice(0, 200)); }
  await p.screenshot({ path: out + 'retour.png', timeout: 120000 }).catch(() => {});
  const ui = await p.evaluate(() => document.body.innerText.replace(/\s+/g, ' ').slice(0, 300)).catch(() => '');
  console.log(ok ? 'VISITE 2 EN JEU ' + ((Date.now() - t0) / 1000).toFixed(0) + 's' : 'VISITE 2 BLOQUEE', '· ECRAN', ui, '· ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
