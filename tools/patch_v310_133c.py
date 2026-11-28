# V310.133 (suite 2) · traduction : une ligne du fil de la ville précédée de « : » est traduite comme la même phrase sans les deux-points
import os
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('let hit = 0; if (ps.length > 1) { const o2 = ps.map(q => { const nq = q.match(I18N.NUM) || [], kq = q.replace(I18N.NUM, "#"); let eq = I18N.d[kq];',
    'let hit = 0; if (ps.length > 1 || /^[:·] /.test(k)) { const o2 = ps.map(q => { const nq = q.match(I18N.NUM) || [], kq = q.replace(I18N.NUM, "#"); let eq = I18N.d[kq]; if (eq == null && /^[:·] /.test(kq) && I18N.d[kq.slice(2)] != null) eq = kq.slice(0, 2) + I18N.d[kq.slice(2)];')
open(p, "w", encoding="utf-8").write(s); print("OK", n, "remplacement")
