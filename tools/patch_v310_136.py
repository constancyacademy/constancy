# V310.136 · « REJOINS-MOI » VERSION 1 SUR CRAZYGAMES (commande de la BUSINESS du 28/11 12h50, point 2 · 0 € : aucun serveur nouveau)
# - menu Pause : « 👥 Inviter un ami » aussi sur CrazyGames (lien d'invitation de LEUR SDK, game.inviteLink({ p: <id du joueur> }), jamais de lien externe)
# - l'ami qui arrive par ce lien (getInviteParam("p")) reçoit +$1 000 et le badge Crew à SA 1re livraison
# - le joueur qui invite : +$1 000 et le badge Crew pour chaque ami arrivé à sa 1re livraison, et la carte « Mon équipe » (pseudo, jour, argent)
#   · côté données : chaque ligne anonyme envoie &ref=<id de celui qui invite>&rl=<1 dès la 1re livraison> au script existant, qui répond à action=crew&id=<id>
#   · tant que le script ne répond pas à action=crew, la carte affiche 0 ami et rien ne casse (code du script : claude/constancy-script-crew-28-11.txt)
# - après la 1re livraison sur CrazyGames, une bulle propose d'inviter un ami (une fois)
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
# arrivée par un lien d'invitation CrazyGames
rep('window.CrazyGames.SDK.init().then(() => { PSDK.cg = window.CrazyGames.SDK;',
    'window.CrazyGames.SDK.init().then(() => { PSDK.cg = window.CrazyGames.SDK; try { const r = PSDK.cg.game.getInviteParam("p"); if (r && /^[a-z0-9]{6,16}$/.test(r) && r !== plId()) { localStorage.setItem("constancy-ref", r); stat("cg-invite-arrivee"); } } catch (e) {} /* V310.136 · Rejoins-moi */')
# l'ami (cadeau à sa 1re livraison), la bulle après la 1re livraison et la vérification de l'équipe toutes les 5 min : une horloge à part, sur CrazyGames seulement (socialTick n'est appelé nulle part, constancy.fr inchangé)
rep('function refreshReferrals() {', '''function crewTick() { if (PORTAL !== "cg" || CREATOR || !P || G.mode !== "play") return; const t = P.playS || 0;
  if (!P.refWelcome && refCode() && (P.deliveries || 0) >= 1) { P.refWelcome = 1; addCash(FRIEND_BONUS, true); P.badges = P.badges || {}; P.badges.crew = 1; saveNow(); stat("bienvenue-filleul"); try { plSend(); } catch (e) {} notify("gold", `<b>Un ami t'a invité.</b> <span>Cadeau de ta 1re livraison :</span> <b style="color:var(--cash)">+$${fmt(FRIEND_BONUS)}</b> <span>· badge Crew.</span>`, 8); return; }
  if ((P.deliveries || 0) >= 1 && !P.crewAsk && !G.mission && !G.inside && !CINE.on) { P.crewAsk = 1; saveNow(); stat("cg-invite-bulle"); notify("gold", "<b>Joue avec tes amis.</b> <span>Invite un ami : +$1,000 pour vous deux.</span> <span>Menu › Inviter un ami</span>", 8); }
  if (t - (P.crewAt || 0) > 300) { P.crewAt = t; crewCheck(); } }
if (PORTAL === "cg") setInterval(() => { try { crewTick(); } catch (e) {} }, 3000);
function refreshReferrals() {''')
# plSend : &ref et &rl
rep('+ "&cash=" + Math.round((P && P.cash) || 0) + "&tg="',
    '+ (refCode() ? "&ref=" + refCode() + "&rl=" + (((P && P.deliveries) || 0) >= 1 ? 1 : 0) : "") /* V310.136 · Rejoins-moi */ + "&cash=" + Math.round((P && P.cash) || 0) + "&tg="')
