import os,math,sys
exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","480"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox;if(o.scale.y*(bb.max.y-bb.min.y)>100)H(o);}});(W6.JW&&W6.JW.beams||[]).forEach(b=>H(b.isObject3D?b:(b.m||b.mesh)));}}"
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
def CARJ(cid): return ("{const W9=window.__W();if(window.__SUVG&&window.__SUVG.__cid!=='%s'){W9.scene.remove(window.__SUVG);window.__SUVG=null;}if(!window.__SUVG){const g=W9.makeCar(W9.CARS.find(c=>c.id=='%s'));W9.scene.add(g);window.__SUVG=g;g.__cid='%s';}const g=window.__SUVG;delete g.visible;g.visible=true;window.__lt=null;}")%(cid,cid,cid)
def xline(z,x0,vx):
  ry=math.pi/2 if vx>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__SUVG;const cz=%f,cx=%f+(%f)*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(z,x0,vx,ry,abs(vx))
def zline(x,z0,vz):
  ry=0 if vz>0 else math.pi
  return ("const W7=window.__W();const g=window.__SUVG;const cx=%f,cz=%f+(%f)*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,vz,ry,abs(vz))
def MK3(name,body,cid="citadine",n=1,o=0,fps=60,wait=2500,js=""):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+CARJ(cid)+js); s["far"]=20000; s["fps"]=fps; return s
def xacc(z,x0,v0,a,sgn=-1):
  ry=math.pi/2 if sgn>0 else -math.pi/2
  return ("const W7=window.__W();const g=window.__SUVG;const cz=%f,cx=%f+(%d)*(%f*T+0.5*%f*T*T),vv=%f+%f*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;")%(z,x0,sgn,v0,a,v0,a,ry)
S={}
S["C1"]=xline(-168,-215,-12)+L(("cx-10+2*T","cy+1.2","-165.5"),("cx","cy+0.7","cz"),52)
S["C2"]=xline(-168,-262,-12)+L(("cx+1","cy+1.0","-160.5"),("cx-1","cy+0.8","cz"),50)
S["K1"]=xline(-168,-300,-4)+L(("cx+6*Math.cos(0.5+0.5*T)","cy+0.9","-168+6*Math.sin(0.5+0.5*T)"),("cx","cy+0.6","cz"),50)
S["K2"]=xacc(-168,-318,4,10)+L(("-312","cy+0.7","-166.3"),("cx","cy+0.7","cz"),52)
Z=-169.6
S["C1"]=xline(Z,-215,-12)+L(("cx-10+2*T","cy+1.2","-166.5"),("cx","cy+0.7","cz"),52)
S["C2"]=xline(Z,-262,-12)+L(("cx+1","cy+1.0","-161.5"),("cx-1","cy+0.8","cz"),50)
S["K1"]=xline(Z,-300,-4)+L(("cx+6*Math.cos(0.5+0.5*T)","cy+0.9","%f+6*Math.sin(0.5+0.5*T)"%Z),("cx","cy+0.6","cz"),50)
S["K2"]=xacc(Z,-296,3,9)+L(("-318","cy+0.55","-172.2"),("cx","cy+0.7","cz"),54)
# exec(open('/root/w/m3/mk3.py').read())
# J=notraf
# sh=[MK3("x",S["C1"]),MK3("bC1",S["C1"],n=144,js=J),MK3("bC2",S["C2"],n=126,js=J),MK3("bK1",S["K1"],"coupe",n=102,js=J),MK3("bK2",S["K2"],"coupe",n=160,js=J)]
# print(run(sh,"/root/w/m3/fin",w=1080,h=960,name="m3fin",wait=False))
