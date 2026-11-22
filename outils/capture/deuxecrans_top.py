# Moitié haute du format DEUX ÉCRANS : fond noir 1080x960, texte EB Garamond blanc, mots clés qui passent en rose
import sys,json,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H,HT=1080,1920,960
FG='/tmp/fnt/ebg700.ttf'; PINK=(255,63,164,255); WHITE=(255,255,255,255)
NB=' '
def block(lines,fsz,hl,cy=394):
  """lines: liste de listes de (mot, clé). hl: ensemble des clés en rose."""
  im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
  d.rectangle((0,0,W,HT-1),fill=(0,0,0,255))
  d.rectangle((0,HT-3,W,HT+1),fill=(255,63,164,255))
  f=ImageFont.truetype(FG,fsz); lh=int(fsz*1.12); y0=cy-lh*len(lines)//2-int(fsz*0.12)
  for i,ln in enumerate(lines):
    full=' '.join(w for w,k in ln); tw=d.textlength(full,font=f); x=(W-tw)/2; y=y0+i*lh
    for j,(w,k) in enumerate(ln):
      s=w+(' ' if j<len(ln)-1 else '')
      col=PINK if k and k in hl else WHITE
      d.text((x,y),w.replace('6','6'),font=f,fill=col)
      x+=d.textlength(s,font=f)
  return im
if __name__=='__main__':
  cfg=json.load(open(sys.argv[1])); out=cfg['out']; os.makedirs(out,exist_ok=True)
  n=round(cfg['total']*30); cache={}
  for i in range(n):
    t=(i+0.5)/30; st=None
    for s in cfg['states']:
      if s[0]<=t<s[1]: st=s; break
    key=json.dumps(st[2:]) if st and len(st)>2 else 'none'
    if key not in cache:
      if st is None or len(st)<3 or st[2] is None:
        im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); d.rectangle((0,0,W,HT-1),fill=(0,0,0,255)); d.rectangle((0,HT-3,W,HT+1),fill=(255,63,164,255))
      else: im=block(st[2],st[3],set(st[4]))
      p=f'{out}/k{len(cache)}.png'; im.save(p); cache[key]=p
    dst=f'{out}/f{i:04d}.png'
    if os.path.exists(dst): os.remove(dst)
    os.link(cache[key],dst)
  print('frames',n,'states',len(cache))
