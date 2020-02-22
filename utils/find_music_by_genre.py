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
    print()
    print("  where <source_directory> is the folder you want to search for files by musical genre.")
    print("  Will recursively check all files and directories in <source_directory> and its subdirectories.")
    print("  Musical selections will be copied to a single destination directory with a filename")
    print("  created by concatenating genre, album name, title and artist.")
    print("  Each filename starts with the genre to make it easy to identify files by genre.")
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
        # print(song)
        f = os.path.splitext(song)
        filename = f[0]
        ext = f[1]  # extension includes the last dot: i.e., .mp3, .flac, etc.
        m = vlc.Media(song)
        m.parse()
        genre = m.get_meta(vlc.Meta.Genre) or "Unknown Genre"
        artist = m.get_meta(vlc.Meta.Artist).title() or "Unknown Artist"
        album = m.get_meta(vlc.Meta.Album).title() or "Unknown Album"
        title = m.get_meta(vlc.Meta.Title).title() or f[1]
        s = genre + "-" + album + "_" + title + "_" + artist
        s = __removeIllegalChars(s)
        s = s.replace(" ", "")
        s = (s[:255]) if len(s) > 255 else s
        str = s+ext
        song2 = os.path.join(dst, str)
        if os.path.exists(song2):
            print("Filename collision for " + song2)
            print("Will append timestamp to this copy to make it unique.")
            str = s+"-"+str(datetime.now()).replace(" ", "_")+ext
            song2 = os.path.join(dst, str)
        print(song2)
        copyfile(song, song2)
