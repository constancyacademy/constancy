import sys,os,time
sys.path.insert(0,'/root/cap')
exec(open('/root/cap/lib212.py').read())
exec(open(sys.argv[1]).read())
out=sys.argv[2]; os.makedirs(out,exist_ok=True)
items=[x.split(':') for x in sys.argv[3].split(',')]
sh=[]
for nm,k,n,pre in items:
  s=MK(nm,S[k],n=int(n),js=NEAR,wait=3000); s["fps"]=60; s["pre"]=int(pre); sh.append(s)
print(run(sh,out,w=1080,h=1920,name=os.environ.get("JN","fin%d"%int(time.time()*10)),wait=False))
