exec(open('/root/w/vi/sc6.py').read().split('\nnames=')[0])
a=math.atan2(-VZ,-VX); c,s=math.cos(a),math.sin(a)
F={}
S["V1"]=L(V("1.5-1.0*T","-1.0+0.35*T","72-24*T"),V(0,1.6,0),48); HL["V1"]=0.3; F["V1"]=96
S["V2"]=L(V("-5.6+1.3*T",1.6,"-5.6+0.4*T"),V("-3+0.6*T",1.25,7),70); HL["V2"]=0.22; F["V2"]=84
S["V3"]=L(V("-15+5*T","5.5-0.8*T","25-2*T"),V("0+2*T",0.5,5),55); HL["V3"]=0.25; F["V3"]=84
S["V4"]=L(V("-%f*(8+10*T)"%c,"4+22*T","-%f*(8+10*T)+9"%s),V("%f"%(c*1700),"35+5*T","%f"%(s*1700)),"(56+4*T)"); HL["V4"]=0.3; F["V4"]=90
S["V5"]=L(V("-9+0.9*T",1.6,"6.2-0.3*T"),V("8",1.3,"-2+1.2*T"),70); HL["V5"]=0.22; F["V5"]=130
names=sys.argv[2].split(',')
shots=[MKI("x",S["V1"],hl=0.3)]+[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
shots[0]["fps"]=60; shots[0]["n"]=1
for sh,k in zip(shots[1:],names): sh["fps"]=60; sh["n"]=F[k]
print(run(shots,sys.argv[1],w=1080,h=1920))
