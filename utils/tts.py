import os
import requests
import urllib.parse
from utils.katakana import katakana_converter
from dotenv import load_dotenv

def voicevox_tts(tts):
    # You need to run VoicevoxEngine.exe first before running this script
    load_dotenv()
    # voicevox_url = 'http://localhost:50021'
    voicevox_url = os.getenv("VOICEVOX_URL") 
    # Convert the text to katakana. Example: ORANGE -> オレンジ, so the voice will sound more natural
    # katakana_text = katakana_converter(tts)
    # You can change the voice to your liking. You can find the list of voices on speaker.json
    # or check the website https://voicevox.hiroshiba.jp
    params_encoded = urllib.parse.urlencode({'text': tts, 'speaker': 24})
    request = requests.post(f'{voicevox_url}/audio_query?{params_encoded}')
    params_encoded = urllib.parse.urlencode({'speaker': 24, 'enable_interrogative_upspeak': True})
    request = requests.post(f'{voicevox_url}/synthesis?{params_encoded}', json=request.json())

    with open("test.wav", "wb") as outfile:
        outfile.write(request.content)

if __name__ == "__main__":
    voicevox_tts("みなさん、こんにちは")
