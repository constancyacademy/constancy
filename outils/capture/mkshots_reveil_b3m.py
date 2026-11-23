import os
# Réveil b2 (24/11 17h) : corrections de l'expert du 23/11 1h58
import sys
sys.argv_saved=list(sys.argv); sys.argv=[sys.argv[0],"x","A"]
exec(open('/root/cap/mkshots_m3reveil_plans.py').read().split('if __name__')[0])
sys.argv=sys.argv_saved
def shut_fast(T0,D=0.9):
  return (FIND+"{const i=window.__CI,q=S7.L[i];const f=Math.min(1,Math.max(0,1-(T-(%f))/%f));q.f=f;const o=new THREE.Object3D();const D=1.52;o.position.set(q.x+D*Math.sin(q.ry),q.y0+3.0,q.z+D*Math.cos(q.ry));o.rotation.set(0,q.ry,0);o.scale.set(q.L+0.12,Math.max(0.0001,3*f),1);o.updateMatrix();S7.im.setMatrixAt(i,o.matrix);S7.aF.array[i]=Math.max(0.001,f);S7.im.instanceMatrix.needsUpdate=true;S7.aF.needsUpdate=true;}")%(T0,D)
def drive2(x0,z,vx,k0,kr):
  return ("const W7=window.__W();const g=window.__CT;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.y=-Math.PI/2;"
   "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"
   "W7.G.onFoot=false;W7.G.ride={kind:'own'};W7.G.fpv=true;W7.BUEE.k=Math.max(0,%f-%f*T);")%(x0,vx,z,abs(vx),k0,kr)
Q={}
# E2 : image 1, soleil qui se leve sur la ville vue d'en haut, camera lancee
Q["E2"]=dict(h0=7.03,js=HIDECT+HIDEGT+UNFPV,body=look(("-92-16*T","50+1.2*T","-80+1.5*T"),("-420","22","-55"),60))
Q["E3"]=dict(h0=7.03,js=HIDECT+HIDEGT+UNFPV,body=look(("-92-16*T","52-1.0*T","-82+3*T"),("-420","18","-45"),62))
# A : gros plan rideau du cafe
for k,(cz,cy,ty,fov) in {"Aa":(-121.6,2.9,2.7,50),"Ab":(-121.0,3.3,2.5,52),"Ac":(-122.2,2.4,2.6,48)}.items():
  Q[k]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_fast(0.55,0.9)+look(("-133.0+0.5*T",str(cy),str(cz)),("-132.3+0.5*T",str(ty),"-125.4"),fov))
# B : vue conducteur, pare-brise sur 70 %
for k,(ex,ey,fov,ty) in {"Ba":(0.35,1.40,66,0.95),"Bb":(0.15,1.32,70,1.0),"Bc":(0.45,1.50,58,1.05)}.items():
  Q[k]=dict(h0=6.85,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx+%s"%ex,"cy+%s"%ey,"cz+0.33"),("cx-40","cy+%s"%ty,"cz+0.33"),fov))
# C : premiere voiture, entre 40 et 65 % de la hauteur
Q["C2"]=dict(h0=6.79,js=FORCE+HIDECT+UNFPV+HIDEGT+notraf+CP,body=shut_smooth(-3.5)+carline2(-134,-108.3,10)+look(("-146+1.2*T","1.5+0.6*T","-111.4"),("-95","1.3+0.3*T","-109.6"),55))

CAFE=lambda T0,D: shut_fast(T0,D)
Q["Af"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_fast(0.3,0.9)+look(("-132.3+0.4*T","3.2","-117.4"),("-132.3+0.4*T","3.0","-123.9"),46))
Q["Ag"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_fast(0.3,0.9)+look(("-139.5+0.5*T","1.9","-121.4"),("-131","2.2","-123.9"),50))
Q["Ah"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_fast(0.3,0.9)+look(("-132.3","1.3","-115.5"),("-132.3","2.4","-123.9"),46))
for k,(ex,ey,fov,ty) in {"Bd":(-0.10,1.30,70,1.25),"Be":(-0.30,1.25,66,1.25)}.items():
  Q[k]=dict(h0=6.85,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx+%s"%ex,"cy+%s"%ey,"cz+0.33"),("cx-40","cy+%s"%ty,"cz+0.33"),fov))

Q["E4"]=dict(h0=7.03,js=HIDECT+HIDEGT+UNFPV,body=look(("-100-16*T","50+1.2*T","-80+1.5*T"),("-420","22","-55"),60))
Q["Ai"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut_fast(0.62,1.0)+look(("-132.3+0.3*T","3.4","-117.4+0.8*T"),("-132.3+0.3*T","3.69","-123.9"),34))

Q["Bf"]=dict(h0=6.85,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx+0.15","cy+1.32","cz+0.33"),("cx-40","cy+9.8","cz+0.33"),44))
Q["Bg"]=dict(h0=6.85,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx+0.15","cy+1.32","cz+0.33"),("cx-40","cy+8.4","cz+0.33"),48))
def mkq(k,o=0,n=1,nm=None):
  d=Q[k]; return m3(nm or k,d["body"],d["h0"],n=n,o=o,js=d["js"],rate=R)
if __name__=="__main__":
  mode=sys.argv[1]; ks=sys.argv[2].split(',')
  sh=[mkq(ks[0],nm="warm")]
  for k in ks:
    if mode=="r":
      for t in [float(x) for x in (sys.argv[3] if len(sys.argv)>3 else "0,0.75,1.5").split(',')]: sh.append(mkq(k,o=t,nm="%s_%02d"%(k,int(round(t*10)))))
    else: sh.append(mkq(k,n=int(sys.argv[3]),o=float(sys.argv[4]) if len(sys.argv)>4 else 0,nm="rv"+k))
  print(run(sh,"/root/w/rv/"+mode,w=1080,h=1920,name=os.environ.get("JN","rv_")+("z" if mode!="r" else "")+mode+"_"+"".join(ks)+str(len(sys.argv)),wait=False))
