#!/bin/sh
for i in *.mp3; do sox "$i" "$i"new.mp3 pad 2 2; mv "$i"new.mp3 "$i" ; done
