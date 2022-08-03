#!/usr/bin/python3
# cognition: 인지/지각/사고

# python module
import os
from re import T
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
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break

def Play_Pocket(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 물건을 담을 주머니가 필요해.")
        time.sleep(1)
        text_to_speech("준비가 됐으면 준비 됐어 라고 말해줘~")
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
        text_to_speech("이번 놀이는 주머니에 손을 넣어 어떤 물건인지 맞추는 놀이야.")
        text_to_speech("눈으로 보지 않고 손의 감각으로 물건을 맞추는 거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("손 안에 쏙 들어가는 물건을 찾아보자.")
                text_to_speech("머리빗, 테니스공, 지우개 같은 작은 물건 5개를 찾으면 돼.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 되면 시작하자고 말해줘.")

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
        behavior_list.do_explain_A()
        while True:
            time.sleep(1)
            text_to_speech("각자 주머니에 친구가 맞출 물건을 안보이게 집어넣자.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비가 됐으면 준비됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    time.sleep(2)
                    text_to_speech(f"먼저 {user_name}이가 물건을 맞춰보자. {user_name}이가 눈을 감으면 친구가 손을 주머니 안에 넣어줘")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("준비가 되면 시작이라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    time.sleep(2)
                    text_to_speech(f"{user_name}이는 주머니 안에 있는 손을 이리저리 움직여서 어떤 물건인지 맞춰봐.")
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            #행동인식 - 사진, 영상 촬영
            text_to_speech("시간이 다 됐어!")
            text_to_speech("물건을 꺼내기 전에 먼저 이름을 말하고 꺼내서 확인해봐.")
            time.sleep(5)
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("물건을 맞췄어?")
            user_said = speech_to_text()
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("제법인걸?")
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("시간이 다 됐어!")
            text_to_speech("물건을 꺼내기 전에 먼저 이름을 말하고 꺼내서확인해봐.")
            time.sleep(5)
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("물건을 맞췄어?")
            user_said = speech_to_text()
            break

        behavior_list.do_praise_L()
        while True:
            #행동인식 - 사진, 영상 촬영
            text_to_speech("우와 재밌다. 파이보는 생각하지 못한 물건이었어. 두 사람 다 재미있는 물건을 숨겨두었네.")
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이제 한번씩 번갈아 가며 나머지 물건을 모두 맞춰보자.")
        
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 찾았으면 다 찾았어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_question_S()
                while True:
                    text_to_speech("누가 더 많이 맞췄어?")
                    user_said = speech_to_text()
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('YES')
                continue
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("그랬구나. 두 사람 모두 막상막하였어!")
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
                text_to_speech("숨기기도 맞추기도 잘 했어. 파이보도 호기심이 많아진 것 같아!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 사용한 물건들을 제자리에 가져다 놓자~")
        time.sleep(5)
        text_to_speech("정리가 끝나면 끝났어 라고 말해줘. ")
        
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"{user_name}이는 정리도 잘 하는구나!")
                time.sleep(1)
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('DONE')
            continue
        break

    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"오늘 주머니 놀이에 {user_name}이는 어떤 물건을 숨겼어?")

        user_said = speech_to_text()

        text_to_speech("정말? 제일 맞추기 어려운 물건은 어떤 거였어?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 그래도 {user_name}가 열심히 추리하는 모습은 멋졌어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 물건을 찾는 흉내를 내며 브이를 해봐!")
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
