import sys,json; sys.path.insert(0,'/root/cap'); from h import *
ev=open(sys.argv[1]).read()
print(json.dumps(run([],"/root/w/ev",w=540,h=960,ev=ev,name="ev%d"%int(time.time()*10))))
