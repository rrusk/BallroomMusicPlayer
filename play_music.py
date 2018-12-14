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
import os
from os import walk
from os.path import expanduser
from pyfiglet import Figlet
import vlc

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def display_exception():
    import sys
    print sys.exc_info()[0]
    import traceback
    print traceback.format_exc()
    print "Press Enter to continue ..." 
    raw_input() 
        
def is_intString(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

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
    info = title+"-"+artist+"-"+album
    return info.encode('ascii','ignore') # remove non-printable characters

def play_music(numSel, firstDance):
    numSel = numSel
    home = expanduser("~")
    musicDir=home+"/Music/"

    dances = ["Waltz","Tango","VienneseWaltz","Foxtrot","QuickStep","WCS","ChaCha","Samba","Rumba","PasoDoble","Jive"]

    idx = -1
    danceFound = False
    for dance in dances:
        idx = idx + 1
        if not dance.startswith(firstDance):
            continue
        else:
            danceFound = True
            break

    if not danceFound:
        print(" Dance not found!!!")
        continueYN = raw_input("Hit carriage return to exit and rerun program.")
        exit()
    else:
        dances = dances[idx:]
        
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
        if len(playlist) < numSel:
            print("There are fewer than " + str(numSel) + " selections in " + musicPath + " folder.")
            continueYN = raw_input("Continue? <Y/N> ")
            if continueYN == 'N' or continueYN == 'n':
               exit()
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
            #time.sleep(5)
            try:
                skipYN = raw_input("Skip Paso Doble <Y/N>: ")
                if skipYN == 'Y' or skipYN == 'y':
                    cnt = numSel
                else:
                    cnt = numSel-1 # play only one Paso Doble
            except Exception:
                print("Exception reading input.")
                display_exception()
                continue
        else:
            cnt = 0
        rplaylist=randomList(playlist)
        for song in rplaylist:
            cnt = cnt + 1
            if cnt > numSel:
                break
            #print("Filename: "+song)
            nextsong=dirpath+"/"+song
            player=vlc.MediaPlayer(nextsong)
            player.audio_set_volume(100)
            infoStr = displayInfo(player)
            print(infoStr)
            try:
                #raise ValueError("A test exception was raised")
                player.play()
            except Exception:
                print "*** Exception occurred ***"
                display_exception()
                continue
            time.sleep(1)
            while True:
                if player.is_playing():
                    time.sleep(1) # sleep awhile to reduce CPU usage
                    continue
                else:
                    break

if __name__=='__main__':
    try:
        fig = Figlet(font='standard')
        print fig.renderText("MusicPlayer")

        defaultsYN = raw_input("Play two selections per dance starting with Waltz <Y/N>: ")
        if defaultsYN == 'N' or defaultsYN == 'n':
            while True:
                numSel = raw_input("Enter number of selections to play per dance: ")
                if numSel.lower() == 'q':
                    exit()
                try:
                    numSel = int(numSel)
                    break
                except ValueError:
                    print("The input must be an integer.  Please try again or enter 'q' to exit.")
            
            print ("First dance?")
            print (" [W]altz")
            print (" [T]ango")
            print (" [V]iennese Waltz")
            print (" [F]oxtrot")
            print (" [Q]uickstep")
            print (" [WCS]")
            print (" [C]ha Cha")
            print (" [S]amba")
            print (" [R]umba")
            print (" [P]aso Doble")
            print (" [J]ive")
            while True:
                firstDance = raw_input("First dance <W/T/V/F/Q/WCS/C/S/R/P/J> or enter 'x' to e[x]it: ")
                firstDance = firstDance.upper()
                if firstDance == 'X':
                    exit()
                elif firstDance not in ('W','T','V','F','Q','WCS','C','S','R','P','J'):
                    print("Unrecognized dance input.  Please try again.")
                else:
                    break
        else:
            numSel = 2
            firstDance = 'W'
        clearScreen()
        play_music(numSel, firstDance)
    except Exception:
        display_exception()
