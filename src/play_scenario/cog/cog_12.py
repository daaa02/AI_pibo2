#!/usr/bin/python3
# cognition: 인지/지각/사고

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
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break

def Play_Ruler(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 줄자와 테이프, 지우개가 필요해~")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")
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
        text_to_speech("이번 놀이는 줄자를 가지고 길이를 재 보는 놀이야.")
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
                text_to_speech("좋았어! 집안의 여러 물건의 길이를 재 보고, 길이를 비교해 볼 거야.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘~")

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
        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech("먼저 줄자는 어떨 때 사용하는 물건인지 이야기 해볼래?")
            user_said = speech_to_text()
            break

        behavior_list.do_suggestion_L()
        while True:
            
            text_to_speech("좋은 답변이야. 맞아, 줄자는 길이나 거리를 잴 때 사용해.")
            text_to_speech("줄자를 끝까지 펴면 길이가 얼만큼인지 알 수 있어.")
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("끝까지 펴보고 적혀있는 숫자를 알려줄래?")

            user_said = speech_to_text()
            number = NLP.nlp_number(user_said=user_said, dic=Dic)

            if number != 0 :
                behavior_list.do_praise_L()
                while True:
                    time.sleep(2)
                    text_to_speech(f"우와. {user_name}이는 큰 숫자도 잘 읽는구나!")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for(number != 0)
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이번엔 집안의 여러 물건의 길이를 재보자. TV, 식탁, 서랍장 처럼 {user_name}이가 재보고 싶은 물건을 찾아봐.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("찾았으면 찾았어 라고 말하고 그 앞으로 파이보를 옮겨줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("우와, 정말 잘 찾았네!")
                    
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('YES')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("이제 길이를 재 보자. 한 번 재어보고 알려줄래?")
            time.sleep(1)

            user_said = speech_to_text()
            number = NLP.nlp_number(user_said=user_said, dic=Dic)

            if number != 0 :
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("좋았어. 처음 해 보는데 정말 잘 하네!")
                    
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for(number != 0)
                continue
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("한번 더 해보자.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech(f"{user_name}이가 재보고 싶은 물건을 찾았으면 찾았어 라고 말하고 그 앞으로 파이보를 옮겨줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("이번에도 잘 찾았네!")
                    
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('YES')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("이제 길이를 재어보고 알려줘.")
            time.sleep(1)

            user_said = speech_to_text()
            number = NLP.nlp_number(user_said=user_said, dic=Dic)

            if number != 0 :
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("역시 길이를 정말 잘 재는구나!")
                    
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for(number != 0)
                continue
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech(f"이번엔 {user_name}랑 50cm 떨어진 위치랑 80cm 떨어진 위치에 테이프를 붙여보자")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("이제 지우개를 던져보자.")
                    text_to_speech("지우개를 던져서 50cm와 80cm 사이에 떨어뜨리면 돼.")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("준비가 됐으면 준비 됐어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    text_to_speech("이제 지우개를 던지자!")
                    text_to_speech("한번에 못 넣어도 괜찮아.")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break        

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("성공했으면 성공했어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech(f"굉장해.어려웠을 텐데 {user_name}이는 힘을 잘 조절하는 구나?")
                    
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
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
                text_to_speech(f"열심히 놀이해 준 {user_name}이가 최고야~ 길이를 재 보는 경험이 정말 특별한 것 같아!")
                break
        break

    # 2.5 마무리 대화

    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("오늘 줄자 놀이는 재미있었어?")

        user_said = speech_to_text()

        text_to_speech("정말? 큰 물건을 재는 게 어렵진 않았어?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 파이보는 {user_name}가 줄자를 다루는 모습이 멋졌어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 줄자를 들고 브이를 해봐!")
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
