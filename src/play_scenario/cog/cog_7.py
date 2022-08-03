#!/usr/bin/python3
# cognition: 인지/지각/사고

# python module
from imghdr import what
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
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break

def Play_Stick(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 크레파스와 나무 막대기 여러 개가 필요해~")
        text_to_speech("나무 젓가락을 모아서 준비해도 좋아. ")
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
        text_to_speech("이번 놀이는 막대기를 쌓아서 성을 만들거야.")
        text_to_speech("성을 만든 후에는 막대기를  하나씩 빼내 볼거야. 성이 무너지지 않게 조심해서 빼야해.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 성을 만들기 전에 막대기 끝에 날씨를 표현하는 색을 칠할거야.")
                text_to_speech("그리고 막대기를 빼낼 때마다 색을 보고 어떤 날씨인지 소개해 주면 돼.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
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
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
        break

    # 2.3 놀이 시작
    def start():
        behavior_list.do_explain_B()
        while True:
            time.sleep(1)
            text_to_speech("막대기 끝에 날씨를 표현할 수 있는 색깔을 칠해보자.")
            text_to_speech("먼저 해, 구름, 눈, 비를 표현해야해. 같은 날씨를 여러 번 반복해도 되고, 다른 날씨를 표현해도 좋아.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("좋았어! 이제 막대기를 쌓아서 성을 만들어 보자.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("멋진 성을 만들고 다 만들었으면 다 만들었다고 말해줘.")
            #행동인식 - 사진, 영상 촬영
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    time.sleep(2)
                    text_to_speech("멋진 성이 완성되었네!")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            time.sleep(1)
            text_to_speech("막대기를 하나씩 빼내 보자. 성이 무너지지 않게 조심해서 빼내는 거야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("성공하면 성공이야 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("대단한 걸? 막대기 끝에 색을 확인해봐.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("어떤 날씨를 표현하는 색이야?")
            user_said = speech_to_text()
            break

        behavior_list.do_suggestion_L()
        while True:
            #날씨인식
            text_to_speech("그렇구나!  그럼 TV에 나오는 기상캐스터 처럼 날씨를 소개해보자!")
            
            break

        behavior_list.do_praise_L()
        while True:
            text_to_speech(f"멋지다. {user_name}이가 또박또박 말하는 목소리가 전문가 같았어!")
            
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("한번 더 해보자. 성이 무너지지 않게 조심해서 빼내는 거야.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("성공하면 성공이야 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    text_to_speech("잘하는 걸? 막대기 끝에 있는 색깔을 확인해봐.")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("그리고 어떤 날씨인지 기상캐스터가 돼서 소개해 줘.")
            break

        behavior_list.do_praise_S()
        while True:
            #날씨인식
            text_to_speech("정말 기상 캐스터 같다! 할 때마다 더 잘하는 것 같아!")
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
                text_to_speech(f"열심히 따라해준 {user_name}이가 최고야~ 파이보도 똑똑해진 것 같아!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 사용한 나무 막대기를 정리하자~")
        time.sleep(5)

        text_to_speech("한 곳에 모아 두어보자.")
        text_to_speech("정리가 끝나면 다 했어 라고 말해줘.")

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
        text_to_speech("나무 막대기를 조심해서 빼내는게 어렵지 않았어?")

        user_said = speech_to_text()

        text_to_speech(f"그렇구나. {user_name}이는 어떤 날씨를 표현 하는 게 재미있었어?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech(f"그랬구나. {user_name}가 집중해서 놀이 하는 모습이 멋졌어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 나무 막대기를 들고 브이를 해봐!")
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
