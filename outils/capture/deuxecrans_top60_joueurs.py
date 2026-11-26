# Moitié haute DEUX ÉCRANS à 60 i/s pour joueurs_b1 : compteur « +0 → +N joueurs. » dès l'image 1 avec « Et toi, t'attends quoi ? », puis les plateformes où le jeu est en ligne
import sys,os
sys.path.insert(0,'/home/claude/rushes/outils/capture')
from deuxecrans_top import W,H,HT,FG,PINK,WHITE
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; total=float(sys.argv[2]); N=int(sys.argv[3]); PLAT=sys.argv[4]; os.makedirs(out,exist_ok=True)
NB=' '
def frame(lines):
  im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); d.rectangle((0,0,W,HT-1),fill=(0,0,0,255)); d.rectangle((0,HT-3,W,HT+1),fill=PINK)
  hs=[int(s*1.15) for _,s,_ in lines]; y=400-sum(hs)//2
  for (t,s,c),h in zip(lines,hs):
    f=ImageFont.truetype(FG,s); tw=d.textlength(t,font=f); d.text(((W-tw)/2,y),t,font=f,fill=c); y+=h
  return im
Q='Et toi, t’attends'+NB+'quoi'+NB+'?'
def state(t):
  if t<1.5:
    k=t/1.5; k=1-(1-k)**3; v=int(round(N*k))
    return ('c%d'%v,[('+%d'%v+NB+'joueurs.',140,PINK if v==N else WHITE),(Q,92,WHITE)])
  if t<2.7: return ('h',[('+%d'%N+NB+'joueurs.',140,PINK),(Q,92,WHITE)])
  if t<5.6: return ('p',[('+%d'%N+NB+'joueurs.',140,PINK),('Ils jouent déjà sur',56,WHITE),(PLAT,50,WHITE)])
  if t<total-0.2: return ('none',None)
  return ('c0',[('+0'+NB+'joueurs.',140,WHITE),(Q,92,WHITE)])
n=round(total*60); cache={}
for i in range(n):
  t=i/60; key,st=state(t)
  if key not in cache:
    im=frame([]) if st is None else frame(st)
    p=f'{out}/k{len(cache)}.png'; im.save(p); cache[key]=p
  dst=f'{out}/f{i:04d}.png'
  if os.path.exists(dst): os.remove(dst)
  os.link(cache[key],dst)
print('frames',n,'states',len(cache))
