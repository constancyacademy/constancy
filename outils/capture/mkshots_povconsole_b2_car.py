import sys; sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/home/claude/rushes/outils/capture/mkshots_povconsole_repérage.py').read().split('if __name__')[0])
X=-40; DT=560
NO=CLOUD+open("/root/w/noufo.js").read()+"{if(window.__HM)window.__HM.visible=false;}"
pre=notraf+place([("or",X-30,LZ,math.pi/2)])+"window.__lt=null;"
body=carjs(X-22,30,LZ)+"const u=Math.max(0,T-0.68);const cmx=%f+25*u*u;const cy=0.38+0.5*Math.min(1,u*2);const dd=Math.max(4,Math.abs(cx-cmx));return {p:[cmx,cy,%f-3.0],t:[cx+(cx>cmx?2.5:0),0.75+0.06*dd,%f],fov:55};"%(X,LZ,LZ)
s=shot("pov3_car",body,dayT=DT,n=58,toff=0,wait=4000,js=NO+pre); s["far"]=20000
print(run([shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=DT),s],'/root/w/pv5',w=1080,h=1920,wait=False))
