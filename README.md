# BallroomMusicPlayer

A simple Ballroom Dance media player based on libvlc:
https://wiki.videolan.org/python_bindings.

Tested on Ubuntu 18.04 with python 2.7.15rc1.

To use, install vlc using 'sudo apt install vlc'.
Then install python-vlc using 'pip install python-vlc'.
FIGlet is used for dance banners, install pyfiglet using `pip install pyfiglet'.

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
