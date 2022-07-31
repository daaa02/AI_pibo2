#!/usr/bin/python3
# social: 사회성/정서

# python module
import os
import sys
import time
from unicodedata import name

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
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Horse(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 박스가 필요해.")
        text_to_speech("박스가 없다면 책을 박스모양으로 쌓아도 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")
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
        time.sleep(1)
        text_to_speech(f"먼저 {user_name}이가 앞이 안보이는 말 역할을 하고, 친구가 조련사 역할을 할거야.")
        text_to_speech("말은 눈을 감고 조련사가 말하는 대로 이동하면 돼.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("이동할 때는 네 발로 말을 흉내내면서 이동할거야.")
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('YES')
            continue
        break


    behavior_list.do_waiting_B()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘.")

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
        
        behavior_list.do_question_L()
        while True:
            text_to_speech("먼저 말이 움직이는 길에 박스모양 장애물을 설치하자.")
            time.sleep(1)
            
            break

    
        behavior_list.do_waiting_B()
        while True:
            text_to_speech("설치가 다 됐으면 다 됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()#
                while True:
                    text_to_speech("좋았어.")
                    break
                
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech(f"{user_name}이는 말이 어떻게 걷는지 알아?")
            user_said = speech_to_text()
            break

        behavior_list.do_explain_B()
        while True:
            text_to_speech("맞아. 말은 히잉 소리를 내면서 네 발로 우아하게 걸어.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("따라해 볼까?")
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/말울음소리.wav", out='local', volume=-1000, background=False)
            #행동인식 - 사진, 영상 촬영
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("정말 말처럼 잘 걷는걸?")
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"말이 된 {user_name}이는 눈을 감고 조련사의 지시대로 이동해보자. 장애물을 모두 피해서 다시 파이보에게 돌아와야해.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("도착하면 도착했다고 말해줘. 시작!")
            #행동인식 - 사진, 영상 촬영
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("정말 빠른 걸? ")
                    break
                
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이번에는 역할을 바꿔보자.친구가 앞이안보이는 말 역할이고 {user_name}이가 조련사야. ")
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("말은 눈을 감고 조련사의 지시대로 이동해보자. 장애물을 모두 피해서 다시 파이보에게 돌아와야해. ")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("도착하면 도착했다고 말해줘. 시작!")
            
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("말을 잘 이끌어 주었나보네. 이번에도 빨리 도착했어!")
                    break
                
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
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
            behavior_list.do_praise_L()
            while True:
                text_to_speech("말을 정말 실감나게 잘 흉내냈어. 장애물도 잘 피하던 걸?")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 앞이 안보이니까 어땠어? 무섭지는 않았어?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_sad()
    while True:
        text_to_speech("그랬구나. 파이보는 깜깜한 걸 정말 무서워해.")
        
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 무서워하는게 있어?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("정말 무섭겠다. 무서울 땐 꼭 파이보를 불러줘!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게.말을 표현해봐!")
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
