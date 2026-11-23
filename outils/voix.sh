#!/bin/bash
# voix.sh in.mp4 voix.mp3 S E out.mp4 SPLIT GAIN_dB
# phrase (avant SPLIT dans le fichier) remontée de GAIN dB (gain simple), « Constancy dot F R » et sa réverbération intacts
IN=$1; V=$2; S=$3; E=$4; OUT=$5; SP=${6:-0}; GD=${7:-0}
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
D=$(python3 -c "print(int(round($S*1000)))"); G=$(python3 -c "print(round(10**($GD/20),4))")
FO=$(python3 -c "print(round($T-0.5,3))")
ffmpeg -v error -y -i "$IN" -i "$V" -filter_complex "[0:a]volume='1-0.8*clip((t-($S-0.25))/0.25,0,1)*clip((($E+0.4)-t)/0.4,0,1)':eval=frame[m];[1:a]volume='if(lt(t,$SP),$G,1)':eval=frame,adelay=$D|$D[v];[m][v]amix=inputs=2:normalize=0:duration=first,afade=t=in:st=0:d=0.03,afade=t=out:st=$FO:d=0.5[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$OUT"
echo "$OUT T=$T S=$S E=$E"
