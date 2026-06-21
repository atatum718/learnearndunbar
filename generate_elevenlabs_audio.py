#!/usr/bin/env python3
"""
Generate TTS audio for all balloon quotes using ElevenLabs API.
Run this on your local computer after installing:
  pip install elevenlabs

Then run:
  python3 generate_elevenlabs_audio.py

It will create an 'audio/' folder with all MP3 files.
Upload those files to: learnearndunbar/images/audio/
Then let Manus know and the balloons will be wired to play on click.
"""

import os
from elevenlabs import ElevenLabs

# Your ElevenLabs API key
API_KEY = "sk_ab19b27fb65eb4ca0c4c48275e52b7a6f10936473e409822"

# Voice IDs for teen-sounding voices (ElevenLabs built-in)
# "Elli" and "Rachel" sound younger and warm
# You can browse more at: https://elevenlabs.io/voice-library
VOICE_FEMALE = "EXAVITQu4vr4xnSDxMaL"  # Bella - warm, young female
VOICE_MALE   = "ErXwobaYiN019PkySvjV"  # Antoni - warm, young male

client = ElevenLabs(api_key=API_KEY)

output_dir = "audio"
os.makedirs(output_dir, exist_ok=True)

# Voices from the Heart quotes
voices_from_heart = [
    ("vfh_01", "Save my money.", VOICE_FEMALE),
    ("vfh_02", "It allowed me to save up.", VOICE_MALE),
    ("vfh_03", "It helped me get better at saving my money.", VOICE_FEMALE),
    ("vfh_04", "It helped me provide for myself independently.", VOICE_MALE),
    ("vfh_05", "I was able to pay for my end-of-year trip and school supplies.", VOICE_FEMALE),
    ("vfh_06", "It helped me put more money toward college.", VOICE_MALE),
    ("vfh_07", "I was able to pay for many senior activities on my own.", VOICE_FEMALE),
    ("vfh_08", "I was able to get food for me and my family.", VOICE_MALE),
    ("vfh_09", "I've been able to budget better.", VOICE_FEMALE),
    ("vfh_10", "I am saving for college.", VOICE_MALE),
    ("vfh_11", "Help with household bills.", VOICE_FEMALE),
    ("vfh_12", "The extra earnings helped me pay for personal expenses and learn how to manage my finances.", VOICE_MALE),
    ("vfh_13", "The money I earned helped me push my snack business and save.", VOICE_FEMALE),
    ("vfh_14", "It allowed me to give money to my mom.", VOICE_MALE),
    ("vfh_15", "It allowed me to buy the things I want and need, go out, and gain independence.", VOICE_FEMALE),
    ("vfh_16", "Pay for my phone bill.", VOICE_MALE),
    ("vfh_17", "It allowed me to provide for my family.", VOICE_FEMALE),
    ("vfh_18", "It allowed me to treat my mom.", VOICE_MALE),
    ("vfh_19", "The money allowed me to save up for important things.", VOICE_FEMALE),
    ("vfh_20", "It allowed me to work on my money management early.", VOICE_MALE),
    ("vfh_21", "The earnings allowed me to invest.", VOICE_FEMALE),
    ("vfh_22", "It allowed me to have a little bit more independence.", VOICE_MALE),
    ("vfh_23", "It helped me plan a more exciting summer.", VOICE_FEMALE),
]

# Student Voices balloon quotes
student_voices = [
    ("sv_01", "Thank you for this opportunity.", VOICE_FEMALE),
    ("sv_02", "Thank you for everything.", VOICE_MALE),
    ("sv_03", "Ms. Tatum was great and super supportive. I would love to share this great experience with other students as well.", VOICE_FEMALE),
    ("sv_04", "Do other schools in DC have this program?", VOICE_MALE),
    ("sv_05", "Thank you for teaching me how to be a sports manager and to present my business.", VOICE_FEMALE),
    ("sv_06", "Thank you for the learning I've done in this class!", VOICE_MALE),
    ("sv_07", "I would like to say thank you for giving me the opportunity.", VOICE_FEMALE),
    ("sv_08", "Thank you to the entire community. I am very grateful.", VOICE_MALE),
    ("sv_09", "Thank you very much.", VOICE_FEMALE),
    ("sv_10", "Thank you and I want to participate next year.", VOICE_MALE),
]

all_quotes = voices_from_heart + student_voices

print(f"Generating {len(all_quotes)} audio clips via ElevenLabs...")

for i, (slug, text, voice_id) in enumerate(all_quotes):
    out_path = os.path.join(output_dir, f"{slug}.mp3")
    if os.path.exists(out_path):
        print(f"  [skip] {slug} already exists")
        continue
    print(f"  [{i+1}/{len(all_quotes)}] {slug}: {text[:60]}...")
    try:
        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id="eleven_turbo_v2",
            output_format="mp3_44100_128",
        )
        with open(out_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        print(f"    -> saved {out_path}")
    except Exception as e:
        print(f"    ERROR: {e}")

print(f"\nDone! Upload the '{output_dir}/' folder contents to:")
print("  learnearndunbar/images/audio/")
print("Then tell Manus the audio files are uploaded and the balloons will be wired up.")
