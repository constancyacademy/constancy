#!/bin/bash
# voix2.sh in.mp4 voix.mp3 S E out.mp4 SPLIT GAIN_dB  (règle 28 de l'expert, 23/11 21h05)
# Musique à 0,2 de S jusqu'à E, puis descend encore (×MEND en RD s) : plus aucune remontée, la queue de « Constancy dot F R » est le son le plus fort de la dernière seconde.
# Phrase (avant SPLIT) remontée de GAIN dB par simple gain, « Constancy dot F R » et sa réverbération intacts, fondu de sortie 0,4 s.
IN=$1; V=$2; S=$3; E=$4; OUT=$5; SP=${6:-0}; GD=${7:-0}; MEND=${MEND:-0.12}
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
D=$(python3 -c "print(int(round($S*1000)))"); G=$(python3 -c "print(round(10**($GD/20),4))")
FO=$(python3 -c "print(round($T-0.4,3))")
M="(1-0.8*clip((t-($S-0.25))/0.25,0,1))*(1-(1-$MEND)*clip((t-$E)/${RD:-0.6},0,1))"
ffmpeg -v error -y -i "$IN" -i "$V" -filter_complex "[0:a]volume='$M':eval=frame[m];[1:a]volume='if(lt(t,$SP),$G,1)':eval=frame,adelay=$D|$D[v];[m][v]amix=inputs=2:normalize=0:duration=first,afade=t=in:st=0:d=0.03,afade=t=out:st=$FO:d=0.4[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$OUT"
# contrôle : niveaux séparés dans la dernière seconde
ffmpeg -v error -y -i "$IN" -filter_complex "[0:a]volume='$M':eval=frame,atrim=$(python3 -c "print($T-1)"):$T[m]" -map "[m]" /tmp/_m.wav
ffmpeg -v error -y -i "$V" -filter_complex "[0:a]volume='if(lt(t,$SP),$G,1)':eval=frame,adelay=$D|$D,apad,atrim=0:$T,atrim=$(python3 -c "print($T-1)"):$T[v]" -map "[v]" /tmp/_v.wav
python3 - <<PY
import numpy as np,subprocess
def rms(f):
  a=subprocess.run(["ffmpeg","-v","error","-i",f,"-f","f32le","-ac","1","-"],capture_output=True).stdout
  x=np.frombuffer(a,np.float32); return 20*np.log10(np.sqrt((x**2).mean())+1e-9), len(x)
m=rms("/tmp/_m.wav"); v=rms("/tmp/_v.wav")
print("DERNIERE SECONDE : musique %.1f dB · voix seule %.1f dB · écart voix-musique %+.1f dB"%(m[0],v[0],v[0]-m[0]))
PY
echo "$OUT T=$T S=$S E=$E"
