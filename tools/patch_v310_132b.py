# V310.132 (suite) · Playgama : le jeu ne repart qu'à la fermeture de la pub (« rewarded » arrive avant « closed »), le son aussi · le « +$500 » s'affiche au retour dans le jeu
# Usage, après patch_v310_132.py : python3 tools/patch_v310_132b.py
import os
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('if ((st === "closed" || st === "failed" || st === "rewarded") && c && adRewarded.mute) { adRewarded.mute = 0; c.resume(); }',
    'if ((st === "closed" || st === "failed") && c && adRewarded.mute) { adRewarded.mute = 0; c.resume(); }')
rep('if (st === "rewarded") adRewarded.ok && adRewarded.ok(); else if (st === "failed" || st === "closed") setTimeout(() => adRewarded.ko && adRewarded.ko(), 300);',
    'if (st === "rewarded") adRewarded.ok && adRewarded.ok(); else if (st === "failed" || st === "closed") { adRewarded.shut = 1; setTimeout(() => { adRewarded.ko && adRewarded.ko(); adUnpause(); }, 300); }')
rep('if (pgM) { adUnpause(); addCash(500, true); try { cashFly(500); } catch (e) {} saveNow(); shopStat("pub_vue", k); help("<b>+$500</b> · Thanks for watching!", 4); return; }',
    'if (pgM) { addCash(500, true); try { cashFly(500); } catch (e) {} saveNow(); shopStat("pub_vue", k); adRewarded.msg = 1; if (!adRewarded.open || adRewarded.shut || !adRewarded.pz) adUnpause(); if (adRewarded.msg && !adRewarded.pz) { adRewarded.msg = 0; help("<b>+$500</b> · Thanks for watching!", 4); } return; }')
rep('function adUnpause() { if (!adRewarded.pz) return; adRewarded.pz = 0; try { if (G.mode === "menu" && screen.classList.contains("hidden")) resume(); const c = SND.ctx; if (c && c.state === "suspended" && SND.on !== false) c.resume(); } catch (e) {} }',
    'function adUnpause() { if (!adRewarded.pz) return; adRewarded.pz = 0; try { if (G.mode === "menu" && screen.classList.contains("hidden")) resume(); const c = SND.ctx; if (c && c.state === "suspended" && SND.on !== false) c.resume(); if (adRewarded.msg) { adRewarded.msg = 0; help("<b>+$500</b> · Thanks for watching!", 4); } } catch (e) {} }')
rep('adRewarded.open = 0; bridge.advertisement.showRewarded();', 'adRewarded.open = 0; adRewarded.shut = 0; adRewarded.msg = 0; bridge.advertisement.showRewarded();')
open(p, "w", encoding="utf-8").write(s); print("OK", n, "remplacements")
