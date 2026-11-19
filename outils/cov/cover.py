from PIL import Image, ImageDraw, ImageFont
import numpy as np
F='/tmp/fnt/ebg.ttf'
COL=(242,240,236); GREY=(133,132,130)
def render(lines,W=1080,H=1920,size=77,lh=1.18,cy=None,brand=True,brand_y=None,bsize=29,scale=1.0):
    im=Image.new('RGB',(W,H),(0,0,0)); d=ImageDraw.Draw(im)
    fo=ImageFont.truetype(F,size,layout_engine=ImageFont.Layout.RAQM)
    asc,desc=fo.getmetrics()
    L=size*lh
    n=len(lines); cy=H/2 if cy is None else cy
    # block of n lines, each line box height L; baseline at top + (L-(asc+desc))/2 + asc
    top=cy-n*L/2
    for i,t in enumerate(lines):
        w=d.textlength(t,font=fo,features=['lnum'])
        y=top+i*L+(L-(asc+desc))/2
        d.text(((W-w)/2,y),t,font=fo,fill=COL,features=['lnum'])
    if brand:
        fb=ImageFont.truetype(F,bsize,layout_engine=ImageFont.Layout.RAQM)
        w=d.textlength('Constancy',font=fb); a2,d2=fb.getmetrics()
        by=brand_y if brand_y is not None else H-240
        d.text(((W-w)/2,by-(a2+d2)/2),'Constancy',font=fb,fill=GREY)
    return im
def bbox_rows(im):
    a=np.array(im.convert('L'))>40
    rows=np.where(a.any(1))[0]; g=[];s=rows[0];p=rows[0]
    for r in rows[1:]:
        if r>p+5:g.append((s,p));s=r
        p=r
    g.append((s,p)); out=[]
    for x,y in g:
        c=np.where(a[x:y+1].any(0))[0]; out.append((x,y,c.min(),c.max()))
    return out
