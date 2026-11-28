exec(open('/root/w/vi/b2fin3.py').read().split('\nnames=')[0])
S["R1"]=L(V("0.5-5.5*T",2.4,-2.5),V(-4.9,1.2,7),66)
S["R2"]=L(V("0.5-5.5*T",2.2,-3.0),V(-4.9,1.6,7),64)
S["R3"]=L(V("1.0-6*T",2.6,-2.0),V("-4.9-0.8*T",1.4,8),68)
for k in ("R1","R2","R3"): HL[k]=0.22
names=sys.argv[2].split(',')
offs=[float(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else [0]
W_=int(os.environ.get("WW","540")); H_=int(W_*16/9)
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  for o in offs:
    sh=MKI(k+"o%02d"%int(round(o*10)),S[k],o=o,hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=W_,h=H_))
