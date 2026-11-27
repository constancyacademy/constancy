# V310.98 · INSCRIPTIONS : « Tu pensais à icloud.com ? » pour toute faute de 1 ou 2 lettres dans un domaine courant (Joueur2812 avait tapé « icoud.com », absent de la liste EM_FIX) · suggestion qui ne bloque pas (un 2e toucher garde l'adresse telle quelle) · statistiques mail-correction-proposee et mail-correction-prise.
# Usage : python3 tools/patch_v310_98.py index.html  →  « OK 2 remplacements »  (correctif de l'expert, claude/constancy-correctif-poki-mail-27-11.txt)
import sys
p = sys.argv[1] if len(sys.argv) > 1 else "index.html"
s = open(p, encoding="utf-8").read()
R = []
A1 = 'const EM_FIX = { "gmial.com": "gmail.com",'
B1 = r'''/* V310.98 (expert, 27/11 13h07) : domaines courants pour la suggestion à 1 ou 2 lettres près · les domaines proches mais vrais (ymail, mail.com, live, gmx, aol…) sont dans la liste, donc jamais corrigés */ const EM_DOMS = ["gmail.com", "hotmail.fr", "hotmail.com", "outlook.fr", "outlook.com", "icloud.com", "yahoo.fr", "yahoo.com", "orange.fr", "free.fr", "sfr.fr", "laposte.net", "live.fr", "live.com", "wanadoo.fr", "me.com", "msn.com", "ymail.com", "mail.com", "aol.com", "gmx.fr", "gmx.com", "neuf.fr", "bbox.fr", "proton.me", "protonmail.com", "hotmail.be", "skynet.be", "bluewin.ch", "yahoo.be", "outlook.be", "hotmail.ch", "gmx.ch", "mac.com", "googlemail.com", "numericable.fr", "aliceadsl.fr", "club-internet.fr", "voila.fr", "hotmail.co.uk", "yahoo.co.uk", "outlook.es", "hotmail.es", "gmail.fr"];
function emNear(d) { try { d = String(d || "").toLowerCase(); if (!d || d.length < 5 || EM_DOMS.includes(d)) return null; const lev = (a, b) => { const m = a.length, n = b.length; if (Math.abs(m - n) > 2) return 9; let pr = Array.from({ length: n + 1 }, (_, j) => j); for (let i = 1; i <= m; i++) { const cu = [i]; for (let j = 1; j <= n; j++) cu[j] = Math.min(pr[j] + 1, cu[j - 1] + 1, pr[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); pr = cu; } return pr[n]; }; let best = null, bd = 3, tie = false; for (const t of EM_DOMS) { if (t === "gmail.fr") continue; const k = lev(d, t); if (k < bd) { bd = k; best = t; tie = false; } else if (k === bd) tie = true; } return bd <= 2 && !tie ? best : null; } catch (e) { return null; } }
'''
R.append((A1, B1 + A1))
A2 = '''{ const dom = v.split("@")[1], fix = EM_FIX[dom] || (() => { const tld = dom.replace(/\\.(con|cmo|cm|ocm|fe|fr\\.)$/, m => ({ ".con": ".com", ".cmo": ".com", ".cm": ".com", ".ocm": ".com", ".fe": ".fr" })[m] || m); return tld !== dom ? tld : null; })();'''
B2 = A2 + ''' if (!fix) { const nf = emNear(dom); if (nf) { chk.innerHTML = '<span style="color:#ff9ec4">Tu pensais à <button type="button" id="emFix" style="background:none;border:0;padding:0;color:#ff9ec4;font:700 inherit;text-decoration:underline;cursor:pointer">' + v.split("@")[0] + "@" + nf + "</button> ?</span>"; try { if (!emNear.s) { emNear.s = 1; stat("mail-correction-proposee"); } } catch (e) {} const b = $("emFix"); if (b) b.onclick = () => { try { stat("mail-correction-prise"); } catch (e) {} $("em").value = v.split("@")[0] + "@" + nf; verify(); }; return; } }'''
R.append((A2, B2))
n = 0
for a, b in R:
    c = s.count(a)
    if c != 1: sys.exit("ÉCHEC : %d occurrence(s) de %r" % (c, a[:90]))
    s = s.replace(a, b); n += 1
open(p, "w", encoding="utf-8").write(s)
print("OK %d remplacements" % n)
