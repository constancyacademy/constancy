import subprocess as _sp; _sp.run(['bash','/home/claude/rushes/outils/verrou.sh','rafraichir'])
import json, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
spec=json.load(open(sys.argv[1]))
W,H=1080,1920
SRC='/root/monteur/src/'
FG='/tmp/fnt/ebg700.ttf'; FG6='/tmp/fnt/ebg600.ttf'; FI='/tmp/fnt/inter600.ttf'; FE='/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
work='/root/monteur/tmp_'+spec['id']; os.makedirs(work,exist_ok=True)
WIN={'T':(0,816),'B':(1075,845),'B2':(1040,880),'F':(0,1920)}
def bandeau(path):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    f1=ImageFont.truetype(FG6,92); f2=ImageFont.truetype(FI,40)
    t1='constancy.fr'; t2='Gratuit · Sans téléchargement'
    b1=d.textbbox((0,0),t1,font=f1); b2=d.textbbox((0,0),t2,font=f2)
    w=max(b1[2]-b1[0],b2[2]-b2[0])+110; h=(b1[3]-b1[1])+(b2[3]-b2[1])+92
    cy=int(H*spec.get('band_cy',0.735)); x0=(W-w)//2; y0=cy-h//2
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+8,x0+w,y0+h+8),radius=36,fill=(0,0,0,120))
    im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(14))); d=ImageDraw.Draw(im)
    d.rounded_rectangle((x0,y0,x0+w,y0+h),radius=36,fill=(12,10,16,220),outline=(255,63,164,255),width=5)
    y=y0+26; d.text(((W-(b1[2]-b1[0]))//2-b1[0],y-b1[1]),t1,font=f1,fill=(255,255,255,255))
    y+=(b1[3]-b1[1])+22; d.text(((W-(b2[2]-b2[0]))//2-b2[0],y-b2[1]),t2,font=f2,fill=(201,185,138,255))
    im.save(path)
def wrap(d,txt,font,maxw):
    if '\n' in txt: return [l for p in txt.split('\n') for l in wrap(d,p,font,maxw)]
    words=txt.split(' '); lines=[]; cur=''
    for w_ in words:
        t=(cur+' '+w_).strip()
        if d.textlength(t,font=font)>maxw and cur: lines.append(cur); cur=w_
        else: cur=t
    lines.append(cur)
    if len(lines)==2:
        best=None
        for i in range(1,len(words)):
            a=' '.join(words[:i]); b=' '.join(words[i:])
            m=max(d.textlength(a,font=font),d.textlength(b,font=font))
            last=words[i-1].lower().strip(',')
            pen=0
            if last in ('de','la','le','les','à','a','un','une','et','en','des','du','sur','au','aux','ma','ta','sa','mon','ton','son','qui','que','ne','se','ce','j\'ai','il','tu','je','on','dans','pour','par'): pen+=400
            if words[i-1].endswith(','): pen-=60
            if words[i-1] in ('GTA',) : pen+=1000
            if m<=maxw and (best is None or m+pen<best[0]): best=(m+pen,[a,b])
        if best: lines=best[1]
    return lines
def text_png(txt,path,sub=None,emoji=None):
    txt=txt.replace('5 000 $','5\u00a0000\u00a0$').replace(' €','\u00a0€').replace(' ?','\u00a0?').replace(' :','\u00a0:').replace(' !','\u00a0!')
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    for fsz in ((spec['nl_fsz'],) if ('\n' in txt and spec.get('nl_fsz')) else (96,88,80,74)):
        font=ImageFont.truetype(FG,fsz); lh=int(fsz*1.08)
        lines=wrap(d,txt,font,960)
        if len(lines)<=2: break
    fs=ImageFont.truetype(FG6,52) if sub else None
    total=lh*len(lines)+(70 if sub else 0)
    y0=int(H*spec.get('text_cy',0.205))-total//2
    items=[]
    for i,l in enumerate(lines):
        tw=d.textlength(l,font=font); ew=0
        if emoji and i==len(lines)-1: ew=100
        items.append((l,font,(W-tw-ew)/2,y0+i*lh,ew))
    if sub:
        tw=d.textlength(sub,font=fs); items.append((sub,fs,(W-tw)/2,y0+lh*len(lines)+10,0))
    if spec.get('text_plate'):
        bx0=min(x for (l,f,x,y,ew) in items)-44; bx1=max(x+d.textlength(l,font=f)+ew for (l,f,x,y,ew) in items)+44
        by0=items[0][3]-26; by1=items[-1][3]+int(items[-1][1].size*1.08)+30
        pl=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(pl).rounded_rectangle((bx0,by0,bx1,by1),radius=34,fill=(10,8,16,spec['text_plate']))
        im=Image.alpha_composite(im,pl); d=ImageDraw.Draw(im)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for (l,f,x,y,ew) in items: ds.text((x+3,y+6),l,font=f,fill=(0,0,0,220))
    im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(6))); d=ImageDraw.Draw(im)
    for (l,f,x,y,ew) in items:
        d.text((x,y),l,font=f,fill=(255,255,255,255),stroke_width=2,stroke_fill=(15,10,25,255))
        if ew:
            ef=ImageFont.truetype(FE,109); e=Image.new('RGBA',(140,140),(0,0,0,0)); ImageDraw.Draw(e).text((0,0),emoji,font=ef,embedded_color=True)
            e=e.crop(e.getbbox()).resize((86,86)); tw=d.textlength(l,font=f); im.alpha_composite(e,(int(x+tw+22),int(y+20)))
            d=ImageDraw.Draw(im)
    im.save(path)
bandeau(work+'/band.png')
segs=[s if len(s)>5 else s+[1.0] for s in spec['segs']]; total=sum((s[2]-s[1])/s[5] for s in segs)
srcs=sorted(set(s[0] for s in segs)); 
def build(texts,out):
    inputs=[]
    for s in srcs: inputs+=['-i',SRC+s+'.mp4']
    inputs+=['-i',work+'/band.png']; bi=len(srcs)
    fc=[]
    for i,(s,a,b,win,xo,sp,*rest) in enumerate(segs):
        hf=bool(rest and 'h' in rest[0])
        if isinstance(win,list): x,y,w,h=win
        else:
            y,h=WIN[win]; w=int(h*9/16)//2*2; x=int(xo*(W-w))
        fc.append(f'[{srcs.index(s)}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,unsharp=5:5:0.5,setsar=1,fps=30'+(',hflip' if hf else '')+f'[s{i}]')
    fc.append(''.join(f'[s{i}]' for i in range(len(segs)))+f'concat=n={len(segs)}:v=1:a=0[c]')
    last='c'; k=bi+1
    if spec.get('music'):
        mj=json.load(open('/root/monteur/mus/'+spec['music']+'.json'))
        bts=[b for b in mj['beats'] if b<total]
        if spec.get('beat_every',1)>1: bts=bts[::spec['beat_every']]
        E='+'.join(f'exp(-(t-{b})/0.085)*gte(t,{b})' for b in bts) or '0'
        A=spec.get('shake',26); Wb=int(W*1.06)//2*2; Hb=int(H*1.06)//2*2
        fc.append(f"[c]scale={Wb}:{Hb},crop={W}:{H}:x='(iw-ow)/2+{A}*({E})*sin(t*93)':y='(ih-oh)/2+{A}*({E})*cos(t*71)',eq=brightness='0.07*({E})':eval=frame[cv]"); last='cv'
    if 'overlay_seq' in spec:
        inputs+=['-framerate','30','-i',spec['overlay_seq']+'/f%04d.png']
        fc.append(f'[{last}][{k}:v]overlay=0:0:shortest=0[cs]'); last='cs'; k+=1
    for j,t in enumerate(texts):
        p=f'{work}/{os.path.basename(out)}_t{j}.png'; text_png(t[2],p,t[3] if len(t)>3 else None,t[4] if len(t)>4 else None); inputs+=['-i',p]
        fc.append(f"[{last}][{k}:v]overlay=0:0:enable='between(t,{t[0]},{t[1]})'[o{j}]"); last=f'o{j}'; k+=1
    fc.append(f'[{last}][{bi}:v]overlay=0:0,format=yuv420p[vo]')
    if 'audio_file' in spec:
        inputs+=['-i',spec['audio_file']]; asrc=k; a0=spec.get('audio_start',0)
    else:
        asrc=srcs.index(spec.get('audio',segs[0][0])); a0=0
    fc.append(f'[{asrc}:a]atrim={a0}:{a0+total},asetpts=PTS-STARTPTS,afade=t=out:st={max(total-spec.get('fade',0.6),0)}:d={spec.get('fade',0.6)}[ao]')
    cmd=['ffmpeg','-v','error','-y']+inputs+['-filter_complex',';'.join(fc),'-map','[vo]','-map','[ao]','-c:v','libx264','-preset','veryfast','-crf','21','-c:a','aac','-b:a','160k','-movflags','+faststart',out]
    subprocess.run(cmd,check=True)
ABO=spec.get('abo_sub','Abonne-toi : Une nouveauté chaque jour.')
for ver in (('q','jeu','yt') if spec.get('abo') else ('q','jeu')):
    tt=[]
    for t in spec['texts']:
        if t[2]=='@Q':
            if ver=='q': tt.append([t[0],t[1],spec['question']]+([ABO] if spec.get('abo') else []))
            elif ver=='yt': tt.append([t[0],t[1],'Abonne-toi',spec.get('yt_sub','Une nouveauté chaque jour.'),'🔔'])
            else: tt.append([t[0],t[1],spec['jeu_text']] if spec.get('jeu_text') else [t[0],t[1],'Commente JEU','Le lien du jeu en message privé','🎁'])
        else: tt.append(t)
    out=f"/root/monteur/out/reel_{spec['id']}_{spec.get('ver','b7')}_{ver}.mp4"; os.makedirs('/root/monteur/out',exist_ok=True)
    build(tt,out); print('OK',ver,round(total,2))
