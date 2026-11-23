# POV PC b3 (24/11 21h) : corrections du jugement du 23/11 7h20
import sys,math,os
exec(open('/root/cap/lib212.py').read())
CARID=os.environ.get("CARID","hyper")
CPN=notraf+"{const W9=window.__W();if(!window.__CPN||window.__CPNid!='%s'){if(window.__CPN)W9.scene.remove(window.__CPN);const g=W9.makeCar(W9.CARS.find(c=>c.id=='%s'));if(g.userData&&g.userData.nacre){g.userData.nacre.em=[];if(window.__NOPOOL){(window.__NOPOOLK||['pool']).forEach(k=>{let P=g.userData.nacre[k];(Array.isArray(P)?P:[P]).forEach(q=>{if(q&&q.isObject3D)Object.defineProperty(q,'visible',{configurable:true,get:()=>false,set:()=>{}});});});}}W9.scene.add(g);window.__CPN=g;window.__CPNid='%s';}W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__CPN&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});delete window.__CPN.visible;window.__CPN.visible=true;window.__lt=null;}"%(CARID,CARID,CARID)+HIDELIGHTS
HIDEPPL="{const W9=window.__W();const v=new THREE.Vector3();const L=[];const A=(a,f)=>{(a||[]).forEach(e=>{const m=f?f(e):e;if(m&&m.isObject3D)L.push(m);});};const B=W9.BEACH||{};A(B.walk,e=>e.h);A(B.swim,e=>e.h);A(B.night);A((W9.life||{}).beach,e=>e.mesh);A((W9.life||{}).dogs,e=>e.mesh);A((W9.GUING||{}).people);A((W9.FIRES||{}).people);A(W9.peds,e=>e.mesh);A(W9.WALKERS,e=>e.h);L.forEach(m=>{if(m.__hid)return;m.getWorldPosition(v);if((v.x>-40&&v.x<160&&v.z>530&&v.z<650)||(v.x>380&&v.x<620&&v.z>-20&&v.z<200)){m.__hid=1;Object.defineProperty(m,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
UNFPV="{const W7=window.__W();W7.G.onFoot=true;W7.G.ride={kind:'none'};W7.G.fpv=false;W7.BUEE.k=0;}"
# point sur la rampe de l'A10 a la distance d (m), voie de droite (off), renvoie C={x,y,z,dx,dz,sl}
DKF=("const W7=window.__W();const S=(window.__A10S=window.__A10S||W7.DK.decks.find(q=>q.name.indexOf('A10')>=0).S);"
     "const at=(d,off)=>{let i=0;while(i<S.length-2&&S[i+1][3]<d)i++;const a=S[i],b=S[i+1];const t=Math.max(-2,Math.min(3,(d-a[3])/(b[3]-a[3])));"
     "let dx=b[0]-a[0],dz=b[1]-a[1];const l=Math.hypot(dx,dz);dx/=l;dz/=l;const x=a[0]+(b[0]-a[0])*t-dz*off,z=a[1]+(b[1]-a[1])*t+dx*off,y=a[2]+(b[2]-a[2])*t;return {x,y,z,dx,dz,sl:(b[2]-a[2])/l};};")
def car_a10(d0,v,off=3.0,sgn=1):
  # sgn=1 : monte (vers +d), sgn=-1 : descend
  return DKF+("const g=window.__CPN;const C=at(%f+(%f)*T,%f);const cx=C.x,cy=C.y,cz=C.z;g.position.set(cx,cy,cz);g.rotation.order='YXZ';"
     "g.rotation.y=Math.atan2(%d*C.dx,%d*C.dz);g.rotation.x=-Math.atan(%d*C.sl);"
     "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(d0,sgn*v,sgn*off,sgn,sgn,sgn,abs(v))
PARK="const g=window.__CPN;g.position.set(0,-50,0);"
def mk5(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=840,n=n,toff=o,wait=wait,js=UNFPV+NO+NOPLANE+("window.__NOPOOL=1;window.__NOPOOLK="+os.environ.get('NPK','["pool"]')+";window.__CPN&&window.__CPNid=='nacre'&&(window.__CPNid='x');" if os.environ.get("NOPOOL") else "")+CPN+HIDEPPL+js,pre=UNFPV); s["far"]=20000; return s
S={}
# camera sur la rampe, devant, regard vers la ville (la voiture monte vers la camera)
S["R1"]=car_a10(2,24)+"const K=at(62,1.2);"+lk(("K.x","K.y+0.7","K.z"),("cx","cy+0.7","cz"),58)
# camera au pied de la rampe, regard vers le haut de la rampe
S["R5"]=car_a10(40,24)+"const K=at(64,0.6);"+lk(("K.x","K.y+0.7","K.z"),("cx","cy+0.6","cz"),58)
S["R2"]=car_a10(2,24)+"const K=at(-6,-1.5);"+lk(("K.x","K.y+0.8","K.z"),("cx","cy+0.7","cz"),58)
# vue large de la rampe la nuit depuis le cote
S["R3"]=car_a10(30,0)+lk(("470","3","100"),("505","4","80"),60)
S["R4"]=car_a10(30,0)+lk(("520","2","40"),("500","3","80"),60)

# image 1 : camera qui recule sur la rampe devant la voiture, ville eclairee derriere
S["T1"]=car_a10(30,22)+"const K=at(39+17*T,1.6);"+lk(("K.x","K.y+1.1","K.z"),("cx","cy+0.6","cz"),56)
S["T2"]=car_a10(30,22)+"const K=at(40+18*T,0.8);"+lk(("K.x","K.y+0.9","K.z"),("cx","cy+0.7","cz"),52)
# reperage lettres
S["L1"]=PARK+lk(("70","25","520"),("70","4","640"),60)
S["L2"]=PARK+lk(("130","1.6","584"),("40","4.5","604"),50)
S["L3"]=PARK+lk(("70","30","700"),("70","2","600"),60)


def cx_line(x0,z,vx):
  ry=math.pi/2 if vx>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__CPN;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;g.rotation.x=0;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x0,vx,z,ry,abs(vx))
