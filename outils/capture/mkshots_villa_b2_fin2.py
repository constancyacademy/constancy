exec(open('/root/w/vi/b2fin.py').read().split('\nnames=')[0])
S["G1"]=AQ(166,-20,46,12,1.8,0.8,3.0,50,tp=0.3); F["G1"]=110
names=sys.argv[2].split(',')
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  sh=MKI(k,S[k],hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=F[k]; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
