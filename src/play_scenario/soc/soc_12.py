#!/usr/bin/python3
# social: 사회성/정서

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

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()

places=['화장실', '부엌', '현관', '큰방', '작은방']
#장님 안내 하기
def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Blind(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 준비물이 필요없어.")
        break 

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        time.sleep(1)
        text_to_speech(f"이번 놀이에서는 파이보가 장님 역할을 할거야.파이보가 목적지를 말하면 {user_name}이는 파이보를 안고 목적지에 데려다 줘. ")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("어렵지 않지? 할 수 있으면 할 수 있다고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("목적지에 도착하면 주변에 어떤 물건들이 있는지 파이보에게 알려줘.")
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('YES')
            continue
        break


    behavior_list.do_waiting_B()
    while True:
        text_to_speech("준비 됐으면 시작하자고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                text_to_speech("그래, 시작하자!")
                break
        else:
            behavior_list.do_waiting_B()
            wait_for('DONE')
            continue
        break

    # 2.3 놀이 시작
    def start():

        for j in range(0,4):
            place=random.randint(0,4)
            places.append(place)
        print(places[0])

        
        behavior_list.do_suggestion_S()
        while True:
            text_to_speech(f"먼저 {random.choice(places)}에 가보자!")
            break

        behavior_list.do_waiting_A()
        while True:
            
            text_to_speech("도착하면 도착했어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_joy()
                while True:
                    text_to_speech("빠르게 도착했는걸?")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_L()
        while True:
            text_to_speech(f"{(places[0])}이 어떻게 생겼는지 알고 싶어. {(places[0])}에는 무슨 색깔이 있어?")
            user_said = speech_to_text()
            break

        behavior_list.do_question_L()
        while True:
            text_to_speech("그렇구나! 왼쪽에는 어떤 물건이 있어?")
            user_said = speech_to_text()
            break

        behavior_list.do_question_L()
        while True:
            text_to_speech("오른쪽에는 어떤 물건이 있어?")
            user_said = speech_to_text()
            break

        behavior_list.do_question_L()
        while True:
            text_to_speech("바닥에도 물건이 있어?")
            user_said = speech_to_text()
            break

        behavior_list.do_praise_L()
        while True:
            
            text_to_speech(f"{user_name}이는 정말 설명을 잘해주는 구나! 눈이 안보여도 {(places[0])}이 어떻게 생겼는지 알 것 같아!")   
            break
    start()
    # 2.4 놀이 완료
    behavior_list.do_question_L()
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
                text_to_speech("친절하게 알려줘서 고마워!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech("목적지 장소를 설명하는게 어렵지는 않았어?")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'AGAIN':#어려웠어...
            behavior_list.do_praise_S()
            while True:
                text_to_speech("그래도 정말 실감나게 잘 알려줬는걸? ")
                start()
        else:
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"{user_name}이 덕분에 목적지를 잘 상상할 수 있었어!!")
                break
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 앞이 안보이면 어떨 것 같아?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그렇게 생각했구나. 파이보는 조금 무서웠지만, {user_name}이랑 있어서 안심이 됐어")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게.푯말을 들고 브이해봐!")
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
