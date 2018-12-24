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
import os
import random
import time

# import curses

if os.name == "nt":
    import keyboard
else:
    import keypoller

import vlc
from pyfiglet import Figlet

"""
The ballroom dance music is assumed to be organized so that the music
for each dance is in a separate directory:

$HOME/Music/
|--- ChaCha
|--- Foxtrot
|--- Jive
|--- LineDance
|--- PasoDoble
|--- QuickStep
|--- Rumba
|--- Samba
|--- Tango
|--- VienneseWaltz
|--- Waltz
|--- WCS
"""


# def my_wrapper(func, *args, **kwds):
#     """Wrapper function that initializes curses and calls another function,
#     restoring normal keyboard/screen behavior on error.
#     The callable object 'func' is then passed the main window 'stdscr'
#     as its first argument, followed by any other arguments passed to
#     wrapper().
#     """
#
#     try:
#         # Initialize curses
#         curses.filter()
#         stdscr = curses.initscr()
#         # Turn off echoing of keys, and enter cbreak mode,
#         # where no buffering is performed on keyboard input
#         curses.noecho()
#         curses.cbreak()
#
#         # In keypad mode, escape sequences for special keys
#         # (like the cursor keys) will be interpreted and
#         # a special value like curses.KEY_LEFT will be returned
#         stdscr.keypad(1)
#
#         # Start color, too.  Harmless if the terminal doesn't have
#         # color; user can test with has_color() later on.  The try/catch
#         # works around a minor bit of over-conscientiousness in the curses
#         # module -- the error return from C start_color() is ignorable.
#         try:
#             # curses.start_color()
#             pass
#         except:
#             pass
#
#         return func(stdscr, *args, **kwds)
#     finally:
#         # Set everything back to normal
#         if 'stdscr' in locals():
#             stdscr.keypad(0)
#             curses.echo()
#             curses.nocbreak()
#             curses.endwin()


def getMusicDir():
    home = os.path.expanduser("~")
    return os.path.join(home, u"Music")  # Make sure filenames are utf-8 encoded
    # return os.path.join(home, u"Downloads", u"Music", u"WF")


def getDances():
    dances = ["Waltz", "Tango", "VienneseWaltz", "Foxtrot", "QuickStep", "WCS",
              "ChaCha", "Samba", "Rumba", "PasoDoble", "Jive"]
    return dances


def availableMusicByDance():
    musicDir = getMusicDir()
    dances = getDances()
    musicList = []
    for idx in range(len(dances)):
        dance = dances[idx]
        musicPath = os.path.join(musicDir, dance)
        playlist = []
        if not os.path.isdir(musicPath):
            print("WARNING: The directory " + musicPath + " does not exist.")
        else:
            for (dirpath, dirnames, filenames) in os.walk(musicPath):
                for name in filenames:
                    playlist.append(os.path.join(dirpath, name))
        musicList.append(playlist)
    return musicList


def randomList(a):
    b = []
    for i in range(len(a)):
        element = random.choice(a)
        a.remove(element)
        b.append(element)
    return b


def randomizeMusicByDance(musicList):
    rMusicList = []
    for dance in musicList:
        rMusicList.append(randomList(dance))
    return rMusicList


def validMusicLists(musicL):
    result = True
    for idx in range(len(getDances())):
        for musicfile in musicL[idx]:
            if os.path.isfile(musicfile) and os.access(musicfile, os.R_OK):
                continue
            else:
                print("File {} doesn't exist or isn't readable".format(musicfile))
                result = False
    return result


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def mediaInfo(player):
    media = player.get_media()
    if media is not None:
        media.parse()
        title = media.get_meta(vlc.Meta.Title) or "Unknown song; title"
        artist = media.get_meta(vlc.Meta.Artist) or "Unknown artist"
        album = media.get_meta(vlc.Meta.Album) or "Unknown album"
        return "{:<60}  {:<20}  {:<20}".format(title.encode('ascii', 'ignore'),
                                               artist.encode('ascii', 'ignore'),
                                               album.encode('ascii', 'ignore'))
    else:
        return ""


def getIndexFirstDance(theFirstDance):
    dances = getDances()
    idx = -1
    i = -1
    danceFound = False
    for dance in dances:
        i = i + 1
        if not dance.startswith(theFirstDance):
            continue
        else:
            danceFound = True
            break
    if danceFound:
        idx = i
    return idx


# def monitor_keypresses(stdscr, player):
#     stdscr.nodelay(True)
#     stdscr.clear()  # doesn't seem to have any effect
#     curses.noecho()  # doesn't seem to work
#     stdscr.idcok(False)
#     stdscr.idlok(False)
#     try:
#         key = stdscr.getkey()
#         if key == " ":  # pause music
#             player.pause()
#             stdscr.erase()  # probably not useful
#         if key == 'n':  # next selection; i.e., stop playing current selection
#             player.stop()
#             stdscr.erase  # probably not useful
#     except Exception as e:
#         # No input
#         pass
#     return True


