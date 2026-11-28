exec(open('/root/w/vi/sc8.py').read().split('\nnames=')[0])
shots=[MKI("x",S["Q2"],hl=0.3),MKI("Q2",ORB(94,12,40,16,0,55),hl=0.3)]
shots[0]["fps"]=60; shots[0]["n"]=1; shots[1]["fps"]=60; shots[1]["n"]=120
print(run(shots,sys.argv[1],w=1080,h=1920))
