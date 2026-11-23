# scouting: python3 sc.py file.py key1,key2 [toffs] [dayT]  -> renders single frames 1080x1920, prints contact sheet path
import sys,os,json,subprocess,glob,time
exec(open('/root/cap/lib212.py').read())
exec(open(sys.argv[1]).read())
sel=sys.argv[2].split(','); toffs=[float(x) for x in (sys.argv[3] if len(sys.argv)>3 else "0").split(',')]
out="/root/w/sc/%d"%int(time.time()); os.makedirs(out,exist_ok=True)
sh=[MK("w",S[sel[0]],wait=1500)]
for k in sel:
  for t in toffs: sh.append(MK("%s_%02d"%(k,int(round(t*10))),S[k],o=t))
r=run(sh,out,w=1080,h=1920,name="sc%d"%int(time.time()*10))
fs=[f for f in sorted(glob.glob(out+"/*.png")) if not os.path.basename(f).startswith("w_")]
lab=[os.path.basename(f)[:-8] for f in fs]
cmd=["ffmpeg","-loglevel","error","-y"]
for f in fs: cmd+=["-i",f]
n=len(fs); cols=min(n,4)
fc="".join("[%d]scale=270:480,drawtext=text='%s':x=5:y=5:fontsize=22:fontcolor=yellow:box=1:boxcolor=black[v%d];"%(i,lab[i],i) for i in range(n))
rows=(n+cols-1)//cols
fc+="".join("[v%d]"%i for i in range(n))
if n>1: fc+="xstack=inputs=%d:layout=%s:fill=gray[o]"%(n,"|".join("%d_%d"%((i%cols)*270,(i//cols)*480) for i in range(n)))
else: fc+="null[o]"
subprocess.run(cmd+["-filter_complex",fc,"-map","[o]",out+"/sheet.png"])
print(out+"/sheet.png", r if not isinstance(r,str) else "")