def play_music(theNumSel, offset, theFirstDance, danceMusic):
    idx = getIndexFirstDance(theFirstDance)
    if idx < 0:
        print(" Dance not found!!!")
        raw_input("Hit carriage return to exit and rerun program.")
        exit()
    myFig = Figlet(font='standard')
    dances = getDances()
    for i in range(idx, len(dances)):
        dance = dances[i]
        print myFig.renderText(dance)

        if theNumSel + offset > len(danceMusic[i]):
            print("There are fewer than " + str(theNumSel + offset) + " selections in the "
                  + os.path.join(getMusicDir(), dance) + " folder.")
            continueYN = raw_input("Continue? <Y/N> ")
            if continueYN == 'N' or continueYN == 'n':
                exit()
        playlist = danceMusic[i][offset:]  # music for dance using offset to skip selections previously played

        if dance == "Waltz":
            if offset == 0:  # at beginning of practice session
                print("[Waltz will have an extra selection for volume adjustment]")
                numPlayed = -1
            else:  # on second or later sessions
                # volume adjustment increased number previously selected for Waltz by 1
                playlist = playlist[1:]
                numPlayed = 0
        elif dance == "PasoDoble":
            nextsong = os.path.join(getMusicDir(), dance, "Get Ready for Paso.mp3")
            if not os.path.isfile(nextsong) or not os.access(nextsong, os.R_OK):
                print("File {} doesn't exist or isn't readable".format(nextsong))
            else:
                player = vlc.MediaPlayer(nextsong)
                player.audio_set_volume(100)
                print mediaInfo(player)
                player.play()
                time.sleep(17)
                for level in range(100, 10, -10):
                    player.audio_set_volume(level)
                    time.sleep(1)
                player.stop()
            try:
                while True:
                    skipYN = raw_input("Skip Paso Doble <Y/N>: ")
                    if skipYN.upper() not in ('Y', 'N'):
                        print("Unrecognized input.  Enter either 'Y' or 'N'.")
                    else:
                        break
                if skipYN.upper() == 'Y':
                    numPlayed = theNumSel
                else:
                    numPlayed = theNumSel - 1  # play only one Paso Doble
            except Exception:
                print("Exception reading input.")
                display_exception()
                continue
        else:
            numPlayed = 0

        for song in playlist:
            numPlayed = numPlayed + 1
            if numPlayed > theNumSel:
                break
            try:
                player = vlc.MediaPlayer(song)
                player.audio_set_volume(100)
                infoStr = mediaInfo(player)
                print(infoStr)
                playing = player.play()
                if playing == -1:
                    print "Failed to play selection."
                    numPlayed = numPlayed - 1
            except Exception:
                print "*** Exception occurred ***"
                display_exception()
                numPlayed = numPlayed - 1
                continue
            time.sleep(1)
            if os.name != 'nt':
                with keypoller.KeyPoller() as keyPoller:
                    while True:
                        # my_wrapper(monitor_keypresses, player)
                        c = keyPoller.poll()
                        while keyPoller.poll() is not None:
                            continue  # discard rest of characters after first
                        if not c is None:
                            if c == " ":
                                player.pause()
                            elif c == "n":
                                player.stop()
                            else:
                                pass
                        if player.is_playing() or player.get_state() == vlc.State.Paused:
                            time.sleep(1)  # sleep awhile to reduce CPU usage
                            continue
                        else:
                            break
            else:
                def on_press_reaction(event):
                    if event.name == 'space':
                        player.pause()
                    elif event.name == 'n':
                        player.stop()

                keyboard.on_press(on_press_reaction)
                while True:
                    # my_wrapper(monitor_keypresses, player)
                    if player.is_playing() or player.get_state() == vlc.State.Paused:
                        time.sleep(1)  # sleep awhile to reduce CPU usage
                        continue
                    else:
                        break


if __name__ == '__main__':
    try:
        fig = Figlet(font='standard')
        print fig.renderText("MusicPlayer")

        theMusic = availableMusicByDance()
        musicLists = randomizeMusicByDance(theMusic)
        if not validMusicLists(musicLists):
            print("Continuing but there may be problems...")

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
                elif firstDance not in ('W', 'T', 'V', 'F', 'Q', 'WCS', 'C', 'S', 'R', 'P', 'J'):
                    print("Unrecognized dance selection.  Please try again.")
                else:
                    break
        else:
            numSel = 2
            firstDance = 'W'
        clearScreen()
        play_music(numSel, 0, firstDance, musicLists)
        print
        while True:
            continueYN = raw_input("At end of playlist.  Begin another playlist starting with Waltz <Y/N>: ")
            continueYN = continueYN.upper()
            if continueYN not in ('Y', 'N'):
                print "Unrecognized input.  Try again."
            else:
                break
        if continueYN == 'Y':
            print
            play_music(numSel, numSel, 'W', musicLists)
            print
        else:
            raw_input("Enter carriage return to exit program...")
            exit()

        raw_input("At end of second playlist.  Press Enter to exit...")

    except Exception:
        display_exception()
