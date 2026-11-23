from mkshots_m3reveil_lib import *
import sys, math
L212=open('/root/cap/lib212.py').read().split('\n',1)[1]
exec(L212)  # GT, HIDELIGHTS, NOPLANE, carline, NO
FIND="const S7=W6.SHUT;if(window.__CI==null)window.__CI=S7.L.findIndex(q=>Math.abs(q.x+132.3)<0.3&&Math.abs(q.z+125.4)<0.3);"
def shut_smooth(T0):
  return (FIND+"{const i=window.__CI,q=S7.L[i];const f=Math.min(1,Math.max(0,1-(T-(%f))/3.2));q.f=f;const o=new THREE.Object3D();const D=1.52;o.position.set(q.x+D*Math.sin(q.ry),q.y0+3.0,q.z+D*Math.cos(q.ry));o.rotation.set(0,q.ry,0);o.scale.set(q.L+0.12,Math.max(0.0001,3*f),1);o.updateMatrix();S7.im.setMatrixAt(i,o.matrix);S7.aF.array[i]=Math.max(0.001,f);S7.im.instanceMatrix.needsUpdate=true;S7.aF.needsUpdate=true;}")%T0
FORCE="{const W6=window.__W();W6.updateShutters(1,true);}"
CAR="{const W7=window.__W();if(!window.__CT){const g=W7.makeCar(W7.CARS.find(c=>c.id=='citadine'));W7.scene.add(g);window.__CT=g;}delete window.__CT.visible;window.__CT.visible=true;window.__lt=null;}"
HIDECT="{if(window.__CT)window.__CT.visible=false;if(window.__CP2)window.__CP2.visible=false;}"
HIDEGT="{if(window.__GT)window.__GT.visible=false;}"
def drive(x0,z,vx,k0):
  return ("const W7=window.__W();const g=window.__CT;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.y=-Math.PI/2;"
   "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"
   "W7.G.onFoot=false;W7.G.ride={kind:'own'};W7.G.fpv=true;W7.BUEE.k=Math.max(0,%f-T/8);")%(x0,vx,z,abs(vx),k0)
UNFPV="{const W7=window.__W();W7.G.onFoot=true;W7.G.ride={kind:'none'};W7.G.fpv=false;W7.BUEE.k=0;}"
R=0.0513
P={}
# A cafe : rideau qui remonte, travelling lateral
P["A"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_smooth(0.10)+look(("-143.5+7.5*T","3.1-0.4*T","-110.0"),("-134.0+2.2*T","1.6","-124"),50))
# D rue encore fermee (plaques Ouvert des 7 h), travelling le long des boutiques
P["D"]=dict(h0=6.680,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_smooth(-1.35)+look(("-104-1.5*T","3.2+3.6*T","-113.5"),("-150","2.0-0.8*T","-119"),55))
# B buee vue conducteur
P["B"]=dict(h0=6.850,js=CAR+HIDEGT,body=drive(-98,-115.5,-11,0.80)+look(("cx+0.7","cy+1.42","cz+0.33"),("cx-40","cy+0.82","cz+0.33"),62))
# C passants + premiere voiture (GT orange), sans circulation
CP="{const W7=window.__W();if(!window.__CP2){const g=W7.makeCar(W7.CARS.find(c=>c.id=='coupe'));W7.scene.add(g);window.__CP2=g;}W7.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__CP2&&o!==window.__CT&&o!==window.__GT&&o!==window.__HY&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});delete window.__CP2.visible;window.__CP2.visible=true;window.__lt=null;}"+HIDELIGHTS
def carline2(x0,z,vx):
  return ("const W7=window.__W();const g=window.__CP2;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.y=Math.PI/2;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x0,vx,z,abs(vx))
P["C"]=dict(h0=6.79,js=FORCE+HIDECT+UNFPV+HIDEGT+notraf+CP,body=shut_smooth(-3.5)+carline2(-139,-108.3,10)+look(("-146+1.2*T","2.6+1.4*T","-111.4"),("-95","1.4+0.4*T","-109.6"),55))
# E soleil qui se leve sur la ville, vu d'en haut (45 m), lent travelling vers le soleil
P["E"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV,body=look(("-99.5-7*T","49+1.5*T","-80"),("-420","24","-55"),60))
def mkp(k,o=0,n=1,nm=None):
  d=P[k]; s=m3(nm or k,d["body"],d["h0"],n=n,o=o,js=d["js"],rate=R); return s
if __name__=="__main__":
  mode=sys.argv[1]; ks=sys.argv[2].split(',')
  sh=[mkp(ks[0],nm="warm")]
  for k in ks:
    if mode=="r":
      for t in (0,0.75,1.5): sh.append(mkp(k,o=t,nm="%s_%02d"%(k,int(t*10))))
    else: sh.append(mkp(k,n=int(sys.argv[3]) if len(sys.argv)>3 else 47,nm="m3"+k))
  run(sh,"/root/w/m3/"+("r" if mode=="r" else "full"),w=1080,h=1920,name="m3_"+mode+"_"+"".join(ks))
