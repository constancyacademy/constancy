import sys,json; sys.path.insert(0,'/root/cap'); from h import *
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
def S(name,body,dt=1140,n=1,toff=0,w=1500):
  s=shot(name,body,dayT=dt,n=n,toff=toff,wait=w,js=CLOUD); s["far"]=20000; return s
def orb(name,cx,cy,cz,r,h,a0,da,ty=1.2,fov=60,toff=0):
  return S(name,"const a=%f+%f*T;return {p:[%f+%f*Math.cos(a),%f,%f+%f*Math.sin(a)],t:[%f,%f,%f],fov:%f};"%(a0,da,cx,r,cy+h,cz,r,cx,cy+ty,cz,fov),toff=toff)
shots=[S("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"),
 S("A_dive0","return {p:[84+45-25*T,69+40-24*T,28+45-25*T],t:[84,70,28],fov:60};"),
 S("A_dive1","return {p:[84+45-25*T,69+40-24*T,28+45-25*T],t:[84,70,28],fov:60};",toff=1.2),
 orb("A_orb",84,69,28,16,4,0.6,0.25),
 orb("B_orb",132,17,188,12,3.5,0.4,0.25),
 orb("C_orb",-35,24,-203,12,3.5,2.2,0.25),
 orb("D_orb",-188,24,-76,12,3.5,0.8,0.25),
 orb("E_orb",140,19,-244,12,3.5,1.5,0.25),
 orb("K_car",-578,2.6,-32,13,2.2,1.0,0.3,ty=2.5,fov=62),
 orb("K_car2",-578,2.6,-32,13,2.2,2.6,0.3,ty=2.5,fov=62),
]
run(shots,'/root/w/n3')
