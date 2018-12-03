# BallroomMusicPlayer

A simple Ballroom Dance media player written in Python and based on
libvlc: https://wiki.videolan.org/python_bindings.  The Python
bindings API documentation is at
https://www.olivieraubert.net/vlc/python-ctypes/doc/.

Tested on Ubuntu 18.04, 14.04 and 64-bit Windows 7, 10 with python 2.7.15.

If using Ubuntu, install vlc using 'sudo apt install vlc'.  Then
install python-vlc using 'pip install python-vlc'.  FIGlet is used for
dance banners; install pyfiglet using `pip install pyfiglet'.

If using Windows, install 64-bit VLC from
https://www.videolan.org/vlc/ and the latest 64-bit Python 2 release
from https://www.python.org/downloads/windows/.  Make sure Python is
added to your path during installation. (It is the last item in the
"Customize Python 2.7.15" list. Select "Entire feature will be
installed on local hard drive".) Then open a Command Prompt window and
enter "pip install python-vlc", "pip install pyfiglet" and "pip
install windows-curses".  The program can then be ran from the command
line using "python play_music.py".  It is also clickable from the GUI.

The player assumes the following music organization:
<pre>
$HOME/Music/
├── ChaCha
├── Foxtrot
├── Jive
├── LineDance
├── PasoDoble
├── QuickStep
├── Rumba
├── Samba
├── Tango
├── VienneseWaltz
├── Waltz
└── WCS
</pre>

The musical selections are assumed to be at the correct tempo and to
be of appropriate length.  The volume of the musical selections should
be normalized.

<pre>
TODO:
Port to Windows
Implement GUI
Add controls to pause, restart, go to next select, delete selection, quit, etc.
</pre>
