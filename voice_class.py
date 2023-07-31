import tts_module as tts #text-to-speech
import stt_module as stt #speech-to-text
#import parser_1 
from random import randint

class Voice_assistant():
    __name = []
    __settings=[]
    
    def __init__(self) -> None:
        #parsing = parser_1.Parser()
        #self.__dictJoks = parsing.getJoke()
        self.__module_tts = tts.Tts_module()
        self.__module_stt = stt.Stt_module()
        
    def say(self) -> None:
        txt = self.__module_stt.listen()
        self.__module_tts.speak(txt)
    
    def say_jokes(self):
        pass
        #index = randint(0, len(self.__dictJoks)-1)
        #self.__module_tts.speak(self.__dictJoks[index])