# V310.105 · PLAYGAMA, dernier blocage de la certification (BUSINESS 27/11 16h00 : « No advertising is implemented », leur test ne fait pas la 1re livraison)
# Porte pg seulement : bouton au choix « ▶ Watch an ad · Start with +$500 » sur l'écran de chargement (avant la 1re mission), isRewardedSupported noté en stat · le bouton après la 1re livraison reste
# Usage, depuis la racine du dépôt : python3 tools/patch_v310_105.py
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
FN = r'''/* V310.105 · Playgama (certification du 27/11 16h00 : « No advertising is implemented », leur test automatique ne fait pas la 1re livraison) : porte pg seulement, pendant l'écran de chargement d'une partie (avant la 1re mission), un bouton AU CHOIX « ▶ Watch an ad · Start with +$500 » · jamais imposé, jamais pendant une mission · les 500 $ arrivent dès que le joueur est en jeu · bridge.advertisement.isRewardedSupported noté en stat (pg-rewarded-oui/non) */
function pgAdStart(ov) { if (PORTAL !== "pg" || CREATOR || !ov || document.getElementById("pgAd0")) return; const b = document.createElement("button"); b.id = "pgAd0"; b.type = "button"; const T0 = "▶ Watch an ad · Start with +$500"; b.textContent = T0; b.style.cssText = "display:none;margin-top:22px;pointer-events:auto;border:0;border-radius:999px;padding:10px 18px;background:rgba(255,45,149,.92);color:#fff;font:700 13px Inter,system-ui,sans-serif;box-shadow:0 4px 18px rgba(0,0,0,.35);cursor:pointer"; ov.appendChild(b);
  const iv = setInterval(() => { try { if (!ov.isConnected) { clearInterval(iv); return; } const br = PSDK.pg; if (!br || !br.advertisement || window.__pgStartBonus) return; if (pgAdStart.sup == null) { pgAdStart.sup = br.advertisement.isRewardedSupported; window.__pgRw = pgAdStart.sup; stat("pg-rewarded-" + (pgAdStart.sup === false ? "non" : "oui")); } if (b.style.display === "none" && !pgAdStart.busy && !pgAdStart.dead) { b.style.display = ""; stat("pub-pg-depart-vue"); } } catch (e) {} }, 500);
  b.addEventListener("click", e => { e.stopPropagation(); const br = PSDK.pg; if (pgAdStart.busy || window.__pgStartBonus || !br) return; pgAdStart.busy = 1; b.textContent = "Loading the ad…"; stat("pub-pg-depart-clic"); let open = 0, done = 0;
    const fin = ok => { if (done) return; done = 1; pgAdStart.busy = 0; if (ok) { window.__pgStartBonus = 1; stat("pub-pg-depart-ok"); b.textContent = "✓ +$500 waiting for you in the game"; b.style.background = "rgba(30,170,100,.92)"; b.style.pointerEvents = "none"; } else if (!open) { pgAdStart.dead = 1; b.textContent = "Ad not available right now"; b.style.pointerEvents = "none"; setTimeout(() => { b.style.display = "none"; }, 2500); } else b.textContent = T0; };
    const h = st => { if (done && !pgAdStart.mute) { try { br.advertisement.off("rewarded_state_changed", h); } catch (e) {} return; } try { const c = SND.ctx; if (st === "opened") { open = 1; if (c && c.state === "running") { c.suspend(); pgAdStart.mute = 1; } } if ((st === "closed" || st === "failed" || st === "rewarded") && c && pgAdStart.mute) { pgAdStart.mute = 0; c.resume(); } } catch (e) {} if (st === "rewarded") fin(1); else if (st === "failed" || st === "closed") setTimeout(() => fin(0), 300); };
    try { br.advertisement.on("rewarded_state_changed", h); br.advertisement.showRewarded(); } catch (e2) { fin(0); } setTimeout(() => { if (!open) fin(0); }, 15000); }); }
window.__pgAdStart = pgAdStart; if (PORTAL === "pg" && !CREATOR) { let k_ = 0; const t_ = setInterval(() => { try { const o = document.getElementById("plLoad"); if (o) { clearInterval(t_); pgAdStart(o); } else if (++k_ > 40) clearInterval(t_); } catch (e) { clearInterval(t_); } }, 250); } /* l'écran de chargement est créé dans une autre portée du script : on le retrouve par son id */
'''
A1 = 'function pgAdBtn() { if (PORTAL !== "pg" || CREATOR) return;'
rep(A1, FN + A1 + ' if (window.__pgStartBonus === 1 && P && G.mode === "play" && !CINE.on) { window.__pgStartBonus = 2; addCash(500, true); try { cashFly(500); } catch (e) {} saveNow(); stat("pub-pg-depart-bonus"); } /* V310.105 : les 500 $ de la pub regardée pendant le chargement */')
rep('put(); const t0 = Date.now(); addEventListener("pagehide",', 'put(); try { if (PORTAL === "pg") window.__pgAdStart && window.__pgAdStart(ov); } catch (e) {} const t0 = Date.now(); addEventListener("pagehide",')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271630';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
