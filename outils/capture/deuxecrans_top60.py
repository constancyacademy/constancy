# Moitié haute DEUX ÉCRANS à 60 i/s : accroche, compteur 0 $ → 12 000 $, « Coupé néon · Débloquée. » en rose
import sys,os
sys.path.insert(0,'/home/claude/rushes/outils/capture')
from deuxecrans_top import block,W,H,HT
from PIL import Image,ImageDraw
out=sys.argv[1]; total=float(sys.argv[2]); os.makedirs(out,exist_ok=True)
NB=' '
def money(v): return ('{:,}'.format(v)).replace(',',NB)+NB+'$'
HOOK=[[("Ta",None),("première",None),("voiture.","a")],[("Dès",None),("ta",None),("première",None),("partie.","b")]]
def empty():
  im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); d.rectangle((0,0,W,HT-1),fill=(0,0,0,255)); d.rectangle((0,HT-3,W,HT+1),fill=(255,63,164,255)); return im
def state(t):
  if t<0.5: return ('hook',(HOOK,104,[]))
  if t<1.9: return ('hook2',(HOOK,104,['a','b']))
  if t<3.9:
    k=min(1,(t-1.9)/1.7); k=1-(1-k)**3; v=int(round(12000*k/100))*100
    return ('m%d'%v,([[(money(v),'m' if v==12000 else None)],[("Gagnés",None),("en",None),("livrant.",None)]],120,['m']))
  if t<5.1: return ('deb',([[("Coupé",'c'),("néon.",'c')],[("Débloquée.",'c')]],120,['c']))
  if t<total-0.2: return ('none',None)
  return ('hook',(HOOK,104,[]))
n=round(total*60); cache={}
for i in range(n):
  t=(i+0.5)/60; key,st=state(t)
  if key not in cache:
    im=empty() if st is None else block(st[0],st[1],set(st[2]))
    p=f'{out}/k{len(cache)}.png'; im.save(p); cache[key]=p
  dst=f'{out}/f{i:04d}.png'
  if os.path.exists(dst): os.remove(dst)
  os.link(cache[key],dst)
print('frames',n,'states',len(cache))
