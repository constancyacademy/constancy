import sys,glob,numpy as np
from PIL import Image
fs=sorted(glob.glob(sys.argv[1])); a0=int(sys.argv[2]) if len(sys.argv)>2 else 0
G=(12,20)
M=[];R=[]
for f in fs:
  im=np.asarray(Image.open(f).convert('RGB').resize((540,960)),dtype=np.float32)
  r,g,b=im[...,0],im[...,1],im[...,2]
  red=((r-np.maximum(g,b))>70).astype(np.float32)
  L=0.299*r+0.587*g+0.114*b
  h,w=L.shape; ch,cw=h//G[1],w//G[0]
  M.append(L.reshape(G[1],ch,G[0],cw).mean(axis=(1,3)))
  R.append(red.reshape(G[1],ch,G[0],cw).sum(axis=(1,3)))
M=np.array(M);R=np.array(R)
D=np.abs(np.diff(M,axis=0))
fl=[]
for i in range(len(D)):
  nb=[j for j in range(max(0,i-4),min(len(D),i+5)) if j!=i]
  med=np.median(D[nb],axis=0)
  z=(D[i]>10)&(D[i]>4*np.maximum(med,1.0))
  P=np.pad(R[i],1); NB=sum(P[1+dy:1+dy+G[1],1+dx:1+dx+G[0]] for dy in (-1,0,1) for dx in (-1,0,1))
  P2=np.pad(R[i+1],1); NB2=sum(P2[1+dy:1+dy+G[1],1+dx:1+dx+G[0]] for dy in (-1,0,1) for dx in (-1,0,1))
  zr=(R[i]<=2)&(R[i+1]>=15)&(NB<R[i+1]/2)
  for (y,x) in zip(*np.where(z|zr)): fl.append((i+a0,i+1+a0,int(x),int(y),round(float(D[i][y,x]),1),int(R[i][y,x]),int(R[i+1][y,x])))
print(len(fs),'images · flags:',fl[:60])
