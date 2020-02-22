#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#

import string
import os
import re
import sys
from shutil import copyfile
from datetime import datetime

import vlc

if len(sys.argv) != 3:
    print()
    print("Usage:", sys.argv[0], "<source_directory> <dest_directory>")
    print("")
    print("  where <source_directory> is the folder you want to search for files by musical genre.")
    print("  Will check all files and directories in <source_directory> and its subdirectories.")
    print("  Musical selections will be copied to folders in the destination directory according to genre.")
    print("  Filenames will also be modified when they contain characters that are not allowed in an NTFS")
    print("  filesystem.")
    print()
    exit()

# Set the path you want to check
src = sys.argv[1]
if not os.path.isdir(src):
    print("Directory [" + src + "] does not exist.")
    exit()

# Check that destination exists
dst = sys.argv[2]
if not os.path.isdir(dst):
    print("Directory [" + dst + "] does not exist.")
    exit()

ILLEGAL_NTFS_CHARS = "[<>:/\\|?*\"]|[\0-\31]"
def __removeIllegalChars(name):
    # removes characters that are invalid for NTFS
    return re.sub(ILLEGAL_NTFS_CHARS, "+", name)

# Check each file in subfolders
for root, dirs, files in os.walk(src):
    for name in files:
        song = os.path.join(root, name)
        #print(song)
        f = os.path.splitext(song)
        ext = f[1]
        m=vlc.Media(song)
        m.parse()
        genre = m.get_meta(vlc.Meta.Genre) or "Unknown Genre"
        artist = m.get_meta(vlc.Meta.Artist) or "Unknown Artist"
        album = m.get_meta(vlc.Meta.Album) or "Unknown Album"
        title = m.get_meta(vlc.Meta.Title) or "Unknown Title"
        artist = __removeIllegalChars(artist)
        album = __removeIllegalChars(album)
        title = __removeIllegalChars(title) + ext
        genredir = os.path.join(dst,genre)
        if not os.path.exists(genredir):
            os.mkdir(genredir)
        artistdir =  os.path.join(dst,genre,artist)
        if not os.path.exists(artistdir):
            os.mkdir(artistdir)
        albumdir = os.path.join(dst,genre,artist, album)
        if not os.path.exists(albumdir):
            os.mkdir(albumdir)
        song2 = os.path.join(dst, genre, artist, album, title)
        if os.path.exists(song2):
            print("Filename collision for " + song2)
            print("Will append timestamp to this copy to make it unique.")
            song2 = song2+"."+str(datetime.now()).replace(" ","_")
        print(song2)
        copyfile(song,song2)
