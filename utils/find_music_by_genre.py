#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#

import string
import os
import re
import sys
from shutil import copyfile

import vlc

if len(sys.argv) != 3:
    print()
    print("Usage:", sys.argv[0], "<source_directory> <dest_directory")
    print("  where <directory> is the folder you want to search for files by musical genre.")
    print("  Will check all files and directories in <directory> and its subdirectories.")
    print("  Musical selections will be copied to destination directory with a filename")
    print("  created by concatenating genre, album name, title and artist.")
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
        m=vlc.Media(song)
        m.parse()
        genre = m.get_meta(vlc.Meta.Genre)
        if genre:
            artist = m.get_meta(vlc.Meta.Artist).title()
            album = m.get_meta(vlc.Meta.Album).title()
            title = m.get_meta(vlc.Meta.Title).title()
            s = genre + "-" + album + "_" + title + "_" + artist
            s = __removeIllegalChars(s)
            s = s.replace(" ","")
            s = (s[:255]) if len(s) > 255 else s
            f = os.path.splitext(song)
            ext = f[1]
            s = s+ext
            #print(song)
            song2 = os.path.join(dst, s)
            #print(song2)
            copyfile(song,song2)
