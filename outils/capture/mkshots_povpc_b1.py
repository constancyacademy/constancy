import sys,math
exec(open('/root/cap/lib212.py').read())
HY=notraf+"{const W9=window.__W();if(!window.__HY){const g=W9.makeCar(W9.CARS.find(c=>c.id=='hyper'));W9.scene.add(g);window.__HY=g;}W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__HY&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});delete window.__HY.visible;window.__HY.visible=true;window.__lt=null;}"+HIDELIGHTS
NOWALK="{const W9=window.__W();(W9.WALKERS||[]).forEach(w=>{if(w.h&&!w.h.__hid){const p=w.h.position;if(p.z>540&&p.z<640){w.h.__hid=1;Object.defineProperty(w.h,'visible',{configurable:true,get:()=>false,set:()=>{}});}}});}"
def hline(x0,z,vx):
  ry=math.pi/2 if vx>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__HY;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x0,vx,z,ry,abs(vx))
def hlinez(x,z0,vz):
  ry=0 if vz>0 else math.pi
  return ("const W7=window.__W();const g=window.__HY;const cx=%f,cz=%f+(%f)*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,vz,ry,abs(vz))
PARK="const g=window.__HY;g.position.set(0,-50,0);"
def mk4(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=840,n=n,toff=o,wait=wait,js=NO+NOPLANE+HY+NOWALK+js); s["far"]=20000; return s
S={}
# image 1 candidates
S["A"]=hline(-83,-115.5,-24)+lk(("-95","0.6","-112.4"),("cx","cy+0.7","cz"),58)
S["B"]=hlinez(119.6,32,-24)+lk(("122.8","0.6","20"),("cx","cy+0.7","cz"),58)
S["C"]=hline(48,63.6,24)+lk(("60","0.6","60.4"),("cx","cy+0.7","cz"),58)
# side travelling
CAMF="const s=Math.max(0,T-0.95);const cmx=-95-(s<0.3?18*s*s/0.6:18*(s-0.15));"
S["A2"]=hline(-71,-115.5,-24)+CAMF+lk(("cmx","1.15","-112.6"),("cx","cy+1.0","cz"),60)
S["A3"]=hline(-36,-115.5,-24)+"const s=Math.max(0,T-0.95);const cmx=-60-(s<0.3?18*s*s/0.6:18*(s-0.15));"+lk(("cmx","1.15","-112.6"),("cx","cy+1.0","cz"),60)
S["X2b"]=hline(40,63.6,20)+lk(("cx-1.5","cy+1.7","cz+5.5"),("cx+1.0","cy+0.9","cz"),60)
S["LA"]=hline(112,578,-20)+lk(("10","1.8","548"),("70","5.5","604"),58)
S["O3"]=PARK+lk(("70-10*T","80-4*T","700-25*T"),("20","72","200"),58)
S["LW"]=PARK+lk(("10","1.8","548"),("70","5.5","604"),100)
S["LW2"]=PARK+lk(("-40","3","520"),("70","6","604"),70)
S["O4"]=PARK+lk(("70-10*T","70-3*T","700-25*T"),("20","84","200"),58)
S["LT"]=hline(17,565,12)+lk(("cx-14","1.8","551"),("cx-14+82*0.682","6","551+82*0.731"),64)
S["CH"]=hlinez(119.6,60,-20)+lk(("cx+1.2","cy+2.6","cz+7.5"),("cx-1.5","cy+0.6","cz-8"),60)
S["LC"]=hlinez(70,500,18)+lk(("cx+1.0","cy+2.2","cz-7.5"),("cx+0.5","4.5","cz+60"),70)
S["DC"]=hline(-60,-115.5,-24)+lk(("cx+9","cy+8","cz+2.5"),("cx-7","cy+0.5","cz"),60)
S["O5"]=PARK+lk(("70-14*T","72-4*T","700-35*T"),("20","84","200"),58)
S["O6"]=PARK+lk(("90-30*T","72-6*T","700-75*T"),("20+20*T","84","200"),58)
S["LD"]=hlinez(70,500,26)+lk(("71","2.0+2.0*T","494.5+8*T"),("70.5","4.5+1.2*T","554.5+8*T"),70)
S["LS"]=hline(40,580,40)+lk(("cx-1","2.2","569"),("cx-1","5.0","604"),58)
HIDEPPL="{const W9=window.__W();const v=new THREE.Vector3();const L=[];const A=(a,f)=>{(a||[]).forEach(e=>{const m=f?f(e):e;if(m&&m.isObject3D)L.push(m);});};const B=W9.BEACH||{};A(B.walk,e=>e.h);A(B.swim,e=>e.h);A(B.night);A((W9.life||{}).beach,e=>e.mesh);A((W9.life||{}).dogs,e=>e.mesh);A((W9.GUING||{}).people);A((W9.FIRES||{}).people);A(W9.peds,e=>e.mesh);A(W9.WALKERS,e=>e.h);L.forEach(m=>{if(m.__hid)return;m.getWorldPosition(v);if(v.x>-40&&v.x<160&&v.z>530&&v.z<650){m.__hid=1;Object.defineProperty(m,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
S["LS2"]=HIDEPPL+hline(102,580,-40)+lk(("cx+1","3.2","568"),("cx+1","3.2","604"),60)
HIDESMALL="{const W9=window.__W();if(!window.__HS){window.__HS=1;const b=new THREE.Box3(),c=new THREE.Vector3(),z=new THREE.Vector3();const ex=new Set();window.__HY.traverse(o=>ex.add(o));const L=[];W9.scene.traverse(o=>{if((o.isMesh||o.isSkinnedMesh)&&!o.isInstancedMesh&&!ex.has(o))L.push(o);});L.forEach(o=>{b.setFromObject(o);if(b.isEmpty())return;b.getCenter(c);b.getSize(z);if(c.x>30&&c.x<125&&c.z>550&&c.z<600&&c.y<3.5&&Math.max(z.x,z.y,z.z)<3.2){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
S["LS3"]=HIDEPPL+HIDESMALL+hline(102,580,-40)+lk(("cx+1","3.2","568"),("cx+1","3.2","604"),60)
S["LS4"]=HIDEPPL+hline(102,580,-40)+lk(("cx+1","6.5","567"),("cx+1","4.0","604"),60)
S["LS5"]=HIDEPPL+hline(108,566,-40)+lk(("cx+1","3.2","553"),("cx+1","3.2","604"),60)
S["DC2"]=hline(-48,-115.5,-24)+lk(("cx+9","cy+8","cz+2.5"),("cx-7","cy+0.5","cz"),60)
S["DC4"]=hline(-60,-115.5,-24)+lk(("cx+9","cy+8","cz+2.5"),("cx-4","cy+0.3","cz"),60)
S["X2"]=hline(40,63.6,20)+lk(("cx-2","cy+0.8","cz+6.5"),("cx+1.5","cy+1.0","cz"),58)
S["X1"]=hlinez(119.6,40,-20)+lk(("cx+6.5","cy+0.8","cz+2"),("cx","cy+1.0","cz-1.5"),58)
# letters
S["L1"]=hline(112,598,-14)+lk(("30","3","560"),("72","4.2","604"),58)
S["L2"]=hline(118,593,-16)+lk(("cx+5-2.5*T","cy+1.3","578"),("cx-3","cy+3.2","604"),60)
S["L3"]=PARK+lk(("70","3.2","579"),("70","4.6","604"),58)
# overview
S["O1"]=PARK+lk(("70-6*T","80","700"),("20","60","200"),58)
S["O2"]=PARK+lk(("70-6*T","95","760"),("20","55","150"),55)
if __name__=="__main__":
  mode=sys.argv[1]; sel=sys.argv[2].split(',')
  sh=[mk4("w",S[sel[0]],wait=2000)]
  for k in sel:
    if mode=='r':
      for t in [float(x) for x in (sys.argv[3] if len(sys.argv)>3 else "0,0.4,0.8").split(',')]: sh.append(mk4("%s_%02d"%(k,int(round(t*10))),S[k],o=t))
    else: sh.append(mk4("m4"+k,S[k],n=int(sys.argv[3]),o=float(sys.argv[4]) if len(sys.argv)>4 else 0,wait=int(__import__("os").environ.get("WAIT","3000"))))
  run(sh,"/root/w/m4/"+mode,w=1080,h=1920,name="m4_"+mode+"".join(sel)+sys.argv[-1].replace(",","").replace(".",""),wait=False)
