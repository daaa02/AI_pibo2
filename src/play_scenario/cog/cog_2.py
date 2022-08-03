#!/usr/bin/python3
# communication: 의사소통/언어표현

# python module
import os
import sys
import time
import random
import string

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

def Play_Mirror(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 거울이 필요해~ 거울이 있는 곳으로 나를 옮겨줘!")
        text_to_speech("거울이 없으면 유리창 앞도 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()    # stt open
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)   # stt 결과 처리 (NLP.py 참고)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(1)
                text_to_speech("좋았어. 놀이 방법을 알려줄게!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')    # DONE 답변 들어올 때까지 stt open 반복
            continue
        break

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        text_to_speech(f"먼저 거울 앞에 서서 {user_name}의 모습을 살펴보자. 거울 앞에서 움직여봐.")
        time.sleep(3)
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("거울이 내 모습과 똑같이 움직이지?")
        text_to_speech("이번 놀이는 사람과 거울 역할을 정해서 이렇게 서로 따라하는 놀이야.")
        text_to_speech("할 수 있으면 할 수 있어 라고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("이제 친구를 바라봐. 서로 마주 보고 섰니?")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘!")

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
        behavior_list.do_suggestion_L()
        while True:
            time.sleep(1)
            text_to_speech(f"먼저 {user_name}이 사람을 해보자. 사람이 먼저 재미있는 포즈를 취해봐~")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("마음에 드는 포즈를 만들었으면 그대로 멈춰서 다 됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("그래. 이번엔 거울이 따라서 포즈를 취해봐.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 됐으면 다 됐어 라고 알려줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_agree()
                while True:
                    time.sleep(2)
                    text_to_speech("좋았어! 이번엔 멈추지 않고 음악에 맞춰 계속 포즈를 바꿔보자.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("동물이나 도형처럼 몸을 만들고 따라해 보자. 음악을 틀어줄게.")
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/거울놀이.mp3", out='local', volume=-1000, background=False)
            time.sleep(120)
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("와~ 정말 잘하는 걸? ")
        
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이번엔 거울과 사람이 역할을 바꿔보자. 사람은 포즈를 취하고 곧이어 {user_name}은 거울처럼 따라서 해봐.")
        
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 됐으면 다 됐어 라고 알려줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("역할을 바꿔도 정말 잘 하는걸?")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("음악을 틀어줄게. 노래가 끝날 때 까지 이어서 해보는 거야!")
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/거울놀이.mp3", out='local', volume=-1000, background=False)
            time.sleep(60)
            break

    start()

    # 2.4 놀이 완료

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("자, 열심히 따라했으니 이제 좀 쉬자. 천천히 바닥에 누워봐.")
        break

    behavior_list.do_waiting_C()
    while True:
        text_to_speech("다 누웠으면 다 누웠어 라고 말해줘")
        time.sleep(1)

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("이제 내가 열을 셀 게. 하나, 둘, 셋, 넷, 다섯, 여섯, 일곱, 여덟, 아홉, 열! 이제 다 셌다.")
                
                
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('YES')
            continue
        break

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
                text_to_speech("정말 훌륭한 거울이었어. 서로를 관찰하는 모습이 보기 좋았어.")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 천천히 일어나보자.")
        time.sleep(3)
        break

    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 거울이 되는 게 좋았어, 사람이 되는 게 좋았어?")

        user_said = speech_to_text()

        text_to_speech("정말? 왜?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그렇구나. 함께 놀이하는 모습이 정말 보기 좋았어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 마음에 드는 포즈를 취해봐!")
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

        if answer == 'AGAIN':       # 지금은 어떤 답변이라도 프로그램 종료됨
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
