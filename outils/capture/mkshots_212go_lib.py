import sys,math,json; sys.path.insert(0,'/root/cap'); from h import *
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
NO=CLOUD+open("/root/w/noufo.js").read()
HIDELIGHTS="{const W9=window.__W();let n=0;W9.scene.traverse(o=>{if(o.isPoints&&o.frustumCulled===false&&o.material&&Math.abs(o.material.size-2.6)<1e-6)n=o.geometry.attributes.position.count;});if(n)W9.scene.traverse(o=>{if(o.isPoints&&o.geometry.attributes.position.count===n&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
# cache la circulation (voitures userData.isCar, sauf la GT) et leurs phares, crée la GT orange une fois
GT=notraf+"{const W9=window.__W();if(!window.__GT){const g=W9.makeCar(W9.CARS.find(c=>c.id=='gt'));W9.scene.add(g);window.__GT=g;}W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__GT&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});window.__GT.visible=true;window.__lt=null;}"+HIDELIGHTS
def carline(x0,z,vx,ry):
  # GT en ligne droite le long de x (vitesse vx), y au sol, inclinaison suivant le relief
  return ("const W7=window.__W();const g=window.__GT;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x0,vx,z,ry,abs(vx))
def carring(cx,cz,R,a0,w):
  # GT sur un cercle de rayon R autour de (cx,cz), angle a0 + w*T (w>0 : sens trigo vu du dessus x->z)
  return ("const W7=window.__W();const g=window.__GT;const a=%f+(%f)*T;const x=%f+Math.cos(a)*%f,z=%f+Math.sin(a)*%f;const y=W7.GH(x,z);g.position.set(x,y,z);g.rotation.order='YXZ';"
          "const dx=-Math.sin(a)*Math.sign(%f),dz=Math.cos(a)*Math.sign(%f);g.rotation.y=Math.atan2(dx,dz);const C={x,y,z,fx:dx,fz:dz,rx:-dz,rz:dx};"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(a0,w,cx,R,cz,R,w,w,abs(w*R))
def mk(name,body,n=1,o=0,dt=840,js="",wait=2500):
  js=NOPLANE+js
  s=shot(name,body,dayT=dt,n=n,toff=o,wait=wait,js=NO+GT+js); s["far"]=20000; return s
def lk(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
NOPLANE="{const W9=window.__W();if(!window.__NOP){window.__NOP=1;let n=0;W9.scene.children.forEach(o=>{if(o.position.y>60&&o.position.y<500){let f=false;o.traverse(m=>{if(m.isMesh&&m.material&&m.material.fog===false)f=true;});if(f){n++;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}}});window.__NOPn=n;}}"
