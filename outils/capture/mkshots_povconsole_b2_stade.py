import sys; sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/home/claude/rushes/outils/capture/mkshots_povconsole_repérage.py').read().split('if __name__')[0])
NO=CLOUD+open("/root/w/noufo.js").read()+"{if(window.__PC)window.__PC.forEach(g=>g.visible=false);}"
SB="const U=T+0.38;return {p:[-175+80-48*U,24-6*U,985+49.6-10*U],t:[-175+6.4,18,985-10.2],fov:60};"
s2=shot("pov4_stade",SB,dayT=560,n=40,wait=4000,js=NO+"{if(window.__HM)window.__HM.visible=false;}"); s2["far"]=20000
print(run([s2],'/root/w/pv8',w=1080,h=1920,wait=False))
