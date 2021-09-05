#!/usr/bin/env python

from gtts import gTTS
dances = ["Waltz", "Tango", "VWSlow", "VienneseWaltz", "Foxtrot", "QuickStep", "WCS",
              "ChaCha", "Samba", "Rumba", "JSlow", "Jive"]
for dance in dances:
    if dance == "VWSlow":
        dance_announced = "Slow Viennese Waltz"
    elif dance == "VienneseWaltz":
        dance_announced = "Viennese Waltz"
    elif dance == "QuickStep":
        dance_announced = "Quickstep"
    elif dance == "WCS":
        dance_announced = "West Coast Swing"
    elif dance == "ChaCha":
        dance_announced = "Cha Cha"
    elif dance == "JSlow":
        dance_announced = "Slow Jive"
    else:
        dance_announced = dance
    tts_en1 = gTTS('  Please get ready for ' + dance_announced, lang='en')
    tts_en2 = gTTS('  Be ready with your partner for ' + dance_announced, lang='en')
    with open(dance+'.mp3', 'wb') as f:
        tts_en1.write_to_fp(f)
        tts_en2.write_to_fp(f)
#
tts_en1 = gTTS('Please get ready for ', lang='en')
tts_es1 = gTTS('Paso Doble', lang='es')
tts_en2 = gTTS('Be ready with your partner for ', lang='en')
tts_es2 = gTTS('Paso Doble', lang='es')
with open('PasoDoble.mp3', 'wb') as f:
    tts_en1.write_to_fp(f)
    tts_es1.write_to_fp(f)
    tts_en2.write_to_fp(f)
    tts_es2.write_to_fp(f)
