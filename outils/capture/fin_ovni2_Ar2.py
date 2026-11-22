import sys,math; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/rec1.py').read().split('shots=[')[0])
a0=0.75*math.pi; AX=X+math.sin(a0)*320; AZ=Z+math.cos(a0)*320
B2=G+"const a=2.25+0.22*T,d=31-4*T;return {p:[%f+d*Math.cos(a),gy+10,%f+d*Math.sin(a)],t:[%f,gy+19.25,%f],fov:62};"%(X,Z,X,Z)
dx,dz=X-AX,Z-AZ; L=math.hypot(dx,dz); sx,sz=dz/L,-dx/L; e=0.8
CX,CZ=AX+dx*e+sx*12,AZ+dz*e+sz*12
AR=G+"return {p:[%f,gy+24+95*0.2-6,%f],t:[M6.x,M6.y,M6.z],fov:58};"%(CX,CZ)
PV="const h=W6.G.ufoRide.h||0,fx=Math.sin(h),fz=Math.cos(h),sx=fz,sz=-fx,s=-0.9+1.2*T;return {p:[M6.x-fx*1.6+sx*s,M6.y+3.2,M6.z-fz*1.6+sz*s],t:[M6.x+fx*30-sx*s*2,M6.y-2.5,M6.z+fz*30-sz*s*2],fov:60};"
D3="const a=0.8+0.3*T;return {p:[M6.x+30*Math.cos(a),M6.y+2,M6.z+30*Math.sin(a)],t:[M6.x,M6.y-3,M6.z],fov:62};"
shots=[mk("warm",5.0,G+"return {p:[%f,gy+3,%f+30],t:[%f,gy+10,%f],fov:60};"%(X,Z,X,Z))]
shots.append(mk("ov2_Ar2",0.36,AR,n=48)); shots=[s for s in shots if s]
run(shots,'/root/w/fo',w=1080,h=1920)
