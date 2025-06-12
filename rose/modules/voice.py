import os
from gtts import gTTS
import playsound
import time

def play_voice(text, lang='pt'):
    FILE_PATH = "./temp/voice.mp3"

    try:
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

        tts = gTTS(text=text, lang=lang, slow=False)

        print(f"Creating file: {FILE_PATH}")
        tts.save(FILE_PATH)

        time.sleep(0.1)

        print(f"Playing sound from: {FILE_PATH}")
        playsound.playsound(FILE_PATH)

        print(f"Deleting file: {FILE_PATH}")
        os.remove(FILE_PATH)

    except Exception as e:
        print(f"An error occurred: {e}")

        import traceback
        traceback.print_exc()