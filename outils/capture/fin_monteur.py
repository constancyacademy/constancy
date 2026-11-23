# final render: python3 fin.py file.py outdir name:key:n:toff[,…]
import sys,os,time
exec(open('/root/cap/lib212.py').read())
exec(open(sys.argv[1]).read())
out=sys.argv[2]; os.makedirs(out,exist_ok=True)
sh=[MK("w",S[sys.argv[3].split(',')[0].split(':')[1]],wait=1500)]
for it in sys.argv[3].split(','):
  nm,k,n,o=it.split(':'); sh.append(MK(nm,S[k],n=int(n),o=float(o),wait=int(os.environ.get("WAIT","3000"))))
print(run(sh,out,w=1080,h=1920,name=os.environ.get("JN","fin%d"%int(time.time()*10)),wait=False))
