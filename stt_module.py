import vosk
import sys
import sounddevice as sd
import queue
import os

class Stt_module:
    def __init__(self) -> None:
        self.__path = os.path.abspath("voice_assistant")+"\\model"
        self.__sample_rate=16000
        self.__device = 1
        self.__q = queue.Queue()
        self.__model = vosk.Model(self.__path)
            
    def __callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.__q.put(bytes(indata))

    def listen(self):
        with sd.RawInputStream(samplerate=self.__sample_rate, blocksize=8000, device=self.__device,
                            dtype='int16', channels=1, callback=self.__callback):
            
            rec = vosk.KaldiRecognizer(self.__model, self.__sample_rate)
            data = self.__q.get()
            if rec.AcceptWaveform(data):
                return rec.Result()
            