import silero
import sounddevice as sd
import torch 
from time import sleep 

language = 'ru'
model_id = 'v3_1_ru'
'''
'v3_1_ru', 'ru_v3',
'aidar_v2', 'aidar_8khz', 'aidar_16khz',
'baya_v2', 'baya_8khz', 'baya_16khz',
'irina_v2', 'irina_8khz', 'irina_16khz', 
'kseniya_v2', 'kseniya_8khz', 'kseniya_16khz',
'natasha_v2', 'natasha_8khz', 'natasha_16khz',
'ruslan_v2', 'ruslan_8khz', 'ruslan_16khz
'''
sample_rate = 48000 #декстритизация - частота звука, по факту
speaker = 'baya' #aidar, baya, kseniya, xenia, eugene, random
device = torch.device('cpu')#
txt = "— Чем отличается еврейская мама от арабского террориста? — С террористом все-таки можно договориться…"
put_accent = True
put_yoo = True

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                    model='silero_tts',
                                    language=language,
                                    speaker=model_id
                                    )

model.to(device)

audio = model.apply_tts(text=txt,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yoo
                        )

sd.play(audio, sample_rate)
sleep(len(audio)/sample_rate)
sd.stop()

