exec(open('/root/w/vi/sc7.py').read().split('\nnames=')[0])
S["V1"]=AP(150,50,18,2.2,0.6,3.0,50); F["V1"]=96
S["V2"]=L(V("-6.4+2.4*T",1.6,"-5.8+0.8*T"),V("-3.5+1.6*T",1.25,7),68); HL["V2"]=0.22; F["V2"]=84
S["V4"]=L(V("-(%f)*(8+10*T)"%c,"4+22*T","-(%f)*(8+10*T)+9"%s),V("%f"%(c*1700),"35+5*T","%f"%(s*1700)),"(56+4*T)"); HL["V4"]=0.3; F["V4"]=90
names=sys.argv[2].split(',')
shots=[MKI("x",S["V1"],hl=0.3)]+[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
shots[0]["fps"]=60; shots[0]["n"]=1
for sh,k in zip(shots[1:],names): sh["fps"]=60; sh["n"]=F[k]
print(run(shots,sys.argv[1],w=1080,h=1920))
