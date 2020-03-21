# BallroomMusicPlayer

A simple Ballroom Dance media player written in Python and based on
libvlc: https://wiki.videolan.org/python_bindings.  The Python
bindings API documentation is at
https://www.olivieraubert.net/vlc/python-ctypes/doc/.

Tested on Ubuntu 18.04, 14.04 and 64-bit Windows 7, 8.1, 10 with
64-bit versions of Python 2.7.15 and Python 3.8.2.  Use the 2to3 branch
with Python 3.  Also, for Windows with Python 3.8+, the location of the
libvlc.dll file must be specified.  See the comment near the top of the
play_music.py script.

If using Ubuntu, install vlc using 'sudo apt install vlc'.  Then
install python-vlc using 'pip install python-vlc'.  For Python 3 you
may need to use pip3.  FIGlet is used for dance banners;
install pyfiglet using `pip install pyfiglet'. Mutagen
is used to determine the length of musical selections.  Install it
using `pip install mutagen`.

If using Windows, install the 64-bit version of VLC from
https://www.videolan.org/vlc/ and the latest 64-bit Python 2 or 3 release
from https://www.python.org/downloads/windows/.  Do a custom installation,
for all users and make sure Python is added to your path during installation.
Then open a Command Prompt window and enter:
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
