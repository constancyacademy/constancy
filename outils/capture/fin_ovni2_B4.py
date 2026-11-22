import sys; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/rec1.py').read().split('shots=[')[0])
B4=G+"const a=2.25+0.22*T,d=36-3*T;return {p:[%f+d*Math.cos(a),gy+8,%f+d*Math.sin(a)],t:[%f,gy+16.5,%f],fov:62};"%(X,Z,X,Z)
shots=[mk("warm",5.0,G+"return {p:[%f,gy+3,%f+30],t:[%f,gy+10,%f],fov:60};"%(X,Z,X,Z)), mk("ov2_B4",5.5,B4,n=48)]
run(shots,'/root/w/fo',w=1080,h=1920)
