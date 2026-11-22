import sys; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/rec1.py').read().split('shots=[')[0])
PF="const h=W6.G.ufoRide.h||0,a=h-0.18+0.30*T,d=6.85-0.6*T;return {p:[M6.x+Math.sin(a)*d,M6.y+3.3,M6.z+Math.cos(a)*d],t:[M6.x,M6.y+2.6,M6.z],fov:46};"
shots=[mk("warm",5.0,G+"return {p:[%f,gy+3,%f+30],t:[%f,gy+10,%f],fov:60};"%(X,Z,X,Z)), mk("ov2_PF3",ARR+18.3,PF,n=48)]
run(shots,'/root/w/fo',w=1080,h=1920)
