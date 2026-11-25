# povparachute_b3 (jeu. 26/11 12h, M2 POV) · reconstruction de la session perdue · base mkshots_povparachute_b1.py
import os,math,sys
exec(open('/root/cap/lib212.py').read())
exec(open('/home/claude/rushes/outils/capture/mkshots_povparachute_b1.py').read())
# CAMX : caméra lissée autour du perso · angle (expression JS, T = temps du plan) relatif au cap du perso, distance d, hauteur hg, visée td sous le perso
def CAMX(a="2.2",d=9.0,hg=4.0,td=3.0,fov=62,k=0.35,tx=0.0):
  return ("const W=window.__W(),g=W.G;let ax,ay,az,h;if(g.para){ax=g.me.x;ay=g.para.alt+1.2;az=g.me.z;h=g.me.h;}else{ax=g.car.x;ay=(g.car.alt||0);az=g.car.z;h=g.car.h;}"
    "let S=window.__CS;if(!S||Math.hypot(ax-S.x,ay-S.y,az-S.z)>40){S=window.__CS={x:ax,y:ay,z:az,h:h};}S.x+=(ax-S.x)*%f;S.y+=(ay-S.y)*%f;S.z+=(az-S.z)*%f;S.h+=(h-S.h)*%f;"
    "const a=(%s),d=%f;const fx=Math.sin(S.h),fz=Math.cos(S.h);return {p:[S.x-Math.sin(S.h+a)*d,S.y+(%f),S.z-Math.cos(S.h+a)*d],t:[S.x+fx*(%f),S.y-(%f),S.z+fz*(%f)],fov:%f};")%(k,k,k,k,a,d,hg,tx,td,tx,fov)
def MKQ(name,cam,n=1,toff=0.0,fps=60,pre=1,setup=None):
  s=MKP(name,setup or SETUP(430,150,-math.pi/2,180),cam,n=n); s["fps"]=fps; s["pre"]=pre; s["toff"]=toff; return s
# CAMW : caméra rigide autour du perso, angle MONDE th (expression JS) : caméra = perso + (cos th, sin th) × d, hauteur ref + hg, visée ref − td
def CAMW(th="0",d=12.0,hg=6.0,td=-2.0,fov=62):
  return ("const W=window.__W(),g=W.G;let ax,ay,az;if(g.para){ax=g.me.x;ay=g.para.alt+1.2;az=g.me.z;}else{ax=g.car.x;ay=(g.car.alt||0);az=g.car.z;}"
    "const th=(%s);return {p:[ax+Math.cos(th)*%f,ay+(%f),az+Math.sin(th)*%f],t:[ax,ay-(%f),az],fov:%f};")%(th,d,hg,d,td,fov)
SU=SETUP(200,150,math.pi/2,180)
CA=CAMX("2.6",13,8,-2,62,k=1)
CD=CAMX("1.9",9,16,-1,64,k=1)
CE=CAMX("1.75+0.22*T",24,3,-0.2,56,k=1)
CO=CAMW("1.06-0.75*(T-5.0)",13,6,-2,62)
# exec(open('/root/w/para/mk.py').read())
# LOGC="if(Math.round(T*60)%30==0)console.log('LOG '+[window.__shotN,T.toFixed(3),(g.para?g.para.alt:-1).toFixed(2),g.me.x.toFixed(1),g.me.z.toFixed(1),g.onFoot].join(' '));"
# def LG(c,nm): return c.replace("const W=window.__W(),g=W.G;","const W=window.__W(),g=W.G;window.__shotN='%s';"%nm+LOGC,1)
# CD2=CAMX("3.0",11,13,-1,64,k=1)
# CO2=CAMW("0.16+0.75*(T-5.0)",13,6,-2,62)
# CA2=CAMX("2.6",13,8,-2,62,k=1)
# sel=os.environ.get("SEL","x,A,D,O,E").split(",")
# D={"x":MKQ("x",CA2,toff=0.05,setup=SU),
#    "A":MKQ("pA",LG(CA2,"A"),n=110,toff=0.15,setup=SU),
#    "D":MKQ("pD",LG(CD2,"D"),n=96,toff=2.3,setup=SU),
#    "O":MKQ("pO",LG(CO2,"O"),n=84,toff=4.9,setup=SU),
#    "E":MKQ("pE",LG(CE,"E"),n=208,toff=2.1,setup=SU)}
# print(run([D[k] for k in sel],"/root/w/para/fin",w=1080,h=1920,name=os.environ.get("JN","fin1")))
# exec(open('/root/w/para/fin.py').read().split("sel=")[0])
# CO3=CAMW("0.23+0.75*(T-2.9)",14,3,-1.5,62)
# print(run([MKQ("x2",CA2,toff=0.05,setup=SU),MKQ("pO2",LG(CO3,"O2"),n=84,toff=2.8,setup=SU)],"/root/w/para/fin",w=1080,h=1920,name="fin3",wait=False))
