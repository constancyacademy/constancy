# M3 Gratuit b1 (mer. 25/11 17h, DEUX ÉCRANS) · Constancy Sud de jour, vraies voitures garées (V310.30) et passants
DT=int(os.environ.get("DT","480"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox;if(o.scale.y*(bb.max.y-bb.min.y)>100)H(o);}});(W6.JW&&W6.JW.beams||[]).forEach(b=>H(b.isObject3D?b:(b.m||b.mesh)));}}"
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+js); s["far"]=20000; return s
S={}
S["TA"]=L(("160","140","900"),("160","0","899"),70)
S["TB"]=L(("680","140","1000"),("680","0","999"),70)
S["TC"]=L(("-680","140","1000"),("-680","0","999"),70)
CAR="{const W9=window.__W();if(!window.__SUVG){const g=W9.makeCar(W9.CARS.find(c=>c.id==(window.__GRCAR||'suv')));W9.scene.add(g);window.__SUVG=g;}const g=window.__SUVG;delete g.visible;g.visible=true;window.__lt=null;}"
def xline(z,x0,vx):
  ry=math.pi/2 if vx>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__SUVG;const cz=%f,cx=%f+(%f)*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(z,x0,vx,ry,abs(vx))
_MKG=MK
def MK(name,body,n=1,o=0,js="",wait=2500): return _MKG(name,body,n=n,o=o,js=CAR+js,wait=wait)
S["B1"]=xline(952,152,-12)+L(("131","cy+0.75","950.2"),("cx","cy+0.8","cz"),58)
S["B2"]=xline(952,175,-12)+L(("cx+5","cy+10","cz+12"),("cx-5","cy","cz-1"),60)
S["B3"]=xline(848,178,-12)+L(("cx+6","cy+1.4","cz+2.5"),("cx-6","cy+0.6","cz-0.5"),60)
S["B4"]=xline(848,130,12)+L(("cx+9","cy+1.6","cz-3"),("cx","cy+0.9","cz"),56)
S["B1"]=xline(952,156,-9)+L(("139.5","cy+0.75","949.6"),("cx","cy+0.8","cz"),58)
S["B2"]=xline(952,174,-9)+L(("cx+3","cy+14","cz-11"),("cx-7","cy","cz+1"),60)
S["B3"]=xline(848,168,-9)+L(("cx+6","cy+1.4","cz+2.5"),("cx-6","cy+0.6","cz-0.5"),60)
S["B4"]=xline(848,141,9)+L(("cx+9","cy+1.6","cz-3"),("cx","cy+0.9","cz"),56)
S["B1"]=xline(952,157.8,-9)+L(("139.5","cy+0.75","949.6"),("cx","cy+0.8","cz"),58)
S["B4c"]=xline(848,137.2,9)+L(("cx+6.5","cy+1.3","cz-2.2"),("cx-0.5","cy+0.7","cz"),52)
S["B3l"]=xline(848,170,-9)+L(("cx+6","cy+1.4","cz+2.5"),("cx-6","cy+0.6","cz-0.5"),60)
# 23/11 23h40 : le SUV Noir Mat en mouvement a les passages de roue qui se déchirent (roue qui sort de l'aile de près) : Prototype Minuit à la place
CAR="window.__GRCAR='minuit';"+CAR
CAR="{const W9=window.__W();if(window.__SUVG&&window.__SUVG.__cid!=='minuit'){W9.scene.remove(window.__SUVG);window.__SUVG=null;}}"+CAR+"{window.__SUVG.__cid='minuit';}"
