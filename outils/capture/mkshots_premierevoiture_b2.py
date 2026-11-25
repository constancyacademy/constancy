import os,math,sys
exec(open('/root/cap/lib212.py').read())
exec(open('/home/claude/rushes/outils/capture/mkshots_premierevoiture_b1.py').read().split("S={}")[0].split("exec(open('/root/cap/lib212.py').read())")[1])
Z=-169.6
def BEACON(xb,zb): return "{const W5b=window.__W();const b=W5b.destBeacon;if(b){b.position.set(%f,0,%f);delete b.visible;b.visible=true;}}"%(xb,zb)
def xstop(z,x0,v0,a):
  # voiture vers -x, freine (a>0 décélération) jusqu'à l'arrêt
  return ("const W7=window.__W();const g=window.__SUVG;const ts=%f/%f,Tc=Math.min(Math.max(T,0),ts);const cz=%f,cx=%f-(%f*Tc-0.5*%f*Tc*Tc),vv=%f-%f*Tc;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=-Math.PI/2;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;")%(v0,a,z,x0,v0,a,v0,a)
S={}
def MKD(name,body,cid="citadine",n=1,dt=480,js="",wait=2500,fps=60,pre=0):
  s=shot(name,body,dayT=dt,n=n,toff=0,wait=wait,js=NO+NOPLANE+HB+UNFPV+CARJ(cid)+notraf+js); s["far"]=20000; s["fps"]=fps
  if pre: s["pre"]=pre
  return s
# repérage
S["K34"]=xline(Z,-300,0)+L(("cx-4.2","cy+1.1","%f+3.0"%Z),("cx+0.3","cy+0.55","cz"),50)
S["K34r"]=xline(Z,-300,0)+L(("cx+4.4","cy+1.2","%f-3.2"%Z),("cx-0.3","cy+0.55","cz"),50)
S["CT"]=xline(Z,-230,-11)+L(("cx-5.2","cy+0.9","%f+2.4"%Z),("cx","cy+0.6","cz"),52)
S["BZ"]=xline(Z,-280,0)+L(("cx+9","cy+2.6","%f-4.5"%Z),("cx-2","cy+0.4","cz"),52)
def xacc2(z,x0,v0,a):
  return ("const W7=window.__W();const g=window.__SUVG;const cz=%f,cx=%f-(%f*T+0.5*%f*T*T),vv=%f+%f*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=-Math.PI/2;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;")%(z,x0,v0,a,v0,a)
ZC=Z+2.4
# F1 image 1 : citadine à 11 m/s, caméra devant qui recule à 8,26 m/s, la voiture la rattrape et la frôle vers 1,9 s
S["F1"]=xline(Z,-215,-11)+L(("-220.2-8.26*T","cy+0.9","%f"%ZC),("cx","cy+0.6","cz"),52)
# F2 livraison : citadine qui freine et s'arrête dans l'anneau violet (-280)
S["F2"]=xstop(Z,-269.92,11,6)+L(("cx+8.2-0.8*T","cy+2.4","%f-4.2"%Z),("cx-2.6","cy+0.45","cz"),52)
# F3 coupé débloquée : orbite basse 3/4 avant -> profil, coucher du soleil
S["F3"]=xline(Z,-300,0)+L(("cx+5.2*Math.cos(2.62-0.34*T)","cy+1.0","cz+5.2*Math.sin(2.62-0.34*T)"),("cx+0.2","cy+0.5","cz"),50)
# F4 la coupé roule déjà à 12 m, frôle la caméra vers 0,7 s, puis s'éloigne
S["F4"]=xacc2(Z,-288,14,4)+L(("-300","cy*0+0.85+W7.GH(-300,%f)"%(Z+3.2),"%f"%(Z+3.2)),("cx-1.2","cy+0.55","cz"),54)
S["F1"]=xline(Z,-215,-11)+L(("-220.93-9.5*T","cy+0.9","%f"%ZC),("cx","cy+0.6","cz"),52)
S["F2"]=xstop(Z,-269.92,11,6)+L(("cx+8.2-0.8*T","cy+2.4","%f-4.2"%Z),("cx-2.6","cy+2.5","cz"),58)
