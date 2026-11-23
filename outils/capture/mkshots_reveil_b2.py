# Réveil de la ville b2 (corrections de l'expert du 23/11 1h58) : python3 mkshots_reveil_b2.py r|f PLANS [n]
import sys; sys.path[:0]=['/root/cap','/home/claude/rushes/outils/capture']
_src=open('/home/claude/rushes/outils/capture/mkshots_m3reveil_plans.py').read().split('if __name__')[0]
exec(_src)
def shut2(T0,dur):
  return (FIND+"{const i=window.__CI,q=S7.L[i];const f=Math.min(1,Math.max(0,1-(T-(%f))/%f));q.f=f;const o=new THREE.Object3D();const D=1.52;o.position.set(q.x+D*Math.sin(q.ry),q.y0+3.0,q.z+D*Math.cos(q.ry));o.rotation.set(0,q.ry,0);o.scale.set(q.L+0.12,Math.max(0.0001,3*f),1);o.updateMatrix();S7.im.setMatrixAt(i,o.matrix);S7.aF.array[i]=Math.max(0.001,f);S7.im.instanceMatrix.needsUpdate=true;S7.aF.needsUpdate=true;}")%(T0,dur)
def drive2(x0,z,vx,k0,kr):
  return ("const W7=window.__W();const g=window.__CT;const cx=%f+(%f)*T,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.y=-Math.PI/2;"
   "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"
   "W7.G.onFoot=false;W7.G.ride={kind:'own'};W7.G.fpv=true;W7.BUEE.k=Math.max(0,%f-%f*T);")%(x0,vx,z,abs(vx),k0,kr)
P["E2"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV,body=look(("-95-18*T","49+1.0*T","-80+6*T"),("-420","40","-50-40*T"),60))
P["A2"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV,body=shut2(0.25,2.0)+look(("-131.2+0.8*T","2.5","-119.0"),("-132.3","2.1","-125.4"),55))
P["C2"]=dict(h0=6.79,js=FORCE+HIDECT+UNFPV+HIDEGT+notraf+CP,body=shut_smooth(-3.5)+carline2(-136,-108.3,10)+look(("-146+1.2*T","2.6+1.4*T","-111.4"),("-95","-10+2*T","-109.6"),55))
P["B2"]=dict(h0=6.850,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx+0.3","cy+1.5","cz+0.33"),("cx-40","cy+1.45","cz+0.33"),55))
HIDEPEO="{const W6=window.__W();const v=new THREE.Vector3();W6.scene.traverse(o=>{if(o.userData&&o.userData.rig!==undefined&&!o.__hp){o.getWorldPosition(v);if(v.x>-142&&v.x<-122&&v.z>-127&&v.z<-113){o.__hp=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}}});}"
P["E3"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV,body=look(("-103-18*T","49+1.0*T","-80+6*T"),("-420","40","-50-40*T"),60))
P["A3"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV+HIDEPEO,body=HIDEPEO+shut2(0.0,5.36)+look(("-131.6+0.4*T","2.4","-117.9+0.6*T"),("-132.3","2.5","-125.4"),26))
P["B3"]=dict(h0=6.850,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx+0.15","cy+1.35","cz+0.33"),("cx-40","cy+1.6","cz+0.33"),42))
def shut3(T0,dur,fmin):
  return shut2(T0,dur).replace("const f=Math.min(1,Math.max(0,","const f=Math.min(1,Math.max(%f,"%fmin)
P["A4"]=dict(h0=6.600,js=FORCE+HIDECT+HIDEGT+UNFPV+HIDEPEO,body=HIDEPEO+shut3(0.15,1.9,0.68)+look(("-131.0+1.2*T","2.0","-118.6+0.5*T"),("-132.3","1.9","-125.4"),48))
P["B4"]=dict(h0=6.850,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx-0.2","cy+1.45","cz+0.33"),("cx-40","cy+1.45","cz+0.33"),50))
P["B5"]=dict(h0=6.850,js=CAR+HIDEGT,body=drive2(-98,-115.5,-11,0.95,0.6)+look(("cx-0.45","cy+1.4","cz+0.33"),("cx-40","cy+1.4","cz+0.33"),55))
P["E4"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV,body=look(("-103-30*T","49+1.5*T","-80+8*T"),("-420","40","-40-70*T"),60))
P["B6"]=dict(h0=6.850,js=CAR+HIDEGT,body=drive2(-92,-115.5,-16,0.95,0.6)+look(("cx-0.2","cy+1.45","cz+0.33"),("cx-40","cy+1.45","cz+0.33"),50))
P["E5"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV,body=look(("-103-30*T","49+1.5*T","-80+8*T"),("-420","40","0-70*T"),60))
P["D2"]=dict(h0=P["D"]["h0"],js=P["D"]["js"]+HIDEPEO,body=HIDEPEO+P["D"]["body"])
P["D3"]=dict(h0=P["D"]["h0"],js=P["D"]["js"]+HIDEPEO+CLOUD,body=HIDEPEO+P["D"]["body"])
P["D4"]=dict(h0=P["D"]["h0"],js=P["D"]["js"]+HIDEPEO+CLOUD+NOPLANE,body=HIDEPEO+P["D"]["body"])
P["E6"]=dict(h0=7.05,js=P["E5"]["js"]+CLOUD+NOPLANE,body=P["E5"]["body"])
P["B7"]=dict(h0=6.850,js=P["B4"]["js"]+CLOUD+NOPLANE,body=P["B4"]["body"])
P["E7"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV+CLOUD+NOPLANE,body=look(("-103-30*T","49+1.5*T","-80+8*T"),("-420","40","75-45*T"),60))
P["E8"]=dict(h0=7.05,js=HIDECT+HIDEGT+UNFPV+CLOUD+NOPLANE,body=look(("-115-30*T","49+1.5*T","-80+8*T"),("-420","92","75-45*T"),60))
if __name__=="__main__":
  mode=sys.argv[1]; ks=sys.argv[2].split(',')
  sh=[mkp(ks[0],nm="warm")]
  for k in ks:
    if mode=="r":
      for t in [float(x) for x in (sys.argv[3] if len(sys.argv)>3 else "0,0.75,1.5").split(',')]: sh.append(mkp(k,o=t,nm="%s_%02d"%(k,int(round(t*10)))))
    else:
      d=P[k]; s=m3("m3"+k,d["body"],d["h0"],n=int(sys.argv[3]),o=0,js=d["js"],rate=R); s["wait"]=9000; sh.append(s)
  run(sh,"/root/w/m3/"+mode,w=1080,h=1920,name="m3_"+mode+"_"+"".join(ks),wait=False)
