import numpy as np, sys, wave
from scipy.signal import butter, sosfilt
SR=44100
def star(direction=1, seed=1):
    r=np.random.default_rng(seed); d=1.25; n=int(SR*d); x=np.arange(n)/SR
    env=np.sin(np.pi*np.minimum(1,x/d*1.15))**1.6
    noise=r.standard_normal(n)*env
    # sweeping bandpass 5200->1500 done in chunks
    out=np.zeros(n); ch=1024
    for i in range(0,n,ch):
        t=i/SR; f=5200*(1500/5200)**(t/d); bw=f/2.2
        sos=butter(2,[max(50,f-bw/2),f+bw/2],btype='band',fs=SR,output='sos')
        out[i:i+ch]=sosfilt(sos,noise[i:i+ch])
    g=np.interp(x,[0,0.22,d],[0,1,0]); out*=g; out/=np.abs(out).max()+1e-9; out*=0.8
    L=np.zeros(n);R=np.zeros(n)
    pan=np.interp(x,[0,d],[-0.7*direction,0.7*direction])
    for k in range(7):
        tk=0.12+k*0.13+r.random()*0.05; f=2600+r.random()*2200; i0=int(tk*SR); m=int(0.3*SR)
        tt=np.arange(m)/SR; fr=f*(0.94)**(tt/0.25); ph=2*np.pi*np.cumsum(fr)/SR
        a=np.minimum(tt/0.006,1)*np.exp(-tt/0.06)*0.5*(1-k/9)
        seg=np.sin(ph)*a; e=min(n,i0+m); out[i0:e]+=seg[:e-i0]
    L=out*np.sqrt((1-pan)/2); R=out*np.sqrt((1+pan)/2)
    return np.stack([L,R],1)
if __name__=="__main__":
    times=[float(v) for v in sys.argv[2].split(',')]; total=float(sys.argv[3])
    buf=np.zeros((int(SR*total)+SR,2))
    for i,t in enumerate(times):
        s=star(1 if i%2==0 else -1, i+3); i0=int(t*SR); buf[i0:i0+len(s)]+=s
    buf=buf[:int(SR*total)]; buf=np.clip(buf,-1,1)
    w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf*32767).astype('<i2').tobytes()); w.close()
