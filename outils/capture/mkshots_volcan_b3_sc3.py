exec(open('/root/w/sc2.py').read().split('\nshots=')[0])
S["d1"]=TP(45,150,20,25,100,55)
S["d2"]=TP(30,150,20,25,100,55)
S["d3"]=TP(45,130,40,30,115,58)
S["d4"]=TP(60,150,15,30,100,55)
S["e1"]=TP(80,176,2.2,8,126,22)
S["e2"]=TP(80,176,2.2,12,132,20)
S["e3"]=TP(80,176,2.2,6,124,28)
S["e4"]=TP(80,176,2.2,14,136,26)
shots=[MK(k,S[k]) for k in sys.argv[2].split(',')]
for s in shots: s["fps"]=60; s["n"]=int(sys.argv[3]) if len(sys.argv)>3 else 1
print(run(shots,sys.argv[1],w=540,h=960))
