import math,sys; sys.path.insert(0,'/root/cap/lib'); from cl import *
def carjs(X0,V,Z,ry=math.pi/2):
  # moves window.__PC[0] along x ; returns cx
  return "const W7=window.__W();const g=window.__PC[0];const cx=%f+%f*T;g.position.set(cx,0,%f);g.rotation.y=%f;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"%(X0,V*(1 if ry>0 else -1),Z,ry,V)
CAR=lambda X0,Z,ry=math.pi/2: notraf+place([("gt",X0,Z,ry)])+"window.__lt=null;"
LZ=-52.4
SA=carjs(-70,24,LZ)+"const k=Math.min(1,T/1.3);const of=7.5-5*k;return {p:[cx+of,0.55,-49.3],t:[cx+0.8,0.75,%f],fov:55};"%LZ
SC=carjs(-30,24,LZ)+"const a=0.25*T;return {p:[cx-7+3*T,21-2*T,%f+2.5],t:[cx+9,0,%f],fov:62};"%(LZ,LZ-1)
SE=carjs(-40,24,LZ)+"return {p:[cx+1.2-1.0*T,0.5,%f-5.8],t:[cx+1.2-1.0*T,0.75,%f],fov:50};"%(LZ,LZ)
SA=carjs(-74,24,LZ)+"const k=Math.min(1,Math.max(0,T/1.8));const of=8-4*k;return {p:[cx+of,0.55,-49.4],t:[cx+0.6,0.8,%f],fov:52};"%LZ
SE=carjs(-40,24,LZ)+"return {p:[cx+1.5-1.2*T,0.9,%f-9.5],t:[cx+1.5-1.2*T,1.2,%f+2],fov:44};"%(LZ,LZ)
CZ=-115.5
SB="return {p:[-70-7*T,3.2,-103],t:[-82-7*T*0.5,3.6,-125],fov:52};"
SD=carjs(-62,22,CZ,-math.pi/2)+"return {p:[-80-2*T,2.4,-100],t:[cx-2,1.2,%f],fov:50};"%CZ
SE=carjs(-40,24,LZ)+"return {p:[cx+0.4-0.8*T,1.0,%f-13],t:[cx+0.4-0.8*T,1.0,%f+2],fov:46};"%(LZ,LZ)
SB="return {p:[-101+5*T,7,-107],t:[-87.5+2*T,1.6,-123.5],fov:50};"
SE=carjs(-40,24,LZ)+"return {p:[cx+0.4-0.8*T,0.7,%f-13.5],t:[cx+0.4-0.8*T,2.3,%f+2],fov:46};"%(LZ,LZ)
SB="return {p:[-77-5*T,9.5,-111.5],t:[-88-3*T,1.2,-123.6],fov:50};"
SE2="return {p:[-20-14*T,1.5,-56],t:[-26-14*T,2.6,-44],fov:52};"
SB2="return {p:[-76-5*T,3.5,-108],t:[-84-2*T,4.2,-125],fov:48};"
PX,PY,PZ=-84.9,143.8,-83.2
SP1="return {p:[%f+14-3*T,%f+2.2,%f+10],t:[%f-12,%f-1,%f-8],fov:55};"%(PX,PY,PZ,PX,PY,PZ)
SP2="return {p:[%f-14+3*T,%f+2.2,%f-10],t:[%f+12,%f-1,%f+8],fov:55};"%(PX,PY,PZ,PX,PY,PZ)
SP3="return {p:[%f+10,%f+2.2,%f-14+3*T],t:[%f-8,%f-1,%f+12],fov:55};"%(PX,PY,PZ,PX,PY,PZ)
# D2 : la GT ralentit devant le club (20 -> 6 m/s sur 1,7 s), camera dans la rue
SD2=("const W7=window.__W();const g=window.__PC[0];const TT=Math.max(0,T);const v=Math.max(6,20-8.2*TT);const s=TT<1.707?20*TT-4.1*TT*TT:20*1.707-4.1*1.707*1.707+6*(TT-1.707);"
 "const cx=-61-s;g.position.set(cx,0,%f);g.rotation.y=-Math.PI/2;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,v,0,T-window.__lt);}window.__lt=T;"
 "const tx=-84+(cx+84)*0.55;return {p:[-76-3*TT,2.3,-104.6],t:[tx,2.0,-118],fov:50};")%CZ
SD3=SD2.replace("return {p:[-76-3*TT,2.3,-104.6],t:[tx,2.0,-118],fov:50};","return {p:[-76-3*TT,4.6,-104.6],t:[tx,2.4,-118],fov:54};")
SD4=SD2.replace("return {p:[-76-3*TT,2.3,-104.6],t:[tx,2.0,-118],fov:50};","return {p:[-76-3*TT,1.6,-104.6],t:[tx,1.2,-118],fov:62};")