S["A1"]=car_a10(30,22)+"const K=at(38+21*T,1.5);"+lk(("K.x","K.y+0.75","K.z"),("cx","cy+1.5","cz"),56)
S["DH2"]=cx_line(-100,-115.5,-24)+lk(("cx+10","cy+6.5","cz"),("cx-2","cy+0.3","cz"),60)
S["F1"]=car_a10(110,24)+"const K=at(104+24*T,-25);"+lk(("K.x","K.y+4","K.z"),("cx","cy-3","cz"),56)
S["F2"]=car_a10(110,24)+"const K=at(100+24*T,-18);"+lk(("K.x","K.y+3","K.z"),("cx","cy-2.2","cz"),50)


S["L4"]=PARK+"const cz=700-20*T;"+lk(("70","14","cz"),("70","5","604"),56)
S["L5"]=PARK+"const cz=690-22*T;"+lk(("66+4*T","9","cz"),("70","6.5","604"),54)


S["F3"]=car_a10(150,20,3.0,-1)+"const K=at(4,0);"+lk(("K.x","K.y+1.2","K.z"),("cx","cy-2.5","cz"),56)
S["F4"]=car_a10(40,22)+"const K=at(4,0);"+lk(("K.x","K.y+1.2","K.z"),("cx","cy-2.5","cz"),56)


S["F5"]=car_a10(60,22)+"const K=at(82+22*T,-1.0);"+lk(("K.x","K.y+4.5","K.z"),("cx+(K.x-cx)*0.0","cy-6.5","cz"),56)
S["F6"]=car_a10(60,22)+"const K=at(90+22*T,-2.0);"+lk(("K.x","K.y+2.2","K.z"),("cx","cy-3.2","cz"),56)


S["L6"]=PARK+"const cx=26+40*T;"+lk(("cx","4","640"),("cx","4.6","604"),58)
S["L7"]=PARK+"const cx=26+40*T;"+lk(("cx","6","646"),("cx","4.4","604"),58)


S["L8"]=PARK+"const cx=26+50*T;"+lk(("cx","1.5","636"),("cx","4.9","604"),58)


S["F7"]=car_a10(60,22)+"const K=at(84+22*T,-1.0);"+lk(("K.x","K.y+4.2","K.z"),("cx","cy-3.4","cz"),56)


S["F8"]=car_a10(40,22)+"const K=at(64+22*T,-1.0);"+lk(("K.x","K.y+4.2","K.z"),("cx","cy-3.4","cz"),56)


S["L9"]=PARK+"const cx=26+50*T;const cz=636+Math.max(0,cx-66)*1.25;"+lk(("cx","1.5","cz"),("cx","4.9+(cz-636)*0.11","604"),58)

if __name__=="__main__":
  mode=sys.argv[1]; sel=sys.argv[2].split(',')
  sh=[mk5("w",S[sel[0]],wait=2000)]
  for k in sel:
    if mode=='r':
      for t in [float(x) for x in (sys.argv[3] if len(sys.argv)>3 else "0,0.6,1.2").split(',')]: sh.append(mk5("%s_%02d"%(k,int(round(t*10))),S[k],o=t))
    else: sh.append(mk5("pc"+k,S[k],n=int(sys.argv[3]),o=float(sys.argv[4]) if len(sys.argv)>4 else 0,wait=int(os.environ.get("WAIT","3000"))))
  print(run(sh,"/root/w/pc3/"+mode+CARID,w=1080,h=1920,name=os.environ.get("JN","pc3_")+mode+"".join(sel)+str(len(sys.argv)),wait=True))
