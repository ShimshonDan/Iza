import silero
import sounddevice as sd
import torch 
from time import sleep

class Tts_module:
    __language = "ru"
    __model_id = "v3_1_ru"
    __sample_rate = 48000 #декстритизация - частота звука, по факту
    __speaker = "baya" #aidar, baya, kseniya, xenia, eugene, random
    __device = torch.device("cpu")
    __put_accent = True
    __put_yoo = True
    
    __additional_setting_model_id = """ 
                    v3_1_ru, ru_v3,
                    aidar_v2, aidar_8khz, aidar_16khz,
                    baya_v2, baya_8khz, baya_16khz,
                    irina_v2, irina_8khz, irina_16khz, 
                    kseniya_v2, kseniya_8khz, kseniya_16khz,
                    natasha_v2, natasha_8khz, natasha_16khz,
                    ruslan_v2, ruslan_8khz, ruslan_16khz
                """
                
    def __init__(self) -> None:
        self.__model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                    model='silero_tts',
                                    language=self.__language,
                                    speaker=self.__model_id
                                    )

        self.__model.to(self.__device)
        
    def speak(self, txt):
        audio = self.__model.apply_tts(text=txt,
                        speaker=self.__speaker,
                        sample_rate=self.__sample_rate,
                        put_accent=self.__put_accent,
                        put_yo=self.__put_yoo
                        )

        sd.play(audio, self.__sample_rate)
        sleep(len(audio)/self.__sample_rate)
        sd.stop()
        