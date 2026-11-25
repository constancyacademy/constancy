# voile de fumée de l'escalier (copie du fireSmokeVeil du jeu : radial-gradient(circle at 50% 60%, rgba(255,110,30,.25), rgba(15,12,12,.95) 70%))
import sys,glob,numpy as np,math
from PIL import Image
fs=sorted(glob.glob(sys.argv[1])); out=sys.argv[2]
W,H=1080,1920; yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
r=np.sqrt((xx-0.5*W)**2+(yy-0.6*H)**2)/ (0.5*math.hypot(W,H)) # 'circle' farthest-corner ~ demi-diagonale
u=np.clip(r/0.70,0,1)[...,None]
c0=np.array([255,110,30],np.float32); c1=np.array([15,12,12],np.float32)
col=c0*(1-u)+c1*u; al=0.25*(1-u)+0.95*u
n=len(fs)
for i,f in enumerate(fs):
  t=i/60.; k=min(1,0.35+0.55*i/max(1,n-1)); k*=0.9+0.1*math.sin(t*9)
  a=al*k
  im=np.asarray(Image.open(f).convert('RGB')).astype(np.float32)
  o=im*(1-a)+col*a
  Image.fromarray(np.clip(o,0,255).astype(np.uint8)).save(f"{out}/v_{i:03d}.png")
print(n)
