# rexfuite : le Rex suit la Hyper vers le portail du parc (coucher du soleil), positions posées à chaque image
import sys,os,json,time
sys.path.insert(0,'/root/cap'); exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","690"))
GX,GZ=-20.0,-2680.0
NX,NZ=float(os.environ.get("NX","0.044")),float(os.environ.get("NZ","0.999"))
HY=("{const W9=window.__W();if(!window.__HY){const g=W9.makeCar(W9.CARS.find(c=>c.id=='hyper'));W9.scene.add(g);window.__HY=g;}"
 "W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__HY&&!o.__hid&&!(W9.SHOWROOM&&W9.SHOWROOM.includes&&W9.SHOWROOM.includes(o))){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
 "delete window.__HY.visible;window.__HY.visible=true;window.__lt=null;window.__lt2=null;const d=W9.REX.d;d.esc=true;}")
def CHASE(s0,v,gap,a=0):
  # Rex à la distance s0 - v*T du portail sur l'axe (NX,NZ), Hyper « gap » m devant lui (côté portail)
  return ("const W7=window.__W();const nx=%f,nz=%f,gx=%f,gz=%f;const sr=%f-(%f*T+0.5*%f*T*T),sc=sr-%f,vv=%f+%f*T;"
          "const d=W7.REX.d,R=d.g;d.esc=true;R.visible=true;const rx=gx+nx*sr,rz=gz+nz*sr;R.position.set(rx,W7.GH(rx,rz)-0.15,rz);R.rotation.y=Math.atan2(-nx,-nz);"
          "if(window.__lt2!=null&&T>window.__lt2){W7.rexStep(d,(vv/6.5)/2.4*(T-window.__lt2));}window.__lt2=T;R.updateMatrixWorld(true);"
          "const g=window.__HY;const cx=gx+nx*sc,cz=gz+nz*sc,cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=Math.atan2(-nx,-nz);"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;const fx=-nx,fz=-nz,sx=-nz,sz=nx;const P={x:rx,y:W7.GH(rx,rz),z:rz};")%(NX,NZ,GX,GZ,s0,v,a,gap,v,a)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MK(name,body,n=1,o=0,js="",wait=3000):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+notraf+HY+js); s["far"]=20000; return s
S={}
def AX(s,side=0,h=0): return "(%f)+(%f)*(%s)+(%f)*(%s)"%(GX,NX,s,-NZ,side), str(h), "(%f)+(%f)*(%s)+(%f)*(%s)"%(GZ,NZ,s,NX,side)
def ax(s,side,h):
  x,_,z=AX(s,side); return (x,"W7.GH(%s,%s)+%s"%(x,z,h),z)
S["A3"]=CHASE(96,12,38)+L(ax(40,2.6,0.8),ax(92,0,13),64)
S["A4"]=CHASE(96,12,40)+L(ax(38,-2.4,0.7),ax(92,0,12),62)
S["B3"]=CHASE(100,12,26)+L(("cx+sx*32+fx*2","cy+2.0","cz+sz*32+fz*2"),("cx-fx*11","cy+8","cz-fz*11"),66)
S["B4"]=CHASE(100,12,26)+L(("cx-sx*32+fx*2","cy+2.0","cz-sz*32+fz*2"),("cx-fx*11","cy+8","cz-fz*11"),66)
S["C2"]=CHASE(62,10,30)+L(("P.x-fx*26-sx*10","P.y+26","P.z-fz*26-sz*10"),("cx+fx*14","cy+2","cz+fz*14"),60)
AIMF="""const W6=W7;const aim=(p,H,u,v,fov)=>{const tv=Math.tan(fov*Math.PI/360),th=tv*1080/1920;let d=new THREE.Vector3(H.x-p[0],H.y-p[1],H.z-p[2]).normalize();const r=new THREE.Vector3().crossVectors(d,new THREE.Vector3(0,1,0)).normalize();const uu=new THREE.Vector3().crossVectors(r,d);const x=2*u-1,y=1-2*v;const w=d.clone().addScaledVector(r,-x*th).addScaledVector(uu,-y*tv).normalize();return [p[0]+w.x*10,p[1]+w.y*10,p[2]+w.z*10];};
const bone=n=>{let b=null;W6.REX.d.g.traverse(o=>{if(o.isBone&&o.name===n)b=o;});b.updateWorldMatrix(true,false);return new THREE.Vector3().setFromMatrixPosition(b.matrixWorld);};"""
def AIM(pos,bn,u,v,fov):
  return AIMF+"const p=[%s,%s,%s];const H=bone('%s');return {p,t:aim(p,H,%s,%s,%s),fov:%s};"%(tuple(pos)+(bn,u,v,fov,fov))
def LT(i): return "{const W6=window.__W();if(!window.__LT){window.__LT=new THREE.PointLight(0xffe6f2,0,160,1.0);W6.scene.add(window.__LT);}window.__LT.intensity=%s;}"%i
def LC(body,dy=6): return body.replace("return {p,","window.__LT&&window.__LT.position.set(p[0],p[1]+%s,p[2]);return {p,"%dy)
S["A7"]=CHASE(108,12,46)+AIM(ax(40,2.6,0.8),"Head",0.5,0.38,66)
S["A8"]=CHASE(108,12,46)+LC(AIM(ax(40,2.6,0.8),"Head",0.5,0.38,66),10)
S["A9"]=CHASE(104,12,44)+LC(AIM(ax("40-3*T",-2.4,0.7),"Head",0.5,0.38,68),10)
_MK=MK
LJ={"A8":2.5,"A9":2.5}
def MK(name,body,n=1,o=0,js="",wait=3000):
  k=[x for x in LJ if S[x]==body]
  return _MK(name,body,n=n,o=o,js=js+LT(LJ[k[0]] if k else 0),wait=wait)
