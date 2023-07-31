import Parser as p
import pyttsx3 as say
from time import perf_counter

def speak(audio):
    engine = say.init('sapi5')
    engine.say(audio)    
    engine.runAndWait()

def main():
    fw = open("tts_old.txt", "w")
    c = 0
    while c != 10:
        start = perf_counter()
        speak("— Чем отличается еврейская мама от арабского террориста?— С террористом все-таки можно договориться…")
        fw.write(str(perf_counter()-start)+"\n")
        c+=1
if __name__ == "__main__":
    main()
    