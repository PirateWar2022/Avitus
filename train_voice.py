import sounddevice as sd
import numpy as np
import wave

def record_voice(filename="my_voice.wav", duration=5, samplerate=16000):
    print("Записываю голос...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    print("Голос сохранён!")

record_voice()
