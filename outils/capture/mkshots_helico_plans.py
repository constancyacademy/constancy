import math
X,Z=-1040,-1765
DT=565
SH={}
SH["decollage"]=(2.0,
 "const X=%d,Z=%d,y0=LH(X,Z);const u=Math.max(0,T-0.15);const hx=X,hz=Z,hy=y0+5.0*u*u,hyaw=Math.PI+0.785,hp=0.07*Math.min(1,u),hr=0"%(X,Z),
 "const a=Math.PI/2+0.45-0.85*T;const R=19-1.5*T;return {p:[hx+R*Math.cos(a),hy+0.6+3.4*T,hz+R*Math.sin(a)],t:[hx,hy+3.0-0.6*T,hz],fov:56};")
SH["foret"]=(1.6,
 "const dx=0.57,dz=-0.82;const hx=-1270+40*T*dx,hz=-1585+40*T*dz,hy=105,hyaw=Math.atan2(dx,dz),hp=0.12,hr=0.05",
 "const sx=-dz,sz=dx;const bk=10+9*T,sd=16-7*T;return {p:[hx-dx*bk-sx*sd,hy+4,hz-dz*bk-sz*sd],t:[hx+dx*7,hy-2,hz+dz*7],fov:60};")
SH["lac"]=(1.4,
 "const hx=-1030-36*T,hz=-1915,hy=12,hyaw=-Math.PI/2,hp=0.14,hr=0",
 "return {p:[-1070+10*T,15,-1893],t:[hx-3,hy-1,hz],fov:58};")
SH["profil"]=(1.7,
 "const hx=-1030-26*T,hz=-2045,hy=70,hyaw=-Math.PI/2,hp=0.1,hr=-0.03",
 "return {p:[-1022-20*T,75,-2022],t:[hx-2,hy+5,hz],fov:58};")
SH["orbite"]=(2.2,
 "const hx=-1060-6*T,hz=-1960+2*T,hy=70,hyaw=-Math.PI/2+0.3,hp=0.05,hr=0",
 "const a=0.75+0.42*T;const R=24;return {p:[hx+R*Math.cos(a),hy+7,hz+R*Math.sin(a)],t:[hx,hy+2.5,hz],fov:60};")
