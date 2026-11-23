import sys,math
exec(open('/root/cap/lib212.py').read())
HY=notraf+"{const W9=window.__W();if(!window.__HY){const g=W9.makeCar(W9.CARS.find(c=>c.id=='hyper'));W9.scene.add(g);window.__HY=g;}W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__HY&&o!==window.__CT&&o!==window.__CP2&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});delete window.__HY.visible;window.__HY.visible=true;window.__lt=null;}"+HIDELIGHTS
NOWALK="{const W9=window.__W();W9.WALKERS.forEach(w=>{if(w.h&&!w.h.__hid){const p=w.h.position;if(p.z>540&&p.z<640&&!w.h.__hid){w.h.__hid=1;Object.defineProperty(w.h,'visible',{configurable:true,get:()=>false,set:()=>{}});}}});}"
def hline(x0,z,vx):
  ry=math.pi/2 if vx>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__HY;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x0,vx,z,ry,abs(vx))
def mk4(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=840,n=n,toff=o,wait=wait,js=NO+NOPLANE+HY+js); s["far"]=20000; return s
S={}
S["H1"]=hline(-68,-115.5,-24)+lk(("-95","0.6","-112.4"),("cx","cy+0.7","cz"),58)
S["H2"]=hline(275,560,-16)+lk(("cx+6-2*T","cy+1.0","548"),("cx-2","cy+2.2","570"),58)
S["H3"]=hline(118,593,-16)+lk(("cx+5-2.5*T","cy+1.3","578"),("cx-3","cy+3.2","604"),60)
S["H4"]=lk(("70-6*T","75","690"),("20","5","300"),58)
def hlinez(x,z0,vz):
  ry=0 if vz>0 else math.pi
  return ("const W7=window.__W();const g=window.__HY;const cx=%f,cz=%f+(%f)*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,vz,ry,abs(vz))
S["X1"]=hlinez(119.6,40,-20)+lk(("cx+6.5","cy+0.8","cz+2"),("cx","cy+1.0","cz-1.5"),58)
S["X2"]=hline(40,63.6,20)+lk(("cx-2","cy+0.8","cz+6.5"),("cx+1.5","cy+1.0","cz"),58)
S["X3"]=hline(112,598,-14)+lk(("70","3.2","579"),("70","4.6","604"),58)
S["X4"]=lk(("70-6*T","80","700"),("20","70","200"),58)

if __name__=="__main__" and True:
  mode=sys.argv[1]; sel=sys.argv[2].split(',')
  sh=[mk4("w",S[sel[0]],wait=2000,js=NOWALK)]
  for k in sel:
    if mode=='r':
      for t in (0,0.6,1.2): sh.append(mk4("%s_%02d"%(k,int(t*10)),S[k],o=t,js=NOWALK))
    else: sh.append(mk4("m4"+k,S[k],n=int(sys.argv[3]),wait=3000,js=NOWALK))
  run(sh,"/root/w/m4/"+mode,w=1080,h=1920,name="m4_"+mode+"".join(sel))
