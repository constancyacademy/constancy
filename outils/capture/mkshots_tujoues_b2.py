exec(open('/home/claude/rushes/outils/capture/mkshots_tujoues_b1.py').read())
# b2 (23/11 22h) : même simulation, nouvelles caméras · SUV entier en image 1 · poursuite d'1 s qui se décale · profil haut et loin (roues petites) · fin 3/4 face plus longue
SKY="return {p:[cx,300,cz],t:[cx,600,cz+1],fov:20};"
CAMS2=("if(T<1.45){const mx=0.72*cx+0.28*G7.me.x,mz=0.72*cz+0.28*G7.me.z;const a=-0.45-0.25*T;return {p:[mx+15.5*Math.sin(a),2.6,mz+15.5*Math.cos(a)],t:[mx,1.0,mz],fov:52};}"
 "if(T<2.3){"+SKY+"}"
 "if(T<4.0){return {p:[%f,0.6,%f],t:[cx,cy+0.8,cz],fov:56};}"
 "if(T<5.1){const k=(T-4.0)/1.1;const so=3.2-6.4*k;return {p:[cx-fx*6.5+sx*so,cy+1.2,cz-fz*6.5+sz*so],t:[cx+fx*8,cy+0.9,cz+fz*8],fov:60};}"
 "if(T<5.65){"+SKY+"}"
 "if(T<7.4){return {p:[cx+sx*10.5+fx*1.2,cy+2.0,cz+sz*10.5+fz*1.2],t:[cx+fx*1.2,cy+0.7,cz+fz*1.2],fov:50};}"
 "return {p:[cx+fx*10+sx*4,cy+1.5,cz+fz*10+sz*4],t:[cx+fx*2,cy+2.4,cz+fz*2],fov:56};")%(CX-14,CZ+4.2)
S["SIM2"]=SIM+CAMS2
_MKT=MK
def MK(name,body,n=1,o=0,js="",wait=2500):
  if "window.__PH" in body: js=INIT2+js
  return _MKT(name,body,n=n,o=o,js=js,wait=wait)
# plan de remplacement du profil (roues qui se déchirent de côté) : drone devant-dessus, roues petites, tour et terminaux
CAMS3=("if(T<5.6||T>7.5){"+SKY+"}"
 "return {p:[cx+fx*13-sx*7,cy+10,cz+fz*13-sz*7],t:[cx+fx*1.5,cy+0.4,cz+fz*1.5],fov:55};")
S["SIM3"]=SIM+CAMS3
CAMS4=("if(T<5.6||T>7.5){"+SKY+"}"
 "return {p:[cx-fx*9+sx*6,cy+6.5,cz-fz*9+sz*6],t:[cx+fx*14-sx*4,cy+1.5,cz+fz*14-sz*4],fov:58};")
S["SIM4"]=SIM+CAMS4
CAMS5=("if(T<5.6||T>7.5){"+SKY+"}"
 "return {p:[cx-fx*7+sx*2.5,cy+4.5,cz-fz*7+sz*2.5],t:[cx+fx*12+sx*0.5,cy+0.3,cz+fz*12+sz*0.5],fov:60};")
S["SIM5"]=SIM+CAMS5
CAMS6=("if(T<5.6){"+SKY+"}"
 "return {p:[cx+fx*10+sx*4,cy+1.5,cz+fz*10+sz*4],t:[cx+fx*2,cy+2.4,cz+fz*2],fov:56};")
S["SIM6"]=SIM+CAMS6
# b3 (24/11 0h50) · roues du SUV figées (la roue tourne avec des éclats de l'aile : passages de roue qui se déchirent) · drone 3/4 arrière · fin avec le SUV sous le bouton
FIXW="{const W8=window.__W();const cm=W8.carMesh;if(cm)cm.traverse(o=>{if(/wheel/i.test(o.name||'')){o.rotation.x=0;}});if(G7.parked&&G7.parked.mesh)G7.parked.mesh.traverse(o=>{if(/wheel/i.test(o.name||'')){o.rotation.x=0;}});}"
CAMS7=("if(T<1.45){const mx=0.72*cx+0.28*G7.me.x,mz=0.72*cz+0.28*G7.me.z;const a=-0.45-0.25*T;return {p:[mx+15.5*Math.sin(a),2.6,mz+15.5*Math.cos(a)],t:[mx,1.0,mz],fov:52};}"
 "if(T<2.4){"+SKY+"}"
 "if(T<5.0){return {p:[cx-fx*13+sx*6,cy+9,cz-fz*13+sz*6],t:[cx+fx*7,cy+0.5,cz+fz*7],fov:55};}"
 "if(T<5.6){"+SKY+"}"
 "return {p:[cx+fx*11-sx*4,cy+3.2,cz+fz*11-sz*4],t:[cx+fx*1,cy+4.3,cz+fz*1],fov:56};")
S["SIM7"]=SIM+FIXW+CAMS7
CAMS8=("if(T<2.3||T>4.75){"+SKY+"}"
 "return {p:[cx-fx*13+sx*6,cy+9,cz-fz*13+sz*6],t:[cx-fx*3.5+sx*0.8,cy-1.5,cz-fz*3.5+sz*0.8],fov:55};")
S["SIM8"]=SIM+FIXW+CAMS8
CAMS9=("if(T<2.3||T>4.75){"+SKY+"}"
 "return {p:[cx-fx*13+sx*6,cy+9,cz-fz*13+sz*6],t:[cx+fx*1.8+sx*0.3,cy-0.4,cz+fz*1.8+sz*0.3],fov:55};")
S["SIM9"]=SIM+FIXW+CAMS9
