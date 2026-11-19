import sys,re,json
from cover import *
NB=' '
def prep(s):
    s=s.replace("'", "’")
    s=re.sub(r' ([?!:;€$])', NB+r'\1', s)
    s=s.replace('GTA 6','GTA'+NB+'6').replace('GTA 1','GTA'+NB+'1')
    s=re.sub(r'(\d) (\d{3})', r'\1'+NB+r'\2', s); s=re.sub(r'(\d) (\d{3})', r'\1'+NB+r'\2', s)
    s=re.sub(r'(\d) (ans|semaine|jours|€)', r'\1'+NB+r'\2', s)
    return s
fo=ImageFont.truetype(F,78,layout_engine=ImageFont.Layout.RAQM)
d=ImageDraw.Draw(Image.new('RGB',(10,10)))
W=lambda t:d.textlength(t.replace(NB,' '),font=fo,features=['lnum'])
MAXW=830
def wrap(sent):
    words=sent.split(' ')
    if W(sent)<=MAXW: return [sent]
    best=None
    # try 2 or 3 lines, minimize max width difference
    import itertools
    n=len(words)
    for k in (2,3):
        for cuts in itertools.combinations(range(1,n),k-1):
            parts=[' '.join(words[a:b]) for a,b in zip((0,)+cuts,cuts+(n,))]
            ws=[W(p) for p in parts]
            if max(ws)>MAXW: continue
            STOP={'de','la','le','les','à','a','un','une','et','en','des','du','sur','au','aux','ma','ta','sa','mon','ton','son','qui','que','ne','se','ce','j’ai','il','tu','je','on','dans','pour','par','gta'}
            pen=sum(900 for pp in parts[:-1] if pp.split(' ')[-1].lower().replace(NB,' ').split(' ')[-1] in STOP)
            score=max(ws)-min(ws)+pen+ (0 if k==2 else 300)
            if best is None or score<best[0]: best=(score,parts)
        pass
    return best[1]
def lines_for(text):
    sents=re.findall(r'[^.?!]+[.?!]+', text) or [text]
    out=[]
    for s in sents: out+=wrap(prep(s.strip()))
    return out
if __name__=='__main__':
    jobs=json.load(open(sys.argv[1]))
    for name,text in jobs.items():
        L=lines_for(text)
        im=render([l for l in L],size=78,lh=1.185,cy=960.5,bsize=30,brand_y=1680)
        im.save(f'out/{name}.png'); print(name,L)
