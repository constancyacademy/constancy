import sys,math
sys.argv_saved=sys.argv
exec(open('/root/cap/lib212.py').read().replace('from h import *','from h import *'))
def carpath(x0,z0,ux,uz,v):
  L=math.hypot(ux,uz); ux/=L; uz/=L
  return ("const W7=window.__W();const g=window.__GT;const cx=%f+%f*%f*T,cz=%f+%f*%f*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;const U={x:%f,z:%f};")%(x0,ux,v,z0,uz,v,math.atan2(ux,uz),abs(v),ux,uz)
C0=(-1500,330)
# fronde 0
fx0,fz0,fx1,fz1=-1455,425,-1300,755
L=math.hypot(fx1-fx0,fz1-fz0); ux,uz=(fx1-fx0)/L,(fz1-fz0)/L
nx,nz=-uz,ux   # normale (b>0)
S={}
S["P1"]=(52,carline(-70,-52.4,24,math.pi/2)+lk(("cx-3.0+0.0*T","cy+0.75","-61.5"),("cx+0.5","cy+0.9","cz"),58))
a0=30; px,pz=fx0+ux*a0,fz0+uz*a0
S["P4"]=(52,carpath(px,pz,ux,uz,22)+lk(("cx-U.x*2.5+(%f)*7.5"%nx,"cy+0.7","cz-U.z*2.5+(%f)*7.5"%nz),("cx+U.x*1.5","cy+0.9","cz+U.z*1.5"),60))
S["P5"]=(52,carring(C0[0],C0[1],90,2.0,0.33)+lk(("C.x+Math.cos(2.0+0.33*T)*38-C.fx*20","C.y+58","C.z+Math.sin(2.0+0.33*T)*38-C.fz*20"),("-1500","0","330"),50))
if __name__=="__main__":
  mode=sys.argv[1]; sel=sys.argv[2].split(',')
  sh=[mk("w",S[sel[0]][1],wait=2000)]
  for k in sel:
    n,b=S[k]
    if mode=='r':
      for t in (0,0.85,1.7): sh.append(mk("%s_%02d"%(k,int(t*10)),b,o=t))
    else: sh.append(mk("m2"+k,b,n=int(sys.argv[3]) if len(sys.argv)>3 else n,wait=3000))
  run(sh,"/root/w/m2/"+("r" if mode=='r' else "full"),w=1080,h=960,name="m2b2_"+mode+"".join(sel))
