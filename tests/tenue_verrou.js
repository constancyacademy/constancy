// Tenue premium verrouillée : « C'est moi » grisé et refusé · node tenue_verrou.js page_avec___TC.html save.json
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:\/\/(?!cdnjs|cdn\.jsdelivr|fonts\.)/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const g = document.getElementById('guide'); if (g) g.remove(); window.__TC.av(); }); await p.waitForTimeout(2500);
  await p.evaluate(() => { const t = document.querySelector('[data-tab="accessoires"]'); if (t) t.click(); }); await p.waitForTimeout(2000);
  const r1 = await p.evaluate(() => { const b = [...document.querySelectorAll('[data-prem]')].find(x => x.dataset.prem); if (!b) return 'pas de tenue premium'; b.click(); return 'essai ' + b.dataset.prem; }); await p.waitForTimeout(2000);
  const r2 = await p.evaluate(() => { const ok = document.getElementById('ok'); return ok ? 'opacity ' + ok.style.opacity + ' aria ' + ok.getAttribute('aria-disabled') : 'pas de bouton'; });
  await p.evaluate(() => document.getElementById('ok').click()); await p.waitForTimeout(1500);
  const r3 = await p.evaluate(() => ({ encore: !!document.getElementById('ok'), aide: (document.querySelector('.help, #help') || {}).innerText || '' }));
  await p.screenshot({ path: '/tmp/tenue.png' }).catch(() => {});
  console.log('TENUE', r1, '· BOUTON', r2, '· APRES CLIC', JSON.stringify(r3).slice(0, 200), '· ERR', errs.length ? errs.slice(0, 2).join(' | ') : 'none'); await b.close(); })();
