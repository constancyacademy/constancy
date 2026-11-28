import sys,glob,numpy as np
from PIL import Image
d,nm=sys.argv[1],sys.argv[2]; fs=sorted(glob.glob(f"{d}/{nm}_*.png"))
st=int(sys.argv[3]) if len(sys.argv)>3 else 2
prev=None; out=[]
for f in fs[::st]:
  a=np.asarray(Image.open(f).convert('L').resize((216,384)),dtype=np.float32)
  if prev is not None: out.append(np.abs(a-prev).mean())
  prev=a
print(nm,"motion(30fps-eq) min %.1f mean %.1f max %.1f"%(min(out),np.mean(out),max(out)))
