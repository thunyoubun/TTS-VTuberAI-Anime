import winsound
import time
import keyboard
from utils.translate import *
from utils.tts import *
from utils.subtitle import *

def translate_text(text):
    global is_Speaking

    # tts will be the string to be converted to audio
    detect = detect_google(text)
    tts = translate_google(text, f"{detect}", "JA")
    # tts = translate_deeplx(text, f"{detect}", "JA")
    # tts_en = translate_google(text, f"{detect}", "EN")
    try:
        # print("ID Answer: " + subtitle)
        print(f"{detect} input : " + text)
        print("JP Answer: " + tts)
        # print("EN Answer: " + tts_en)
    except:
        print("Error translating text")
        return

    # Choose between the available TTS engines
    # Japanese TTS
    voicevox_tts(tts)

    # Generate Subtitle
    generate_subtitle(text)

    time.sleep(1)

    # is_Speaking is used to prevent the assistant speaking more than one audio at a time
    is_Speaking = True
    winsound.PlaySound("test.wav", winsound.SND_FILENAME)
    is_Speaking = False

    # Clear the text files after the assistant has finished speaking
    time.sleep(1)
    with open ("output.txt", "w") as f:
        f.truncate(0)
    with open ("chat.txt", "w") as f:
        f.truncate(0)

if __name__ == "__main__":
    
    try:
        while True:
            text = input("text input : ")
            translate_text(text)
    except KeyboardInterrupt:
        print("Exit Program.\n")