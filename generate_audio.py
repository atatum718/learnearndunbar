#!/usr/bin/env python3
"""Generate TTS audio for all balloon quotes using OpenAI TTS."""
import os
from openai import OpenAI

client = OpenAI()

output_dir = "/home/ubuntu/learnearndunbar/images/audio"
os.makedirs(output_dir, exist_ok=True)

# Voices from the Heart quotes (heart-shaped graphic)
voices_from_heart = [
    ("vfh_01", "Save my money."),
    ("vfh_02", "It allowed me to save up."),
    ("vfh_03", "It helped me get better at saving my money."),
    ("vfh_04", "It helped me provide for myself independently."),
    ("vfh_05", "I was able to pay for my end-of-year trip and school supplies."),
    ("vfh_06", "It helped me put more money toward college."),
    ("vfh_07", "I was able to pay for many senior activities on my own."),
    ("vfh_08", "I was able to get food for me and my family."),
    ("vfh_09", "I've been able to budget better."),
    ("vfh_10", "I am saving for college."),
    ("vfh_11", "Help with household bills."),
    ("vfh_12", "The extra earnings helped me pay for personal expenses and learn how to manage my finances."),
    ("vfh_13", "The money I earned helped me push my snack business and save."),
    ("vfh_14", "It allowed me to give money to my mom."),
    ("vfh_15", "It allowed me to buy the things I want and need, go out, and gain independence."),
    ("vfh_16", "Pay for my phone bill."),
    ("vfh_17", "It allowed me to provide for my family."),
    ("vfh_18", "It allowed me to treat my mom."),
    ("vfh_19", "The money allowed me to save up for important things."),
    ("vfh_20", "It allowed me to work on my money management early."),
    ("vfh_21", "The earnings allowed me to invest."),
    ("vfh_22", "It allowed me to have a little bit more independence."),
    ("vfh_23", "It helped me plan a more exciting summer."),
]

# Student Voices balloon quotes
student_voices = [
    ("sv_01", "Thank you for this opportunity."),
    ("sv_02", "Thank you for everything."),
    ("sv_03", "Ms. Tatum was great and super supportive. I would love to share this great experience with other students as well."),
    ("sv_04", "Do other schools in DC have this program?"),
    ("sv_05", "Thank you for teaching me how to be a sports manager and to present my business."),
    ("sv_06", "Thank you for the learning I've done in this class!"),
    ("sv_07", "I would like to say thank you for giving me the opportunity."),
    ("sv_08", "Thank you to the entire community. I am very grateful."),
    ("sv_09", "Thank you very much."),
    ("sv_10", "Thank you and I want to participate next year."),
]

all_quotes = voices_from_heart + student_voices

# Use alternating voices for variety — nova and shimmer sound younger/warmer
voice_cycle = ["nova", "shimmer", "nova", "shimmer", "nova", "shimmer",
               "nova", "shimmer", "nova", "shimmer", "nova", "shimmer",
               "nova", "shimmer", "nova", "shimmer", "nova", "shimmer",
               "nova", "shimmer", "nova", "shimmer", "nova", "shimmer",
               "nova", "shimmer", "nova", "shimmer", "nova", "shimmer",
               "nova", "shimmer", "nova"]

print(f"Generating {len(all_quotes)} audio clips...")

for i, (slug, text) in enumerate(all_quotes):
    out_path = os.path.join(output_dir, f"{slug}.mp3")
    if os.path.exists(out_path):
        print(f"  [skip] {slug} already exists")
        continue
    voice = voice_cycle[i % len(voice_cycle)]
    print(f"  [{i+1}/{len(all_quotes)}] {slug} ({voice}): {text[:50]}...")
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text,
        )
        response.stream_to_file(out_path)
        print(f"    -> saved {out_path}")
    except Exception as e:
        print(f"    ERROR: {e}")

print("Done!")
