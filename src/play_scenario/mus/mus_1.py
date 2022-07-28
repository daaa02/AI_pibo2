#!/usr/bin/python3
# muscle: 대근육/소근육

# python module
import os
import sys
import time

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Balloon(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 풍선이 필요해~")
        time.sleep(1)
        text_to_speech("풍선은 두 개 정도 필요해.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(1)
                text_to_speech("좋았어. 놀이 방법을 알려줄게!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
        break

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        text_to_speech("풍선은 바람을 넣으면 재밌는 소리를 내고 높이 날아가기도 해")
        time.sleep(1)
        text_to_speech("풍선 꼭지를 묶으면 공처럼 놀 수도 있어.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech(f"좋아. {user_name}이가 좋아하는 색깔의 풍선을 골라봐.")
                break
        else:
            behavior_list.do_waiting_B()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("고르고 준비가 됐으면 시작하자고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                text_to_speech("그래, 시작하자!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
        break

    # 2.3 놀이 시작
    def start():
        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("자, 이제 풍선을 불어봐~")
            time.sleep(5)
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("풍선을 묶지 말고 멀리 날려보자~")
            time.sleep(3)
            text_to_speech("이제 풍선을 쫓아가서 잡아 오자.")
            break

        behavior_list.do_joy()
        while True:
            text_to_speech("정말 재밌어 보여!")
            time.sleep(1)
            break

        behavior_list.do_explain_B()
        while True:
            text_to_speech("이번에는 풍선을 불어서 꼭지를 묶어봐~")
            time.sleep(5)
            break

        behavior_list.do_explain_A()
        while True:
            text_to_speech("풍선으로 공을 만들어 축구 선수들처럼 멋지게 차보자~")           
            time.sleep(1)
            text_to_speech("발이나 무릎으로 풍선을 차 올리는 거야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("자, 그럼 시~작! 내가 열을 셀 동안 해봐. ")
                    time.sleep(1)
                    text_to_speech("하나, 두울, 세엣, 네엣, 다섯, 여섯, 일곱, 여덟, 아홉, 열!")    # 둘, 셋 하면 너무 빠르게 느껴짐
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_joy()
        while True:
            text_to_speech("정말 재미있어 보여!")
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이번엔 머리로 헤딩슛을 해보자~")
            text_to_speech("제자리에서 뛰면서 머리로 풍선을 치는 거야.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘~")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("자, 그럼 시~작! 내가 열을 셀 동안 해봐. ")
                    time.sleep(1)
                    text_to_speech("하나, 두울, 세엣, 네엣, 다섯, 여섯, 일곱, 여덟, 아홉, 열!")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("정말 축구 선수 같은 걸? 멋지다!")
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_question_S()
    while True:
        text_to_speech("한 번 더 해볼까? 또 하고 싶으면 또 하자라고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'AGAIN':
            behavior_list.do_agree()
            while True:
                text_to_speech("그래 또 하자!")
                start()
        else:
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"열심히 놀이한 {user_name}이가 최고야~ 정말 신났어!")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("풍선으로 하는 축구 놀이 재미있었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech("그랬구나. 열심히 하는 모습이 보기 좋았어!")
        break

    behavior_list.do_sad()
    while True:
        text_to_speech("파이보는 오늘 달리느라 힘들었어.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 놀이하면서 어려운 거 있었어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그랬구나. 이야기 들려줘서 고마워.")
        time.sleep(1)
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 축구 선수처럼 포즈를 취해봐!")        
        break

    behavior_list.do_photo()
    time.sleep(5)
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3", out='local', volume=-1000, background=False)

    # 2.7 다음 놀이 제안
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("또 다른 놀이 할까? 파이보랑 또 놀고 싶으면 놀고 싶다고 말해줘!")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'AGAIN':
            behavior_list.do_joy()
            while True:
                text_to_speech("그래 좋아!")
                time.sleep(1)
                break
        else:
            behavior_list.do_agree()
            while True:
                time.sleep(1)
                text_to_speech("다음에 또 놀자!")
                break
        break
