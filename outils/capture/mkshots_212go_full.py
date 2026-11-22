from lib import *
import math,sys
C0=(-1500,330)
S={}
S["B1"]=(66,carline(-1230,328,-30,-math.pi/2)+lk(("cx+8.5-1.2*T","cy+2.0","cz+1.6-0.6*T"),("cx-20","cy+1.5","cz"),62))
S["B2"]=(66,carline(-1300,326,-30,-math.pi/2)+lk(("cx-1.0+1.4*T","cy+1.1","cz-7.0"),("cx-1.0+1.4*T","cy+0.9","cz"),54))
S["B3"]=(66,carring(C0[0],C0[1],90,3.0,0.33)+lk(("C.x-C.fx*7.5-C.rx*3","C.y+1.1","C.z-C.fz*7.5-C.rz*3"),("C.x+C.fx*14","C.y+1.4","C.z+C.fz*14"),62))
S["B4"]=(66,carring(C0[0],C0[1],90,2.0,0.33)+lk(("C.x+Math.cos(2.0+0.33*T)*38-C.fx*20","C.y+46","C.z+Math.sin(2.0+0.33*T)*38-C.fz*20"),("C.x*0.55+(-1500)*0.45","0","C.z*0.55+330*0.45"),60))
mode=sys.argv[1]; sel=sys.argv[2].split(',')
sh=[mk("w",S[sel[0]][1],wait=2000)]
for k in sel:
  n,b=S[k]
  if mode=='r':
    for t in (0,0.7,1.4,2.1): sh.append(mk("%s_%02d"%(k,int(t*10)),b,o=t))
  else: sh.append(mk("m2"+k,b,n=n,wait=3000))
run(sh,"/root/w/m2/"+("r4" if mode=='r' else "full"),w=540 if mode=='r' else 1080,h=480 if mode=='r' else 960,name="l_m2_"+mode+str(len(sel))+sel[0])