# fonctions de l'équipe
rep('function crewTick() {',
    '''/* V310.136 · « Rejoins-moi » sur CrazyGames : l'équipe est lue au script existant (action=crew), sans serveur nouveau */
const CREW = { list: [], n: 0, ok: false, busy: false };
function crewCheck(then) { try { if (CREW.busy || NOSTAT || typeof VERIFY_URL === "undefined" || !VERIFY_URL) { if (then) then(); return; } const id = plId(); if (!id) { if (then) then(); return; } CREW.busy = true;
    fetch(VERIFY_URL + "?action=crew&id=" + encodeURIComponent(id)).then(r => r.json()).then(j => { CREW.busy = false; if (!j || typeof j.n !== "number") { if (then) then(); return; } CREW.ok = true; CREW.n = j.n; CREW.list = Array.isArray(j.list) ? j.list.slice(0, 30) : []; const paid = P.filleulsPaid || 0;
      if (CREW.n > paid) { const k = CREW.n - paid; P.filleulsPaid = CREW.n; P.badges = P.badges || {}; P.badges.crew = 1; addCash(REF_BONUS * k, true); saveNow(); stat("cg-invite-recompense"); try { celebrate(4); } catch (e) {} notify("gold", `<b>${k > 1 ? k + " amis ont" : "Un ami a"} fait sa 1re livraison grâce à toi.</b> <b style="color:var(--cash)">+$${fmt(REF_BONUS * k)}</b> · badge Crew.`, 8); }
      if (then) then(); }).catch(() => { CREW.busy = false; if (then) then(); }); } catch (e) { CREW.busy = false; if (then) then(); } }
function openCrewCG(fromMenu) { setMode("menu"); stat("cg-invite-carte");
  show(`<div class="panel"><div class="kicker" style="color:#ff6fbf">Mon équipe</div><h2>Invite tes amis. Gagnez tous les deux.</h2>
    <div class="card" style="gap:8px"><p class="lead" style="margin:0">🤝 <span>+$1,000 pour ton ami à sa 1re livraison.</span><br>🎁 <span>+$1,000 pour toi et le badge Crew quand il l'a faite.</span></p></div>
    <input class="linkbox" id="crewLink" readonly value="…" style="font-size:12px;box-sizing:border-box;width:100%;max-width:100%;text-align:center;border-radius:16px">
    <button class="btn pink" id="crewCopy" type="button">Copier mon lien</button>
    <div class="card" id="crewList" style="gap:4px"><p class="note" style="margin:0">Chargement…</p></div>
    <button class="btn alt" id="crewBack" type="button">${fromMenu ? "Retour" : "Plus tard"}</button></div>`, "mail");
  on("crewBack", () => fromMenu ? openMenu() : resume());
  let link = ""; try { const sdk = PSDK.cg; if (sdk && sdk.game && sdk.game.inviteLink) Promise.resolve(sdk.game.inviteLink({ p: plId() })).then(u => { link = String(u || ""); const el = $("crewLink"); if (el) el.value = link || "—"; }).catch(() => {}); else { const el = $("crewLink"); if (el) el.value = "—"; } } catch (e) {}
  on("crewCopy", () => { if (!link) { help("Le lien d'invitation n'est pas disponible pour le moment.", 4); return; } const done = () => { stat("cg-invite-copie"); help("<b>Lien copié.</b> Envoie-le à tes amis.", 4); }; try { navigator.clipboard.writeText(link).then(done, () => { const el = $("crewLink"); if (el) { el.select(); try { document.execCommand("copy"); done(); } catch (e) {} } }); } catch (e) { const el = $("crewLink"); if (el) { el.select(); try { document.execCommand("copy"); done(); } catch (e2) {} } } });
  const draw = () => { const el = $("crewList"); if (!el) return; const L = CREW.list || []; el.innerHTML = `<p class="note" style="margin:0"><span>Amis arrivés :</span> <b>${CREW.n || 0}</b></p>` + L.map(f => `<div style="display:flex;justify-content:space-between;gap:8px;padding:6px 2px;border-top:1px solid rgba(255,255,255,.08)"><span>${String(f.p || "Player").replace(/[<>&"]/g, "").slice(0, 16)}</span><span>Day ${+f.d || 1} · $${fmt(+f.c || 0)}</span></div>`).join(""); };
  crewCheck(draw); }
function crewTick() {''')
# menu Pause : bouton aussi sur CrazyGames
rep('${DOOR === "nomail" ? "" : `<button class="pm-t pk" id="shareM" type="button">${pmIcon("share")}<span>Inviter un ami</span></button>`}',
    '${DOOR === "nomail" && !(PORTAL === "cg" && !CREATOR) ? "" : `<button class="pm-t pk" id="shareM" type="button">${pmIcon("share")}<span>Inviter un ami</span></button>`}')
rep('on("shareM", () => openShare(true));', 'on("shareM", () => PORTAL === "cg" ? openCrewCG(true) : openShare(true));')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611281430';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
