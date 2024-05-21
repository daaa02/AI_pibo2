import io
import os
import requests
import json
import wave
import urllib.request


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class TextToSpeech:

    def tts_connection(self, text, filename):
        # CLOVA auth-key
        client_id = "9rx70l2455"
        client_secret = "zC7febcAzgI4oTQ25DODSqDKerk0lUwhwIAbVvsA"
        encText = urllib.parse.quote(text)
        data = "speaker=nhajun&volume=0&speed=1&pitch=0&format=wav&text=" + encText
        url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
        request.add_header("X-NCP-APIGW-API-KEY",client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            with open(filename, 'wb') as f:
                f.write(response_body)
        else:
            print("Error Code:" + rescode)            
            

    # tts, 효과음 등 모든 오디오를 플레이하는 함수
    def play(self, filename, out='local', volume='-1000', background=True):
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
