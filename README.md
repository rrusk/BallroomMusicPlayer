# BallroomMusicPlayer

A simple Ballroom Dance media player written in Python and based on
libvlc: https://wiki.videolan.org/python_bindings.  The Python
bindings API documentation is at
https://www.olivieraubert.net/vlc/python-ctypes/doc/.

Tested on Ubuntu 18.04, 14.04 and Windows 10 with python 2.7.15.

If using Ubuntu, install vlc using 'sudo apt install vlc'.  Then
install python-vlc using 'pip install python-vlc'.  FIGlet is used for
dance banners; install pyfiglet using `pip install pyfiglet'.

If using Windows, install VLC from https://www.videolan.org/vlc/ and
the latest Python 2 release from
https://www.python.org/downloads/windows/.  Make sure Python is added
to your path during installation.  Then open a Command Prompt window
and enter "pip install python-vlc" and "pip install pyfiglet".  The
program can then be ran from the command line using "python
play_music.py".  It is also clickable from the GUI.

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
