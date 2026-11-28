exec(open('/root/w/vi/b2s.py').read().split('\nnames=')[0])
S["K5"]=L(V("0.5-6*T",2.3,-3.5),V("-1-9*T",2.0,7),66)
S["K6"]=L(V("1-6*T",2.3,-4.5),V("-1.5-7*T",2.2,7),64)
S["K7"]=L(V("-0.5-5*T",2.1,-2.5),V("-2.5-7*T",2.1,7),66)
for k in ("K5","K6","K7"): HL[k]=0.22
names=sys.argv[2].split(',')
offs=[float(x) for x in sys.argv[3].split(',')]
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  for o in offs:
    sh=MKI(k+"o%02d"%int(round(o*10)),S[k],o=o,hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
