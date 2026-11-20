import sys,os,math
from PIL import Image,ImageDraw,ImageFont
out,total,t_sw,t_loop,label=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),sys.argv[5]
os.makedirs(out,exist_ok=True)
W,H=1080,1920
f=ImageFont.truetype('/tmp/fnt/inter600.ttf',46)
n=int(round(total*30))+2
blank=Image.new('RGBA',(W,H),(0,0,0,0))
def tag(alpha):
  im=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(im)
  tw=d.textlength(label,font=f);w=int(tw+64);h=78;x0=(W-w)//2;y0=168
  d.rounded_rectangle((x0,y0,x0+w,y0+h),radius=39,fill=(255,63,164,int(235*alpha)))
  d.text(((W-tw)/2,y0+13),label,font=f,fill=(255,255,255,int(255*alpha)))
  return im
for i in range(n):
  t=i/30
  if t<t_sw or t>=t_loop:
    a=0.85+0.15*abs(math.sin(t*math.pi*2.0))
    tag(a).save(f'{out}/f{i:04d}.png')
  else: blank.save(f'{out}/f{i:04d}.png')
