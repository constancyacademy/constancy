# nuit2h_b1 (sam. 28/11 21h, M4 NUIT POV « POV : 2 h du mat, tu roules encore. ») · Hyper Gold de nuit : rue du club (voie -x z = -115,5), puis x = -171,6 vers +z avec les faisceaux du stade des Constancy Stars dans le ciel
import os
exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","900"))
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}}}"
HY=("{const W9=window.__W();if(!window.__HY){const g=W9.makeCar(W9.CARS.find(c=>c.id=='hyper'));W9.scene.add(g);window.__HY=g;}"
 "W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__HY&&!o.__hid&&!(W9.SHOWROOM&&W9.SHOWROOM.includes&&W9.SHOWROOM.includes(o))){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
 "delete window.__HY.visible;window.__HY.visible=true;window.__lt=null;}")
def CARX(x0,z,v,a=0,dirx=-1):
  # Hyper le long de x (sens dirx), vitesse v + accélération a
  return ("const W7=window.__W();const g=window.__HY;const d=%f*T+0.5*%f*T*T,vv=%f+%f*T;const cx=%f+(%d)*d,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;const fx=%d,fz=0;")%(v,a,v,a,x0,dirx,z,(-1.5708 if dirx<0 else 1.5708),dirx)
def CARZ(x,z0,v,a=0):
  return ("const W7=window.__W();const g=window.__HY;const d=%f*T+0.5*%f*T*T,vv=%f+%f*T;const cx=%f,cz=%f+d;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=0;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;const fx=0,fz=1;")%(v,a,v,a,x,z0)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MKN(name,body,n=1,o=0,js="",wait=3000):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+HY+notraf+HIDELIGHTS+js); s["far"]=8000; return s
S={}
# N1 : au ras du bitume derrière la Hyper qui file sur la rue du club, la caméra la rattrape (recul 9 → 4,5 m)
S["N1"]=CARX(-20,-115.5,20,3)+L(("cx+Math.max(4.5,9-2.2*T)","cy+0.45","cz+0.3"),("cx-30","cy+0.9","cz-0.4"),62)
S["N1b"]=CARX(-20,-115.5,20,3)+L(("cx+Math.max(4.2,8-2*T)","cy+0.6","cz+1.6"),("cx-30","cy+1.2","cz-1.5"),64)
# N2 : travelling de côté, la Hyper devant l'enseigne du Constancy Club et la file
S["N2"]=CARX(-60,-115.5,18)+L(("cx+1.5","cy+1.1","-108.6"),("cx-1","cy+1.6","-124"),56)
S["N2b"]=CARX(-60,-115.5,18)+L(("cx-3","cy+0.7","-109.5"),("cx+2","cy+1.8","-125"),58)
# N3 : x = -171,6 vers +z (vers le stade), caméra derrière qui monte et lève les yeux vers les faisceaux
S["N3"]=CARZ(-171.6,120,18)+"const u=Math.min(1,T/3.2),e=u*u*(3-2*u);"+L(("cx+0.2","cy+0.5+5.5*e","cz-6-3*e"),("cx","cy+0.8+120*e","cz+40+260*e"),64)
S["N3b"]=CARZ(-171.6,120,18)+"const u=Math.min(1,T/3.2),e=u*u*(3-2*u);"+L(("cx+1.2","cy+0.5+3*e","cz-5.5-2*e"),("cx-0.5","cy+0.9+80*e","cz+40+200*e"),66)
def MK(name,body,n=1,o=0,js="",wait=3000): return MKN(name,body,n,o,js,wait)
NEAR=""
S["N3f"]=CARZ(-171.6,120,18)+"const u=Math.min(1,T/4.0),e=u*u*(3-2*u);"+L(("cx+0.6","cy+0.8+2.2*e","cz-7-1.5*e"),("cx-0.2","cy+1.0+14*e","cz+60"),64)
