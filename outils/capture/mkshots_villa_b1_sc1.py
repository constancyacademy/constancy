exec(open('/home/claude/rushes/outils/capture/mkshots_villa_reperage_lib2.py').read())
import math
HL={};EXT={}
cx,cz=-VX,-VZ  # direction to city center from villa
cl=math.hypot(cx,cz); ux,uz=cx/cl,cz/cl
S["A1"]=L(V(0,1.0,60),V(0,3,0),50); EXT["A1"]=1
S["A2"]=L(V(0,1.0,60),V(0,3,0),50)
S["A3"]=L(V(30,12,45),V(0,2,0),50)
S["A4"]=L(V(30,12,45),V(0,2,0),50); EXT["A4"]=1
S["I1"]=L(V(-5.0,1.6,-5.4),V(-3,1.3,7),70); HL["I1"]=0.45
S["I2"]=L(V(0,1.6,-6.2),V(0,1.2,10),72); HL["I2"]=0.45
S["I3"]=L(V(9.5,1.7,-5.5),V(-4,1.0,4),72); HL["I3"]=0.45
S["I6"]=L(V(-9,1.6,6.2),V(8,1.4,-2),70); HL["I6"]=0.45
S["C1"]=L(V(0,2.0,9),V("%f"%(ux*400),"20","%f"%(uz*400)),60); HL["C1"]=0.45
S["C2"]=L(V(0,8,20),V("%f"%(ux*1500),"60","%f"%(uz*1500)),55); EXT["C2"]=1
names=sys.argv[2].split(',')
shots=[MK("x",L(V(0,30,60),V(0,0,0),60))]+[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
for s in shots: s["fps"]=60; s["n"]=1
print(run(shots,sys.argv[1],w=540,h=960))
