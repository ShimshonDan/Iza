import vosk
import sys
import sounddevice as sd
import queue
import os
import tts_module as tts

path = os.path.abspath("voice_assistant")+"\\model"
sample_rate=16000
device = 1
q = queue.Queue()
model = vosk.Model(path)
t = tts.Tts_module()

def qcallback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
    
def listen():
        with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, device=device,
                        dtype='int16', channels=1, callback=qcallback):
            
            rec = vosk.KaldiRecognizer(model, sample_rate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    return rec.Result()
                    
t.speak("это все написал Дима")