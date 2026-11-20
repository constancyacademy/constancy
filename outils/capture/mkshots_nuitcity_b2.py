import math,sys; sys.path.insert(0,'/root/cap/lib'); from p1 import *
def CARX(cid,X0,Z,ry=math.pi/2): return notraf+place([(cid,X0,Z,ry)])+"window.__lt=null;"
NOSPIN=lambda s: s.replace("W7.spinWheels(","(()=>0)(")
# file du club devant la porte, cote +x (videur a 1.55,0.75 local)
QUEUE="{const W2=window.__W();const C=W2.CLUB;if(C.ppl){C.ppl.forEach((h,k)=>{if(k==0)return;h.position.set(2.5+(k-1)*0.85,0,1.05+((k%2)?0.12:-0.08));h.rotation.y=Math.PI/2+((k%3)-1)*0.35;});}}"
SB3="return {p:[-70-4*T,3.0,-108],t:[-81-2*T,2.5,-125],fov:50};"
SD5=("const W7=window.__W();const g=window.__PC[0];const TT=Math.max(0,T);const v=Math.max(10,20-5.9*TT);const s=TT<1.695?20*TT-2.95*TT*TT:20*1.695-2.95*1.695*1.695+10*(TT-1.695);"
 "const cx=-61-s;g.position.set(cx,0,%f);g.rotation.y=-Math.PI/2;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,v,0,T-window.__lt);}window.__lt=T;"
 "const tx=-84+(cx+84)*0.55;return {p:[-76-3*TT,1.6,-104.6],t:[tx,1.2,-118],fov:62};")%CZ
SD6=SD5.replace("t:[tx,1.2,-118],fov:62","t:[tx,1.85,-118],fov:62")
