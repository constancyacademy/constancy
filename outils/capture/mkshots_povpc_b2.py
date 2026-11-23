# POV PC b2 (24/11 21h) : coupé néon, corrections de l'expert du 23/11 5h35
import sys,math,os
exec(open('/root/cap/lib212.py').read())
CARID=os.environ.get("CARID","coupe")
CPN=notraf+"{const W9=window.__W();if(!window.__CPN){const g=W9.makeCar(W9.CARS.find(c=>c.id=='%s'));W9.scene.add(g);window.__CPN=g;}W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__CPN&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});delete window.__CPN.visible;window.__CPN.visible=true;window.__lt=null;}"%CARID+HIDELIGHTS
NOWALK="{const W9=window.__W();(W9.WALKERS||[]).forEach(w=>{if(w.h&&!w.h.__hid){const p=w.h.position;if(p.z>540&&p.z<640){w.h.__hid=1;Object.defineProperty(w.h,'visible',{configurable:true,get:()=>false,set:()=>{}});}}});}"
HIDEPPL="{const W9=window.__W();const v=new THREE.Vector3();const L=[];const A=(a,f)=>{(a||[]).forEach(e=>{const m=f?f(e):e;if(m&&m.isObject3D)L.push(m);});};const B=W9.BEACH||{};A(B.walk,e=>e.h);A(B.swim,e=>e.h);A(B.night);A((W9.life||{}).beach,e=>e.mesh);A((W9.life||{}).dogs,e=>e.mesh);A((W9.GUING||{}).people);A((W9.FIRES||{}).people);A(W9.peds,e=>e.mesh);A(W9.WALKERS,e=>e.h);L.forEach(m=>{if(m.__hid)return;m.getWorldPosition(v);if(v.x>-40&&v.x<160&&v.z>530&&v.z<650){m.__hid=1;Object.defineProperty(m,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
def cx_line(x0,z,vx):
  ry=math.pi/2 if vx>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__CPN;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x0,vx,z,ry,abs(vx))
def cz_line(x,z0,vz):
  ry=0 if vz>0 else math.pi
  return ("const W7=window.__W();const g=window.__CPN;const cx=%f,cz=%f+(%f)*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,vz,ry,abs(vz))
PARK="const g=window.__CPN;g.position.set(0,-50,0);"
UNFPV="{const W7=window.__W();W7.G.onFoot=true;W7.G.ride={kind:'none'};W7.G.fpv=false;W7.BUEE.k=0;}"
HIDEPPL2=HIDEPPL.replace("v.x>-40&&v.x<160&&v.z>530&&v.z<650","(v.x>-40&&v.x<160&&v.z>530&&v.z<650)||(v.x>-10&&v.x<230&&v.z>25&&v.z<105)||(v.x>-170&&v.x<-50&&v.z>-135&&v.z<-95)")
def mk5(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=840,n=n,toff=o,wait=wait,js=UNFPV+NO+NOPLANE+CPN+NOWALK+HIDEPPL2+js,pre=UNFPV); s["far"]=20000; return s
S={}
# image 1 : la coupe frole la camera au ras du sol
S["H1"]=cx_line(-83,-115.5,-24)+lk(("-95","0.6","-112.4"),("cx","cy+0.7","cz"),58)      # rue du club (ref b1)
S["AV"]=cz_line(119.6,32,-24)+lk(("122.8","0.6","20"),("cx","cy+0.7","cz"),58)           # avenue x=119,6
S["RZ"]=cx_line(48,63.6,24)+lk(("60","0.6","60.4"),("cx","cy+0.7","cz"),58)               # rue z=63,6
# drone dans l'axe, derriere la voiture
S["DAV"]=cz_line(119.6,16,-24)+lk(("cx","cy+6.5","cz+10"),("cx","cy+0.3","cz-7"),60)
S["DRZ"]=cx_line(64,63.6,24)+lk(("cx-10","cy+6.5","cz"),("cx+7","cy+0.3","cz"),60)
S["DH"]=cx_line(-100,-115.5,-24)+lk(("cx+10","cy+6.5","cz"),("cx-7","cy+0.3","cz"),60)
# lettres seules (sans voiture), travelling vers -x
S["LS"]=HIDEPPL+PARK+"const cx=108-40*T;"+lk(("cx+1","3.2","553"),("cx+1","3.2","604"),60)
# plan final : la voiture qui revient vers la camera
S["FAV"]=cz_line(119.6,60,-24)+lk(("121.5","1.2+0.3*T","8"),("cx","cy+0.8","cz"),56)
S["I1"]=cx_line(20,63.6,24)+lk(("62","0.6","60.2"),("cx","cy+0.7","cz"),58)
S["D2"]=cx_line(40,63.6,24)+lk(("cx-9","cy+6","cz"),("cx+2","cy","cz"),60)
S["F2"]=cx_line(20,63.6,20)+"const kx=46+12*T;"+lk(("kx","1.5","63.6"),("cx","cy+0.6","cz"),58)
S["F3"]=cx_line(70,63.6,24)+"const kx=cx+8-0.9*T;"+lk(("kx","cy+1.6","cz"),("cx+2","cy-0.6","cz"),60)
S["DH2"]=cx_line(-100,-115.5,-24)+lk(("cx+10","cy+6.5","cz"),("cx-2","cy+0.3","cz"),60)
S["LS2"]=HIDEPPL+PARK+"const cx=108-40*T;"+lk(("cx+1","2.4","553"),("cx+1","14","604"),60)
S["F4"]=cx_line(70,63.6,24)+"const kx=cx+8-0.9*T;"+lk(("kx","cy+1.6","cz"),("cx+2","cy+0.0","cz"),60)
if __name__=="__main__":
  mode=sys.argv[1]; sel=sys.argv[2].split(',')
  sh=[mk5("w",S[sel[0]],wait=2000)]
  for k in sel:
    if mode=='r':
      for t in [float(x) for x in (sys.argv[3] if len(sys.argv)>3 else "0,0.6,1.2").split(',')]: sh.append(mk5("%s_%02d"%(k,int(round(t*10))),S[k],o=t))
    else: sh.append(mk5("pc"+k,S[k],n=int(sys.argv[3]),o=float(sys.argv[4]) if len(sys.argv)>4 else 0,wait=int(os.environ.get("WAIT","3000"))))
  print(run(sh,"/root/w/pc/"+mode,w=1080,h=1920,name=os.environ.get("JN","pc_")+mode+"".join(sel)+str(len(sys.argv)),wait=False))
