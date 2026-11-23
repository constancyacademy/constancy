# python3 tk.py name "Accroche."  -> /root/w/tk/tiktok_cover_<name>.png (2160x2880, gabarit tiktok_cover_vrai3d_b3)
import sys; sys.path.insert(0,'/root/monteur/cov')
import os; os.chdir('/root/monteur/cov')
exec(open('make.py').read().split("if __name__")[0])
from cover import render,bbox_rows
import numpy as np
name,text=sys.argv[1],sys.argv[2]
L=lines_for(text)
def mk(cy,by):
  return render(L,W=2160,H=2880,size=156,lh=1.185,cy=cy,bsize=64,brand_y=by)
cy,by=1440.0,2621.0
for it in range(3):
  im=mk(cy,by); rows=bbox_rows(im)
  txt=rows[:-1]; br=rows[-1]
  ic=(txt[0][0]+txt[-1][1])/2; cy+=1440-ic
  bc=(br[0]+br[1])/2; by+=2621-bc
im=mk(cy,by); rows=bbox_rows(im)
out='/root/w/tk/tiktok_cover_%s.png'%name; im.save(out); print(out,L,rows)
