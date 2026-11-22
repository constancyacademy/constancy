import sys; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/rec1.py').read().split('shots=[')[0])
B4=G+"const a=2.25+0.22*T,d=36-3*T;return {p:[%f+d*Math.cos(a),gy+8,%f+d*Math.sin(a)],t:[%f,gy+16.5,%f],fov:62};"%(X,Z,X,Z)
s=shot("ov2_B4pre",B4,dayT=840,n=15,toff=-0.5,wait=1200,js=setup(5.5),pre=PRE+CLOUD); s["far"]=20000; s.pop("toff",None)
s["camjs"]=s["camjs"]  # toff already baked into camjs
shots=[mk("warm",5.0,G+"return {p:[%f,gy+3,%f+30],t:[%f,gy+10,%f],fov:60};"%(X,Z,X,Z)), s]
run(shots,'/root/w/fo',w=1080,h=1920)
