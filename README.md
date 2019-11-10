# BallroomMusicPlayer

A simple Ballroom Dance media player written in Python and based on
libvlc: https://wiki.videolan.org/python_bindings.  The Python
bindings API documentation is at
https://www.olivieraubert.net/vlc/python-ctypes/doc/.

Tested on Ubuntu 18.04, 14.04 and 64-bit Windows 7, 8.1, 10 with
python 2.7.15.

If using Ubuntu, install vlc using 'sudo apt install vlc'.  Then
install python-vlc using 'pip install python-vlc'.  FIGlet is used for
dance banners; install pyfiglet using `pip install pyfiglet'. Mutagen
is used to determine the length of musical selections.  Install it
using `pip install mutagen`.

If using Windows, install the 64-bit version of VLC from
https://www.videolan.org/vlc/ and the latest 64-bit Python 2.7 release
from https://www.python.org/downloads/windows/.  Make sure Python is
added to your path during installation. (It is the last item in the
"Customize Python 2.7.15" list. Select "Entire feature will be
installed on local hard drive".) Then open a Command Prompt window and
enter:
<pre>
pip install python-vlc pyfiglet windows-curses keyboard mutagen
</pre>
(If "pip" isn't found, log out or restart Windows so that the Python
binaries are added to your environment variables.)  The program can
then be ran from the command line using "python play_music.py".  It is
also clickable from the GUI.

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

To pause music press spacebar.  The music can be resumed by pressing
the spacebar again.  To skip to the next selection press 'n'.

WINDOWS BUG FIX: (seen in Windows 8.1, Windows 10)

It appears that libvlc has a bug related to changing between daylight
standard time and daylight saving time.  After both the spring and
fall time change, libvlc complains that the plugin cache is stale.
The error message begins with "main libvlc error: stale plugins cache:
modified c:\".  After many warnings BallroomMusicPlay will continue.
VLC provides an executable to update the plugin cache timestamps.  To
run it, execute "resolve-stale-plugins.bat" from this repository as
Administrator.

<pre>
TODO:
Implement GUI
</pre>
