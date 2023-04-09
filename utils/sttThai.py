import os
import wave
import keyboard
import pyaudio
import torch
from transformers import pipeline

# use speechRecognize from https://github.com/biodatlab/whisper-th-demo
def transcribe_audio():
    #Model
    MODEL_NAME = "biodatlab/whisper-th-medium-combined"
    lang = "th"

    device = 0 if torch.cuda.is_available() else "cpu"

    pipe = pipeline(
        task="automatic-speech-recognition",
        model=MODEL_NAME,
        chunk_length_s=30,
        device=device,
    )

    pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(language=lang, task="transcribe")
    text = pipe("record.wav")["text"]
    print("text from audio : ", text)
    return text

def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "record.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    print("Recording...")
    while keyboard.is_pressed('LEFT_SHIFT'):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Stopped recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("Converting...")
    # transcribe_audio()

if __name__ == "__main__":
    try:
        print("Press and Hold Left Shift to record audio")
        while True:
            if keyboard.is_pressed('LEFT_SHIFT'):
                record_audio()
                transcribe_audio()
    except KeyboardInterrupt:
        print("Stopped Program")
