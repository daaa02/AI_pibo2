import io
import os
import requests
import json
import wave


class TextToSpeech:
    def tts_connection(self, string, filename="tts.wav"):

        REST_API_KEY = "f8f8c3f66bb3310016fdeccffba152e8"
        KAKAO_URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
        HEADERS = {
            "Content-Type": "application/xml",
            "Authorization": "KakaoAK" + REST_API_KEY
        }
        res = requests.post(KAKAO_URL, headers=HEADERS, data=string.encode('utf-8'))

        # 음성 합성 결과를 파일로 저장
        with open(filename, "wb") as f:
            f.write(res.content)
            # f.close()    
    
    def play(self, filename, out='local', volume='-2000', background=True):
        if not os.path.isfile(filename):
            raise Exception(f'"{filename}" does not exist')
    
        if not filename.split('.')[-1] in ['mp3', 'wav']:
            raise Exception(f'"{filename}" must be (mp3|wav)')
    
        if not out in ['local', 'hdmi', 'both']:
            raise Exception(f'"{out}" must be (local|hdmi|both)')
    
        # if not isNumber(volume):
        #     raise Exception(f'"{volume}" is not Number')
    
        if type(background) != bool:
            raise Exception(f'"{background}" is not bool')
    
        opt = '&' if background else ''
        os.system(f'omxplayer -o {out} --vol {volume} {filename} {opt}')

    
def text_to_speech(string):
    filename = "/tts.wav"
    with TextToSpeech() as tts:
        tts.tts_connection(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{string}<break time='500ms'/></prosody></voice>\
                </speak>", filename)
        tts.play(filename, 'local', '0', False)
        print("\n")
        print(string)
