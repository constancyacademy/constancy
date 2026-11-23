exec(open('/home/claude/rushes/outils/capture/mkshots_povtemps_b1.py').read())
# b2 (23/11 21h30) : Concession vue de l'intérieur, sans pilier ni coupé blanc au premier plan · drone plus haut (voiture dans le tiers bas)
S["C1"]=PARK+L(("136+5*T","1.5","-95.5"),("142+5*T","2.2","-84"),55)
S["C2"]=PARK+L(("133+3*T","1.2","-94"),("141","2.6","-86"),50)
S["C3"]=PARK+L(("146-5*T","1.4","-95.5"),("138-3*T","2.4","-85"),55)
S["C4"]=PARK+L(("140+4*T","1.6","-93"),("140+2*T","2.4","-80"),60)
def orb(a0,da,R,h,ty,tx=140,tz=-86.4,fov=58): return PARK+"const a=%f+%f*T;return {p:[%f+%f*Math.sin(a),%f,%f-%f*Math.cos(a)],t:[%f,%f,%f],fov:%f};"%(a0,da,tx,R,h,tz,R,tx,ty,tz,fov)
S["O1"]=orb(-0.6,0.3,7.5,3.0,3.0)
S["O2"]=orb(0.5,-0.3,7.5,3.2,2.9)
S["O3"]=orb(-0.2,0.25,9,2.4,3.0,fov=55)
S["O4"]=orb(-0.5,0.3,6,7,2.6,fov=60)
S["O5"]=orb(-0.3,0.3,8,5,2.8,fov=58)
S["O6"]=orb(2.7,0.3,8,5,2.8,fov=58)
S["O7"]=orb(-0.35,0.3,7.5,6,2.5,fov=60)
S["P6"]=cz_line(LX,320,-24)+L(("cx-7","cy+6","cz+7"),("cx","cy+0.3","cz-9"),60)
S["P7"]=cz_line(LX,320,-24)+L(("cx-8","cy+8","cz+8"),("cx-1","cy","cz-12"),62)
S["O8"]=orb(-0.35,0.3,6.5,8,2.2,fov=60)
S["P8"]=cz_line(LX,320,-24)+L(("cx-7","cy+6","cz+7"),("cx+10.5","cy","cz-10.5"),62)
# b3 (24/11 0h45) : Constancy City en 3/4 avant serré, la caméra tourne AVEC le plateau (fond qui défile), rien sous le bouton
NAC="const W7=window.__W();const NC=W7.SHOWROOM.find(g=>g.userData.carId==='nacre');const ry=NC.rotation.y;"
def k34(off,R,h,ty,fov=55): return PARK+NAC+"const a=ry+%f;return {p:[140+%f*Math.sin(a),%f,-86.4+%f*Math.cos(a)],t:[140,%f,-86.4],fov:%f};"%(off,R,h,R,ty,fov)
S["K1"]=k34(0.6,6.0,3.9,3.0)
S["K2"]=k34(-0.6,6.0,3.9,3.0)
S["K3"]=k34(0.5,5.2,4.4,2.8,58)
NAC="const W7=window.__W();const NC=W7.SHOWROOM.find(g=>Math.abs(g.position.x-140)<1&&g.position.y>2)||W7.SHOWROOM[6];const ry=NC.rotation.y;"
S["K1"]=k34(0.6,6.0,3.9,3.0)
S["K2"]=k34(-0.6,6.0,3.9,3.0)
S["K3"]=k34(0.5,5.2,4.4,2.8,58)
NACH="{const W6=window.__W();const NC=W6.SHOWROOM.find(g=>Math.abs(g.position.x-140)<1&&g.position.y>2)||W6.SHOWROOM[6];const u=NC.userData.nacre;if(u&&!u.__h){u.__h=1;['pool','beams','halo','haloS','under'].forEach(k=>{let a=u[k];(Array.isArray(a)?a:[a]).forEach(o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});});});}}"
S["K4"]=NACH+k34(0.55,7.0,4.8,2.9,55)
S["K5"]=NACH+k34(0.55,7.6,5.6,1.5,56)
HIDECO="{const W9=window.__W();const v=new THREE.Vector3();const L=[];const A=(a,f)=>{(a||[]).forEach(e=>{const m=f?f(e):e;if(m&&m.isObject3D)L.push(m);});};A(W9.peds,e=>e.mesh);A(W9.WALKERS,e=>e.h);A((W9.life||{}).peds,e=>e.mesh);W9.scene.traverse(o=>{if(o.userData&&(o.userData.rig||o.userData.human||o.userData.ped))L.push(o);});L.forEach(m=>{if(m.__hid)return;m.getWorldPosition(v);if(v.x>112&&v.x<168&&v.z>-112&&v.z<-58){m.__hid=1;Object.defineProperty(m,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
S["K6"]=HIDECO+S["K5"]
