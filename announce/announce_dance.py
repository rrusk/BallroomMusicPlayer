#!/usr/bin/env python

from gtts import gTTS
dances = ["Waltz", "Tango", "VienneseWaltz", "Foxtrot", "QuickStep", "WCS",
              "ChaCha", "Samba", "Rumba", "Jive"]
for dance in dances:
    if dance == "VienneseWaltz":
        dance_announced = "Viennese Waltz"
    elif dance == "QuickStep":
        dance_announced = "Quickstep"
    elif dance == "WCS":
        dance_announced = "West Coast Swing"
    elif dance == "ChaCha":
        dance_announced = "Cha Cha"
    else:
        dance_announced = dance
    tts_en = gTTS('Please get ready for ' + dance_announced, lang='en')
    with open(dance+'.mp3', 'wb') as f:
        tts_en.write_to_fp(f)
#
tts_en = gTTS('Please get ready for ', lang='en')
tts_fr = gTTS('Paso Doble', lang='es')
with open('PasoDoble.mp3', 'wb') as f:
    tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)
