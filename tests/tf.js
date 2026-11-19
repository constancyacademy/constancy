// test V306.1-4 : accueil (voiture sur chaque plan, un seul gros bouton), sauvegarde sans mur, source ?s=tt, badge Jour 1. Aucun appel réseau (tout est coupé).
const { chromium } = require('playwright'); const path = require('path');
(async () => { const page = path.resolve(process.argv[2]), out = process.argv[3] || '/tmp/cont/tf_';
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const mk = async (ua) => { const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, hasTouch: true, isMobile: true, userAgent: ua }); await ctx.route(/^https?:/, r => r.abort()); const p = await ctx.newPage(); p.errs = []; p.on('pageerror', e => p.errs.push(e.message.slice(0, 160))); return p; };
  const IOS = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
  const p = await mk(IOS); const t0 = Date.now();
  await p.goto('file://' + page + '?nostat=1&s=tt&jour1=1'); await p.evaluate(() => { try { sessionStorage.setItem('cst-relance', '1'); } catch (e) {} }); await p.waitForSelector('#quick', { timeout: 900000 }); console.log('title', (Date.now() - t0) / 1000);
  await p.waitForFunction(() => { const X = window.__X && window.__X(); return X && X.TCAM && X.TCAM.t > 0.5; }, null, { timeout: 600000, polling: 1000 });
  for (const t of [0.8, 9]) { await p.evaluate(t => { window.__X().TCAM.t = t; }, t); await p.waitForTimeout(5000);
    const vis = await p.evaluate(() => { const X = window.__X(), T = X.TCAM, cam = X.camera; if (!T.car || !T.car.visible) return 'voiture absente'; const v = T.car.position.clone().project(cam); return 'voiture ' + (Math.abs(v.x) < 1 && Math.abs(v.y) < 1 && v.z < 1 ? 'DANS LE CHAMP' : 'hors champ') + ' x' + v.x.toFixed(2) + ' y' + v.y.toFixed(2); });
    console.log('accueil t=' + t, vis); await p.screenshot({ path: out + 'accueil_' + String(t).replace('.', '_') + '.png', timeout: 600000 }); }
  console.log('boutons', await p.evaluate(() => [...document.querySelectorAll('.panel .btn, .panel .tlink')].map(e => e.className + ':' + e.textContent.trim().slice(0, 40)).join(' | ')));
  // parcours
  await p.click('#quick', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForSelector('#ok', { timeout: 600000 }); await p.waitForTimeout(500); await p.evaluate(() => document.getElementById('ok').click());
  await p.waitForSelector('.choice', { timeout: 600000 }); await p.waitForTimeout(800);
  await p.evaluate(() => { window.__F().openEmailGate(() => window.__afterOK = 1, 2); }); await p.waitForTimeout(1500); await p.screenshot({ path: out + 'sauvegarde.png', timeout: 600000 });
  await p.evaluate(() => { const e = document.getElementById('em'), w = document.getElementById('emPw'); e.value = 'constancy.test.v306@gmail.com'; e.dispatchEvent(new Event('input')); w.value = 'abc123'; w.dispatchEvent(new Event('input')); }); await p.waitForTimeout(2500); await p.evaluate(() => document.getElementById('emGo').click()); await p.waitForTimeout(4000);
  console.log('après sauvegarde', await p.evaluate(() => ({ after: window.__afterOK, gate: !!document.getElementById('em'), confirmWait: /Confirme ton adresse/.test(document.body.innerText) && !!document.querySelector('.panel.eg'), cash: window.__W().P.cash, email: window.__W().P.email, src: window.__W().P.src, err: (document.getElementById('emErr') || {}).textContent })));
  await p.screenshot({ path: out + 'apres_sauvegarde.png', timeout: 600000 });
  await p.click('.choice', { force: true, noWaitAfter: true, timeout: 600000 }).catch(() => {}); await p.waitForTimeout(15000);
  console.log('stats', await p.evaluate(() => window.__stats.join(' ')));
  console.log('P', await p.evaluate(() => { const P = window.__W().P; return JSON.stringify({ src: P.src, badgeJ1: P.badgeJ1, firstD: P.firstD, cash: P.cash }); }));
  await p.screenshot({ path: out + 'en_jeu.png', timeout: 600000 });
  await p.evaluate(() => window.__F().openMenu()); await p.waitForTimeout(1500); await p.screenshot({ path: out + 'menu.png', timeout: 600000 });
  console.log('ERR', p.errs.slice(0, 6).join(' || ') || 'none'); await b.close(); })();
