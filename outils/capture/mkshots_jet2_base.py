import sys,json; sys.path.insert(0,'/root/cap'); from h import *
JET=open('/root/w/jet_js.txt').read(); NOU=open('/root/w/noufo.js').read()
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
def J(name,body,n=1,toff=0,w=1500):
  s=shot(name,body,dayT=840,n=n,toff=toff,wait=w,js=JET+CLOUD+NOU); s["far"]=20000; return s
PINS="const J=window.__JET;J.visible=true;const z=-1440-80*T;J.position.set(-1160,72,z);J.rotation.set(0,Math.PI,0);J.rotation.z=-0.25;return {p:[-1160+16,78,z+26],t:[-1160,70,z-10],fov:60};"
shots=[J("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"),
 J("pins0",PINS,w=9000), J("pins1",PINS,toff=0.7,w=3000), J("pins2",PINS,toff=1.4,w=3000),
 J("m1","return {p:[-180,160,-1400],t:[-180,130,-1750],fov:60};"),
 J("m2","return {p:[-60,140,-1450],t:[-150,120,-1750],fov:60};"),
 J("m3","return {p:[-300,140,-1450],t:[-180,120,-1750],fov:60};"),
 J("m4","return {p:[100,120,-1500],t:[-120,110,-1750],fov:60};"),
]
run(shots,'/root/w/j1')
