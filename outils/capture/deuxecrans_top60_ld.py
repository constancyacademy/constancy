# Moitié haute DEUX ÉCRANS à 60 i/s · lignedroite_b1 : accroche, 3 · 2 · 1 (le chiffre en cours en rose), « PARTEZ. », « +800 $. » en rose
import sys,os
sys.path.insert(0,'/home/claude/rushes/outils/capture')
from deuxecrans_top import block,W,H,HT
from PIL import Image,ImageDraw
out=sys.argv[1]; total=float(sys.argv[2]); os.makedirs(out,exist_ok=True)
NB=' '
HOOK=[[("Il",None),("m’a",None),("défié",'d')],[("au",None),("feu",'f'),("rouge.",'f')]]
CD=[[("3",'a'),("·",None),("2",'b'),("·",None),("1",'c')]]
def empty():
  im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); d.rectangle((0,0,W,HT-1),fill=(0,0,0,255)); d.rectangle((0,HT-3,W,HT+1),fill=(255,63,164,255)); return im
def state(t):
  if t<0.6: return ('h0',(HOOK,112,[]))
  if t<1.8: return ('h1',(HOOK,112,['d','f']))
  if t<2.3: return ('c3',(CD,190,['a']))
  if t<2.8: return ('c2',(CD,190,['a','b']))
  if t<3.3: return ('c1',(CD,190,['a','b','c']))
  if t<4.6: return ('go',([[("PARTEZ.",'p')]],170,[]))
  if t<5.8: return ('win',([[("+800"+NB+"$.",'m')]],170,['m']))
  if t<total-0.2: return ('none',None)
  return ('h1',(HOOK,112,['d','f']))
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
