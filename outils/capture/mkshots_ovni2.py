import sys; sys.path.insert(0,'/root/cap')
from ufo import *
import math
NOUFO=open('/root/cap/noufo.js').read()
CLOUD="if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
ARR=7.2
def mk(name,t0,body,n=1,w=1200):
  s=shot(name,body,dayT=840,n=n,wait=w,js=setup(t0),pre=PRE+CLOUD); s["far"]=20000; return s
G="const gy=W6.G.ufoRide?W6.G.ufoRide.gy:0;"
shots=[
 # B' : beam close, camera low 30 m
 mk("Bp1",5.6,G+"const a=2.25+0.30*T;return {p:[%f+30*Math.cos(a),gy+2.5,%f+30*Math.sin(a)],t:[%f,gy+14,%f],fov:62};"%(X,Z,X,Z)),
 mk("Bp2",5.6,G+"const a=2.25+0.30*T;return {p:[%f+24*Math.cos(a),gy+1.6,%f+24*Math.sin(a)],t:[%f,gy+13,%f],fov:70};"%(X,Z,X,Z)),
 # pilots
 mk("P1",ARR+18,"const h=W6.G.ufoRide.h||0,fx=Math.sin(h),fz=Math.cos(h);return {p:[M6.x+fx*6.5,M6.y+3.2,M6.z+fz*6.5],t:[M6.x,M6.y+1.8,M6.z],fov:45};"),
 mk("P2",ARR+18,"const h=W6.G.ufoRide.h||0,fx=Math.sin(h),fz=Math.cos(h),sx=fz,sz=-fx;return {p:[M6.x+fx*4.5+sx*3,M6.y+2.6,M6.z+fz*4.5+sz*3],t:[M6.x,M6.y+1.9,M6.z],fov:50};"),
 mk("P3",ARR+18,"const h=W6.G.ufoRide.h||0,fx=Math.sin(h),fz=Math.cos(h),sx=fz,sz=-fx;return {p:[M6.x-fx*5+sx*2,M6.y+3.0,M6.z-fz*5+sz*2],t:[M6.x+fx*2,M6.y+1.6,M6.z+fz*2],fov:50};"),
 # D3 lower over towers during descent
 mk("D3a",ARR+35.0,"return {p:[M6.x+22,M6.y-4,M6.z+26],t:[M6.x,M6.y-2,M6.z],fov:62};"),
 mk("D3b",ARR+34.0,"const a=0.8+0.3*T;return {p:[M6.x+40*Math.cos(a),M6.y+6,M6.z+40*Math.sin(a)],t:[M6.x,M6.y-8,M6.z],fov:62};"),
 # arrival : camera near player looking toward incoming saucer
 mk("Ar1",0.7,G+"const R=W6.G.ufoRide;return {p:[%f,gy+3,%f],t:[R.ax,gy+60,R.az],fov:60};"%(X,Z)),
 mk("Ar2",1.6,G+"const R=W6.G.ufoRide;return {p:[%f,gy+3,%f],t:[M6.x,M6.y,M6.z],fov:60};"%(X,Z)),
]
run(shots,'/root/w/r1')
# --- Plans finaux d'OVNI b2 (22/11, monteur) : voir fin_ovni*.py dans le commit · B4 image 1 (ride 5.5, cam 36→31 m, gy+8, cible gy+16.5, fov 62, rayon éteint à la 46e image), B4pre = même caméra T-0,5 s (boucle), PF3 pilotes de face (ARR+18.3, d 6.85-0.6T, y+3.3, cible y+2.6, fov 46), Ar2 arrivée (t0 0.36, caméra fixe à 80 % du trajet d'arrivée, décalée 12 m, regarde la soucoupe)
