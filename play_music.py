#!/usr/bin/env python
"""
Copyright (c) 2018 [Raymond Rusk <rusk.raymond@gmail.com>]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
import time
import random
from os import walk
from os.path import expanduser
from pyfiglet import Figlet
import vlc

def is_intString(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
if len(sys.argv) > 2:
    print "Script to play dance music for practice"
    print "Usage: "+sys.argv[0]+" [number]"
    print "  [number] is musical selections per dance."
    print "  Default is 2 if no argument provided."
    exit(1)
elif len(sys.argv) == 2:
    if not is_intString(sys.argv[1]):
        print "The number of musical selection per dance must be an integer."
        exit(1)
    numSel = int(sys.argv[1])
else:
    numSel = 2

def randomList(a):
    b=[]
    for i in range(len(a)):
        element=random.choice(a)
        a.remove(element)
        b.append(element)
    return b

def displayInfo(player):
    media=player.get_media()
    media.parse()
    artist=media.get_meta(vlc.Meta.Artist) or "Unknown artist"
    title=media.get_meta(vlc.Meta.Title) or "Unknown song; title"
    album=media.get_meta(vlc.Meta.Album) or "Unknown album"
    return title+"-"+artist+"-"+album

home = expanduser("~")
musicDir=home+"/Music/"

#dances = ["QuickStep","PasoDoble","Jive"]
dances = ["Waltz","Tango","VienneseWaltz","QuickStep","WCS","ChaCha","Samba","Rumba","PasoDoble","Jive"]

fig = Figlet(font='standard')
for idx in range(len(dances)):
  dance=dances[idx]
  #print "\t\t*** "+dance.upper()+" ***"
  print fig.renderText(dance)
  musicPath=musicDir+dance
  playlist=[]
  for (dirpath, dirnames, filenames) in walk(musicPath):
    playlist.extend(filenames)
    break
  if dance=="Waltz":
      print(" [Waltz has an extra selection for volume adjustment]")
      cnt = -1
  elif dance=="PasoDoble":
      song="Get Ready for Paso.mp3"
      nextsong=dirpath+"/"+song
      player=vlc.MediaPlayer(nextsong)
      player.audio_set_volume(100)
      infoStr = displayInfo(player)
      if "Unknown" not in infoStr:
        print(infoStr)
      else:
        print(infoStr)
        #print("Filename: "+song)
      player.play()
      time.sleep(17)
      for level in range(100,10,-10):
          player.audio_set_volume(level)
          time.sleep(1)
      player.stop()
      time.sleep(5)
      cnt = numSel-1 # play only one Paso Doble
  else:
      cnt = 0
  rplaylist=randomList(playlist)
  for song in rplaylist:
    cnt = cnt + 1
    if cnt > numSel:
        break
    nextsong=dirpath+"/"+song
    player=vlc.MediaPlayer(nextsong)
    player.audio_set_volume(100)
    infoStr = displayInfo(player)
    if "Unknown" not in infoStr:
      print(infoStr)
    else:
      print(infoStr)
      #print("Filename: "+song)
    player.play()
    time.sleep(1)
    while True:
      if player.is_playing():
        continue
      else:
        break
