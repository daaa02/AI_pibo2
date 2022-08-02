#!/usr/bin/python3
# communication: 의사소통/언어표현

# python module
from ast import While
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

global i
i=1;
def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Clean(user_name):

    print(f"user name: {user_name} \n")
    #나의 자동차
    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 큰 박스랑, 공, 수건이 필요해. ")
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘.")
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
        text_to_speech(f"먼저 상자를 세워서 터널을 만들꺼야. {user_name}이가 자동차가 되어서 터널안에 들어가면 청소부 친구가 세차를 해줄거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                text_to_speech("세차 코스는 절약코스, 기본코스, 강력 코스가 있어. 코스에 따라서 강도가 달라질거야.")
                text_to_speech("자동차 역할은 어떤 세차 코스를 받을 지 이야기를 해줘야해~")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
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
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
        break

    # 2.3 놀이 시작
    def start():
        global i
        
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech("자동차는 터널 안으로 들어가고 청소부는 터널 옆에 앉아줘.")
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("준비가 됐으면 준비됐다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    time.sleep(2)
                    text_to_speech("세차코스는 절약코스, 기본코스, 강력코스가 있어.")
                    
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        behavior_list.do_explain_A()
        while True:
            text_to_speech("원하는 세차 코스를 이야기하고 시작!이라고 말해줘.")
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_joy()
                while True:
                    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/세차장놀이_경적소리.mp3", out='local', volume=-1000, background=False)
                    text_to_speech("좋아. 세차가 시작됐어.")
                    
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
            
            text_to_speech("먼저 공으로 자동차 마사지를 해보자.")
            #행동인식 - 사진, 영상 촬영
            time.sleep(20)
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("이번에는 왁스칠을 할거야.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("자동차를 수건으로 닦자.")
            #행동인식 - 사진, 영상 촬영
            time.sleep(20)
            break

        behavior_list.do_joy()
        while True:
            text_to_speech("세차가 완료됐어.")  
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("자동차는 터널에서 나와서 세차완료라고 말해줘.")
            #행동인식 - 사진, 영상 촬영
            break  

        if i==1:
            behavior_list.do_joy()
            while True:
                text_to_speech("정말 깨끗해 졌는걸?")
                #행동인식 - 사진, 영상 촬영
                break  
            behavior_list.do_suggestion_L()
            while True:
                text_to_speech(f"이번에는 역할을 바꿔보자. 친구가 자동차, {user_name}이가 청소부야. ")
                break  
            behavior_list.do_waiting_A()
            while True:
                text_to_speech("준비가 완료되면 준비됐어라고 말해줘.")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    i=i+1

                    start()
                    break

                    
                        
                else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
                

        elif i==2:
            behavior_list.do_praise_S()
            while True:
                text_to_speech("이번에도 정말 깨끗하게 세차가 됐는 걸?")
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
            start()
        else:
            behavior_list.do_praise_L()
            while True:
                text_to_speech("자동차가 정말 반짝반짝해진 것 같아. 수고했어!")
                break
        break



    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech("세차를 해보니까 기분이 어땠어? 상쾌해진 기분이야?")
        
        user_said = speech_to_text()
        
        text_to_speech(f"그렇구나. {user_name}이는 어떤 코스가 제일 마음에 들었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"맞아. {user_name}이가 정말 신나 보였어.")
        break

    

    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 박스 안에 들어가서 브이해봐!")
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
