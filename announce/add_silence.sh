#!/bin/sh
for i in *.mp3; do sox "$i" "$i"new.mp3 pad 2 2; mv "$i"new.mp3 "$i" ; done
# add additional silence after PasoDoble announcement (totaling 15 sec)
sox PasoDoble.mp3 PasoDoble_new.mp3 pad 0 13
mv PasoDoble_new.mp3 PasoDoble.mp3
