# python module
import os
import sys
import time
import random

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

# my module-scenario_list
from src.play_scenario.com_1 import Play_Hoop


NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(string):
    filename = "tts.wav"
    tts.tts_connection(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{string}<break time='500ms'/></prosody></voice>\
                </speak>", filename)
    tts.play(filename, 'local', '0', False)


Scenario_List = {
    "com_1": ["사자와 쥐", "훌라후프에 동물 넣기"],
    "soc_1": ["늑대 대장의 법", "나는 왕"],
    "cog_1": ["외나무다리", "휴지길 놀이"],
    "mus_1": ["나와 우리의 차이", "풍선 축구"]
}


class Scenario_List:
    com_1 = ["사자와 쥐", "훌라후프에 동물 넣기"]
    soc_1 = ["늑대 대장의 법", "나는 왕"]
    cog_1 = ["외나무다리", "휴지길 놀이"]
    mus_1 = ["나와 우리의 차이", "풍선 축구"]


class Intro:

    def __init__(self, user_name, story_name, play_name, re_play_name):
        self.user_name = user_name
        self.story_name = story_name
        self.play_name = play_name
        self.re_play_name = re_play_name

    def Intro_Scenario(self):

        # 1.1 이야기
        behavior_list.do_suggestion()
        while True:
            text_to_speech(f"오늘은 {self.story_name} 이야기를 들려줄게")
            break

        behavior_list.do_question()
        while True:
            text_to_speech("오늘은 누구랑 놀까?" 
                           "파이보랑 둘이 놀고 싶으면 1번, 엄마나 친구랑 같이 놀고 싶으면 2번을 골라줘")

            user_said = speech_to_text()
            answer = NLP.nlp_number(user_said=user_said, dic=Dic)

            if answer == '1':
                behavior_list.do_suggestion()
                while True:
                    text_to_speech(f"좋아 파이보랑 놀자! 이번에는 {self.play_name} 놀이를 하자. 너는 어때?")
                    break
            elif answer == '2':
                behavior_list.do_suggestion()
                while True:
                    text_to_speech(f"좋아 다같이 놀자! 이번에는 {self.play_name} 놀이를 하자. 너는 어때?")
                    break
            else:
                print("*** 답변 기다리는 중 ***")
                continue
            break

        behavior_list.do_waiting()
        while True:
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_joy()
                while True:
                    text_to_speech("재미있겠다!")
                    break
                Play_Hoop(user_name)        # 나중에 방법 좀 다시 찾아봐
            else:
                behavior_list.do_question()
                while True:
                    text_to_speech(f"그럼 {self.re_play_name} 놀이를 할까?")
                    continue
            break


# 다른 놀이 제안 (임시)
recommend = [Scenario_List.com_1, Scenario_List.soc_1, Scenario_List.cog_1, Scenario_List.mus_1]
re_play_name = random.choice(recommend)  # play_name 이랑 겹칠수도 있지만 어차피 우리 거 ㄴㄴ


if __name__ == '__main__':

    user_name = input("이름 입력: ")
    run = Intro(user_name, Scenario_List.com_1[0], Scenario_List.com_1[1], re_play_name[1])
    run.Intro_Scenario()
