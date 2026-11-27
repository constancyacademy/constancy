S["F6"]=CHASE(110,12,24)+AIM(ax(64,6,1.0),"Head",0.55,0.40,70)
S["F7"]=CHASE(110,12,24)+AIM(ax(64,-6,1.0),"Head",0.45,0.40,70)
def ORB(a,r,h,da=0,dr=0,dh=0,u=0.5,v=0.46,fov=60):
  return CHASE(34,2.5,26)+AIM(("P.x+Math.cos(%s+%s*T)*(%s+%s*T)"%(a,da,r,dr),"P.y+%s+%s*T"%(h,dh),"P.z+Math.sin(%s+%s*T)*(%s+%s*T)"%(a,da,r,dr)),"Head",u,v,fov)
S["KF1"]=ORB(-0.43,46,6)
S["KF2"]=ORB(-2.0,46,6)
S["DR1"]=ORB(-2.0,46,10,0.05,10,7)
S["DR2"]=ORB(-0.43,46,10,-0.05,10,7)
S["F10"]=CHASE(110,12,34)+AIM(ax("58-3*T",2.0,1.0),"Head",0.5,0.40,80)
S["F11"]=CHASE(110,12,34)+AIM(ax("58-3*T",-2.5,1.0),"Head",0.5,0.40,80)
def CHASE2(s0,vr,gap,vc):
  return ("const W7=window.__W();const nx=%f,nz=%f,gx=%f,gz=%f;const sr=%f-%f*T,sc=%f-%f-%f*T,vv=%f;"
          "const d=W7.REX.d,R=d.g;d.esc=true;R.visible=true;const rx=gx+nx*sr,rz=gz+nz*sr;R.position.set(rx,W7.GH(rx,rz)-0.15,rz);R.rotation.y=Math.atan2(-nx,-nz);"
          "if(window.__lt2!=null&&T>window.__lt2){W7.rexStep(d,(%f/6.5)/2.4*(T-window.__lt2));}window.__lt2=T;R.updateMatrixWorld(true);"
          "const g=window.__HY;const cx=gx+nx*sc,cz=gz+nz*sc,cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=Math.atan2(-nx,-nz);"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;const fx=-nx,fz=-nz,sx=-nz,sz=nx;const P={x:rx,y:W7.GH(rx,rz),z:rz};")%(NX,NZ,GX,GZ,s0,vr,s0,gap,vc,vc,vr)
S["F12"]=CHASE2(110,14,26,9)+AIM(("cx+fx*3+sx*4.5","cy+1.0","cz+fz*3+sz*4.5"),"Head",0.40,0.40,76)
S["F13"]=CHASE2(110,14,26,9)+AIM(("cx+fx*3-sx*4.5","cy+1.0","cz+fz*3-sz*4.5"),"Head",0.60,0.40,76)
S["F14"]=CHASE(110,12,30)+AIM(ax("56-3*T",6,0.7),"Head",0.62,0.40,80)
S["F15"]=CHASE(110,12,30)+AIM(ax("56-3*T",-6,0.7),"Head",0.38,0.40,80)
S["DR3"]=ORB(-0.53,66,24,0.0,4,2)
S["DR4"]=ORB(-2.1,66,24,0.06,9,6)
