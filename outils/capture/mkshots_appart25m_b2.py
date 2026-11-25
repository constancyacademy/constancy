import os,math,sys
exec(open('/root/cap/lib212.py').read())
exec(open('/home/claude/rushes/outils/capture/mkshots_appart25m_b1.py').read())
P=lambda pre: "const U=T-%f;"%((pre+1)/60.0)
# BURSTL : fusée du jeu qui éclate à l'instant U voulu, position en coordonnées LOCALES du penthouse
def BURSTL(x,y,z,t,key,c=(1,.8,.5)):
  return ("{const F=window.__FW,g=window.__APG;if(F&&F.pos&&g&&U>=%f&&!window.%s){window.%s=1;const A=g.localToWorld(new THREE.Vector3(%f,%f,%f));const i=F.i=(F.i+1)%%F.n,k=i*3;F.pos[k]=A.x;F.pos[k+1]=A.y;F.pos[k+2]=A.z;F.v[k]=0;F.v[k+1]=0.5;F.v[k+2]=0;F.life[i]=F.max[i]=0.02;F.base[k]=%f;F.base[k+1]=%f;F.base[k+2]=%f;F.kind[i]=1;F.sz[i]=1.4;}}")%(t,key,key,x,y,z,c[0],c[1],c[2])
RB="if(T<0.2){window.__b1=0;window.__b2=0;window.__b3=0;window.__b4=0;}"
def MK6(name,body,n=1,pre=150,wait=3000):
  s=MK(name,body,n=n,js=NEAR,wait=wait); s["fps"]=60; s["pre"]=pre; return s
# BURSTC : gerbe posée directement (sans fusée), couleurs choisies (rose, or), position LOCALE du penthouse, à l'instant U
def BURSTC(x,y,z,t,key,c1=(1,.45,.8),c2=(1,.75,.25),n=190,spd=52,ring=0):
  return ("{const F=window.__FW,g=window.__APG;if(F&&F.pos&&g&&U>=%f&&!window.%s){window.%s=1;const A=g.localToWorld(new THREE.Vector3(%f,%f,%f));"
          "const c1=[%f,%f,%f],c2=[%f,%f,%f],N=%d,S=%f;for(let q=0;q<N;q++){let dx,dy,dz;if(%d){const a=q/N*6.283;dx=Math.cos(a);dy=Math.sin(a)*0.3;dz=Math.sin(a);}else{dy=Math.random()*2-1;const a=Math.random()*6.283,r=Math.sqrt(1-dy*dy);dx=Math.cos(a)*r;dz=Math.sin(a)*r;}"
          "const cc=q%%2?c1:c2,s=S*(0.85+Math.random()*0.2);const i=F.i=(F.i+1)%%F.n,k=i*3;F.pos[k]=A.x;F.pos[k+1]=A.y;F.pos[k+2]=A.z;F.v[k]=dx*s;F.v[k+1]=dy*s;F.v[k+2]=dz*s;F.life[i]=F.max[i]=(1.8+Math.random())*1.25;"
          "F.base[k]=cc[0];F.base[k+1]=cc[1];F.base[k+2]=cc[2];F.kind[i]=2;F.sz[i]=3.2*1.37;}F.flash=Math.max(F.flash||0,0.3);}}")%(t,key,key,x,y,z,c1[0],c1[1],c1[2],c2[0],c2[1],c2[2],n,spd,ring)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
# BURSTW : gerbe en coordonnées MONDE
def BURSTW(x,y,z,t,key,c1=(1,.45,.8),c2=(1,.75,.25),n=200,spd=52,sz=4.4):
  return BURSTC(x,y,z,t,key,c1,c2,n,spd).replace("const A=g.localToWorld(new THREE.Vector3(%f,%f,%f));"%(x,y,z),"const A={x:%f,y:%f,z:%f};"%(x,y,z)).replace("F.sz[i]=3.2*1.37","F.sz[i]=%f"%sz)
PK=(1,.45,.8); GD=(1,.75,.25); CY=(.35,.8,1); RD=(1,.25,.35)
def BW(*bs): return RB+"".join(BURSTW(*b) for b in bs)
def SH(name,body,pre=150,n=1,toff=0.0):
  s=MK6(name,P(pre)+body,n=n,pre=pre); s["toff"]=toff; return s
S={}
S["F1"]=BW((-60,345,10,0.0,"__b1",PK,GD),(-10,370,-100,0.15,"__b2",GD,PK),(-110,330,-40,0.7,"__b3",CY,PK),(0,380,40,1.3,"__b4",RD,GD))+L(("110-11*U","300.5-0.6*U","-62+8*U"),("58","300","-27"),55)
S["B"]=BW((230,318,-55,0.0,"__b1",PK,GD),(205,306,5,0.25,"__b2",GD,PK),(260,328,-20,0.8,"__b3",CY,PK))+L(("64.0+0.9*U","297.6","-28.1"),("200","256","-28"),70)
S["E"]=BW((-40,350,40,0.0,"__b1",GD,PK),(10,375,-80,0.6,"__b2",PK,CY),(-90,335,-20,1.3,"__b3",RD,GD))+L(("96-1.5*U","307-0.3*U","6-2*U"),("58","293","-28"),56)
S["B2"]=BW((230,318,-55,0.0,"__b1",PK,GD),(205,306,5,0.25,"__b2",GD,PK),(260,328,-20,0.8,"__b3",CY,PK))+L(("63.8+1.07*U","299.5","-28.1"),("200","250","-28"),70)
# exec(open('/root/w/m4/mk4.py').read())
# sh=[SH("x",S["F1"],pre=60),SH("aF1",S["F1"],pre=60,n=126),SH("aB",S["B2"],pre=60,n=96),SH("aE",S["E"],pre=60,n=144)]
# print(run(sh,"/root/w/m4/fin",w=1080,h=1920,name="m4fin",wait=False))
