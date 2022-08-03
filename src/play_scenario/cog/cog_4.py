#!/usr/bin/python3
# communication: 의사소통/언어표현

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
    
def Play_Tissue(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("놀이를 위해 휴지가 필요해~ 두루마리 휴지를 준비해줘.")
        text_to_speech("많으면 많을 수록 좋아. ")
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
        text_to_speech("이번 놀이는 휴지로 길을 만들고 바깥쪽은 바다라고 생각 하는 거야.")
        text_to_speech("바다에 빠지지 않고 길을 잘 건너가야 해.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 중간에 해적이 나와서 가는 길을 방해 할 거야.해적 역할은 한 번 씩 양보하면서 해보자.")
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
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech("휴지로 길을 만들어보자~")
            break

        behavior_list.do_explain_B()
        while True:
            time.sleep(1)
            text_to_speech("길 끝에는 섬이 있어야 해. 섬은 하나, 길은 여러 개 만들 수 있어.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 만들었으면 다 만들었어 라고 말해줘!")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech(f"{user_name}이가 먼저 길을 건너가 보자.")
                    text_to_speech("친구는 해적이 되어줘. 해적은 공이나 인형을 던져 방해할 거야.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("모두 제자리에 준비가 됐으면 준비 됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("내가 시작을 외치면 건너 가는거야.")
                    
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            
            text_to_speech("섬에 도착하면 도착했어 라고 말해줘. 간다. 시~작!")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    #행동인식 - 사진, 영상 촬영
                    time.sleep(2)
                    text_to_speech("정말 용감했어!")
                    
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이번엔 휴지를 더 사용해서 새로운 길을 연결해봐. 더 재밌을 거야.")
            
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("길을 다 고쳤으면 다 고쳤어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_explain_A()
                while True:
                    text_to_speech(f"이번엔 {user_name}이가 해적이 되고 친구는 섬까지 건너가 보자.")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('YES')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("모두 제자리에 준비해. 준비가 되면 준비 됐어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_waiting_B()
                while True:
                    text_to_speech("이제 간다. 시~작! ~")
                    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/휴지로바다.wav", out='local', volume=-1000, background=False)
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_sad()
        while True:
            #행동인식 - 사진, 영상 촬영
            text_to_speech("바다에 빠지진 않았어? 파이보는 두 번이나 빠져서 조마조마 했어. OO이는 달리기도 정말 잘한다.")
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
                text_to_speech(f"열심히 놀이해 준 {user_name}이가 최고야~ 정말 신났어!")
                break
        break

    # 2.5 마무리 대화

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 길을 건너는게 재밌었어? 방해하는게 재밌었어?")
        user_said = speech_to_text()

        text_to_speech("그래? 왜?")
        user_said = speech_to_text()

        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 적이 있는 바다에 간다면 어떤 무기를 가져가고 싶어?")
        user_said = speech_to_text()

        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇게 생각했구나. 정말 좋을 것 같아.")
        break

    


    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 해적처럼 포즈를 취해봐!")
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
