# Correctif de l'expert (écrit V310.90, appliqué en V310.95) · usage : python3 tools/patch_v310_95.py index.html (refuse si un texte de départ a changé)
import sys
p = sys.argv[1]; s = open(p, encoding="utf-8").read()
R = [
# 1. prix en euros à côté des Néons (seulement quand le paiement est ouvert) + plafond de 20 € par mois et par appareil
('const NEON_PACKS = [{ id: "p1", n: 100, eur: 0.99 }, { id: "p2", n: 330, eur: 2.99, bonus: 10 }, { id: "p3", n: 600, eur: 4.99, bonus: 20, best: 1 }];',
 'const NEON_PACKS = [{ id: "p1", n: 100, eur: 0.99 }, { id: "p2", n: 330, eur: 2.99, bonus: 10 }, { id: "p3", n: 600, eur: 4.99, bonus: 20, best: 1 }];\n'
 '/* V310.90 (expert, section 11 du prompt : aucune monnaie qui cache le vrai prix, plafond de dépense, beaucoup de joueurs jeunes) : dès que le paiement est ouvert, chaque prix en Néons montre son prix en euros (100 Néons = 0,99 €) · 20 € par mois au plus par appareil */\n'
 'const NEON_EUR = n => { const v = (n * 0.0099).toFixed(2); return LANG === "en" ? "€" + v : v.replace(".", ",") + " €"; }, gEur = n => (payAllowed() ? " · " + NEON_EUR(n) : "");\n'
 'const PAY_CAP = 20; function payMonth() { try { const m = new Date().toISOString().slice(0, 7), o = JSON.parse(localStorage.getItem("cst-pay-mois") || "{}"); return o.m === m ? +o.eur || 0 : 0; } catch (e) { return 0; } } function payMonthAdd(eur) { try { localStorage.setItem("cst-pay-mois", JSON.stringify({ m: new Date().toISOString().slice(0, 7), eur: +(payMonth() + (+eur || 0)).toFixed(2) })); } catch (e) {} }'),
('own ? (on ? shT("Équipé", "Equipped") : shT("À toi", "Owned")) : "◆ " + g.p}</span>',
 'own ? (on ? shT("Équipé", "Equipped") : shT("À toi", "Owned")) : "◆ " + g.p + gEur(g.p)}</span>'),
('${can ? shT("Acheter", "Buy") + " · ◆ " + g.p : ',
 '${can ? shT("Acheter", "Buy") + " · ◆ " + g.p + gEur(g.p) : '),
('  const ref = (shopPayId() || "x") + "." + k.id + "." + Date.now().toString(36), eur = k.eur.toFixed(2);',
 '  if (payMonth() + k.eur > PAY_CAP + 0.001) { shopStat("plafond_mois", k.id); show(`<div class="panel gshop" data-out><div class="kicker">${shT("Néons", "Neons")}</div><h2>${shT("Plafond du <em>mois</em>", "Monthly <em>limit</em>")}</h2><p class="lead" style="font-size:14px">${shT("Sur cet appareil, les achats sont limités à 20 € par mois. Ce pack dépasserait ce plafond.", "On this device, purchases are capped at €20 a month. This pack would go over it.")}</p><p class="note">${shT("Tout le reste se gagne en jouant. Chaque livraison te rapporte des Néons.", "Everything else is earned by playing. Every delivery earns you Neons.")}</p><button class="btn" id="gPkBack" type="button">${shT("Retour", "Back")}</button></div>`); on("gPkBack", () => openShop(null, "packs")); return; }\n'
 '  const ref = (shopPayId() || "x") + "." + k.id + "." + Date.now().toString(36), eur = k.eur.toFixed(2);'),
('<p class="note" id="ppWait">${shT("Chargement du paiement…", "Loading payment…")}</p></div><button class="btn alt" id="gPkBack" type="button">',
 '<p class="note" id="ppWait">${shT("Chargement du paiement…", "Loading payment…")}</p></div><p class="note">${shT("Plafond : 20 € par mois sur cet appareil.", "Limit: €20 a month on this device.")}</p><button class="btn alt" id="gPkBack" type="button">'),
# 2. bouton PayPal noir (charte : pas de jaune)
('style: { layout: "vertical", color: "gold", shape: "pill", label: "pay" }',
 'style: { layout: "vertical", color: "black", shape: "pill", label: "pay" }'),
('shopInit(); P.neons += r.neons; saveNow();',
 'shopInit(); P.neons += r.neons; payMonthAdd(r.eur); saveNow();'),
# 3. tâche 3 de la file : à quel % et au bout de combien de secondes partent les joueurs des portails
('ov.querySelector("b").textContent = pct + "%";',
 'window.__plPct = pct; { const M = window.__plM || (window.__plM = { bk: 0, ts: 0, n: 0 }), bk = Math.floor(pct / 20), el = Date.now() - t0; if (!PL.rank || PL.rank < 2) { if (bk > M.bk || el - M.ts > 15000) { M.bk = Math.max(bk, M.bk); M.ts = el; if (++M.n <= 8) plSend(); } } } /* V310.90 (expert) : pendant le chargement, une ligne anonyme à chaque palier de 20 % et toutes les 15 s (8 au plus) · un joueur qui ferme pendant que la construction bloque la page n\'envoie plus rien en partant, on garde ainsi le dernier palier vu */ ov.querySelector("b").textContent = pct + "%";'),
('"&e=" + encodeURIComponent(PL.step || "Accueil")',
 '"&e=" + encodeURIComponent((PL.rank || 0) >= 2 ? PL.step : ((PL.step || "Accueil") + (window.__plPct != null && G.mode !== "play" ? " · " + window.__plPct + " % · " + Math.round(performance.now() / 1000) + " s" : ""))) /* V310.90 (expert) : un joueur parti pendant le chargement est noté « Accueil · 40 % · 12 s » (pourcentage affiché, secondes depuis l\'ouverture de la page) */'),
('const put = () => { if (document.body) document.body.appendChild(ov); else setTimeout(put, 30); }; put(); const t0 = Date.now();',
 'const put = () => { if (document.body) document.body.appendChild(ov); else setTimeout(put, 30); }; put(); const t0 = Date.now(); addEventListener("pagehide", () => { if (G.mode !== "play" && window.__plPct != null && !window.__plQ) { window.__plQ = 1; stat("portail-quitte-" + Math.min(80, Math.floor(window.__plPct / 20) * 20) + "pct"); } });'),
# 4. charte (pas de jaune) : la plaque et les feux d'artifice de la vitrine passent en rose
('{ id: "g07", cat: "car", slot: "plate", p: 40, ic: "▭", c: "#ffd23f",', '{ id: "g07", cat: "car", slot: "plate", p: 40, ic: "▭", c: "#ff8fd0",'),
('{ id: "g17", cat: "fx", slot: "fw", p: 80, ic: "✺", c: "#ffd23f",', '{ id: "g17", cat: "fx", slot: "fw", p: 80, ic: "✺", c: "#ff2d95",'),
]
for a, b in R:
    n = s.count(a)
    if n != 1: sys.exit("REFUS : texte de départ trouvé %d fois : %s" % (n, a[:90]))
for a, b in R: s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s); print("OK", len(R), "remplacements")
