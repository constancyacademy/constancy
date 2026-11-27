import sys,os,time
exec(open('/root/w/rx/lib.py').read())
exec(open(sys.argv[1]).read())
out=sys.argv[2]; os.makedirs(out,exist_ok=True)
sh=[]
for it in sys.argv[3].split(','):
  nm,k,n,pre=it.split(':'); s=MK(nm,S[k],n=int(n)); s["fps"]=60; s["pre"]=int(pre); sh.append(s)
print(run(sh,out,w=1080,h=1920,name="fin%d"%int(time.time()*10),wait=False))
