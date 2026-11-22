from rex import *
import sys
AIMF="""const aim=(p,H,u,v,fov)=>{const tv=Math.tan(fov*Math.PI/360),th=tv*1080/1920;let d=new THREE.Vector3(H.x-p[0],H.y-p[1],H.z-p[2]).normalize();const r=new THREE.Vector3().crossVectors(d,new THREE.Vector3(0,1,0)).normalize();const uu=new THREE.Vector3().crossVectors(r,d);const x=2*u-1,y=1-2*v;const w=d.clone().addScaledVector(r,-x*th).addScaledVector(uu,-y*tv).normalize();return [p[0]+w.x*10,p[1]+w.y*10,p[2]+w.z*10];};
const eyes=()=>{const a=bone('L_Eye'),b=bone('R_Eye');return a.add(b).multiplyScalar(0.5);};const bone=n=>{let b=null;W6.REX.d.g.traverse(o=>{if(o.isBone&&o.name===n)b=o;});b.updateWorldMatrix(true,false);return new THREE.Vector3().setFromMatrixPosition(b.matrixWorld);};"""
def camA(a0,dphi,rad,h,bn,u,v,fov):
  # camera sur le cercle (comme polp), visée calée pour que l'os bn tombe au pixel (u,v)
  return (PIN(a0)+AIMF+"const d6=W6.REX.d;const A=(%s)+(%s);const p=[d6.cx+Math.cos(A)*(%s),P.y+(%s),d6.cz+Math.sin(A)*(%s)];const H=('%s'==='EYES')?eyes():bone('%s');return {p,t:aim(p,H,%s,%s,%s),fov:%s};")%(a0,dphi,rad,h,rad,bn,bn,u,v,fov,fov)
def camR(a0,f,s,u_,bn,u,v,fov):
  # camera relative au Rex (avant f, cote s, haut u_)
  return (PIN(a0)+AIMF+"const p=[P.x+fx*(%s)+sx*(%s),P.y+(%s),P.z+fz*(%s)+sz*(%s)];const H=('%s'==='EYES')?eyes():bone('%s');return {p,t:aim(p,H,%s,%s,%s),fov:%s};")%(f,s,u_,f,s,bn,bn,u,v,fov,fov)
SH={
 "GD2":camA(1.0,1.20,"61.5-0.8*T",5,"EYES",0.5,0.47,58),
 "GC2":camR(1.6,"6","-66","4","L_Foot",0.5,0.645,85),
 "GA":camA(1.0,0.92,"60.5-0.8*T",8,"EYES",0.27,0.48,60),
 "GB":camR(1.3,"48","-18","1.2+9*T","EYES",0.5,0.57,58),
 "GC":camR(1.6,"6","-52","4","L_Foot",0.5,0.71,85),
 "GD":camA(1.0,1.20,"61.5-0.8*T",5,"EYES",0.5,0.55,58),
 "FA":camA(1.0,0.85,"60.5-0.8*T",9,"EYES",0.27,0.38,60),
 "FA2":camA(1.0,0.92,"60.5-0.8*T",8,"EYES",0.27,0.38,60),
 "FB":camR(1.3,"48","-18","1.2+9*T","EYES",0.5,0.47,58),
 "FC":camR(1.6,"6","-52","4","L_Foot",0.5,0.68,75),
 "FD":camA(1.0,1.20,"61.5-0.8*T",5,"EYES",0.5,0.45,58),
 "A3":camA(1.0,0.70,"60.5-1.0*T",9,"Head",0.30,0.48,60),
 "A4":camA(1.0,0.55,"60.5-1.0*T",9,"Head",0.30,0.48,60),
 "C2":camR(1.6,"10","-85","6","L_Foot",0.5,0.70,60),
 "D2":camA(1.0,1.20,"61.5-0.8*T",5,"Head",0.5,0.50,58),
 "A1":camA(1.0,0.97,"60.5-1.0*T",9,"Head",0.26,0.40,62),
 "A2":camA(1.0,1.25,"60.5-1.0*T",9,"Head",0.26,0.40,62),
 "B":camR(1.3,"48","-18","1.2+9*T","Head",0.5,0.47,58),
 "C":camR(1.6,"6","-58","5","L_Foot",0.5,0.68,52),
 "D":camA(1.0,1.34,"59-0.8*T",5,"Head",0.5,0.43,62),
}
if __name__=="__main__":
  mode=sys.argv[1]; ks=sys.argv[2].split(',')
  DT=int(sys.argv[4]) if len(sys.argv)>4 else 840
  sh=[mk("w",SH[ks[0]],wait=3000,dt=DT)]
  for k in ks:
    if mode=="r":
      for t in (0,1.3): sh.append(mk("%s_%02d"%(k,int(t*10)),SH[k],o=t,dt=DT))
    else: sh.append(mk("m1"+k,SH[k],n=int(sys.argv[3]),wait=3000,dt=DT))
  print(run(sh,"/root/w/m1/"+mode+str(DT),w=1080,h=1920,name="rx_"+mode+"".join(ks)))
