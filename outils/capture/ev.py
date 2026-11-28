import sys,json,os,time
ev=open(sys.argv[1]).read()
nm="ev%d"%int(time.time()*10); p="/root/cap/jobs/%s.json"%nm
json.dump({"out":"/root/w/sc/ev","w":540,"h":960,"shots":[],"eval":ev},open(p+".tmp","w")); os.rename(p+".tmp",p)
while not os.path.exists(p+".done"): time.sleep(1)
if os.path.exists(p+".err"): print("ERR",open(p+".err").read()[:1500])
if os.path.exists(p+".res"): print(open(p+".res").read()[:6000])
