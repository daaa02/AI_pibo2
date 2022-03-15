import io
import os
import requests
import json
import wave


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class TextToSpeech:

    def tts_connection(self, string, filename="tts.wav"):
        # Kakao auth-key
        REST_API_KEY = "f8f8c3f66bb3310016fdeccffba152e8"
        KAKAO_URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
        HEADERS = {
            "Content-Type": "application/xml",
            "Authorization": "KakaoAK " + REST_API_KEY  # "KakaoAK" + "공백" + Key ;;;;; 
        }
        res = requests.post(KAKAO_URL, headers=HEADERS, data=string.encode('utf-8'))

        # 음성 합성 결과를 파일로 저장
        with open(filename, "wb") as f:
            f.write(res.content)
            
            
    # tts, 효과음 등 모든 오디오를 플레이하는 함수
    def play(self, filename, out='local', volume='-2000', background=True):
        if not os.path.isfile(filename):
            raise Exception(f'"{filename}" does not exist')

        if not filename.split('.')[-1] in ['mp3', 'wav']:
            raise Exception(f'"{filename}" must be (mp3|wav)')

        if not out in ['local', 'hdmi', 'both']:
            raise Exception(f'"{out}" must be (local|hdmi|both)')

        if not isNumber(volume):
            raise Exception(f'"{volume}" is not Number')

        if type(background) != bool:
            raise Exception(f'"{background}" is not bool')

        opt = '&' if background else ''
        os.system(f'omxplayer -o {out} --vol {volume} {filename} {opt}')
