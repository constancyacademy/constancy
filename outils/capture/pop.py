import sys,glob
from PIL import Image, ImageChops, ImageStat
import statistics as st
def frames_from(p):
  return sorted(glob.glob(p))
def check(fs,label):
  ims=[Image.open(f).convert('L').resize((216,384)) for f in fs]
  D=[]
  for i in range(1,len(ims)):
    d=ImageChops.difference(ims[i],ims[i-1]); cells=[]
    for gy in range(8):
      for gx in range(4):
        cells.append(ImageStat.Stat(d.crop((gx*54,gy*48,(gx+1)*54,(gy+1)*48))).mean[0])
    D.append(cells)
  flags=[]
  for i in range(len(D)):
    for c in range(32):
      nb=[D[j][c] for j in range(max(0,i-3),min(len(D),i+4)) if j!=i]
      m=st.median(nb) if nb else 0
      if D[i][c]>4 and D[i][c]>2.5*max(m,1): flags.append((i,i+1,c,round(D[i][c],1),round(m,1)))
  print(label,'transitions',len(D),'flags',flags[:40])
if __name__=='__main__':
  check(frames_from(sys.argv[1]),sys.argv[1])
