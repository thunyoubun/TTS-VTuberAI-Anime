import winsound
import time
import keyboard
from utils.translate import *
from utils.tts import *
from utils.subtitle import *
from utils.sttThai import *

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

def speechToText():

    record_audio()
    text = transcribe_audio()
    translate_text(text)



if __name__ == "__main__":
    
    try:
        mode = input("[Mode] 1).Text to Speech 2).Speech to Text : ")
        if mode == "1":
            while True:
                text = input("text input : ")
                translate_text(text)
        if mode == "2":
            print("Press and Hold Left Shift to record audio")
            while True:
                if keyboard.is_pressed('LEFT_SHIFT'):
                    speechToText()
            
    except KeyboardInterrupt:
        print("Exit Program.\n")