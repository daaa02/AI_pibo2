#!/usr/bin/python3
# social: 사회성/정서

# python module
import os
from re import I
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

body=['발바닥', '배', '팔', '다리', '팔꿈치', '무릎', '허벅지']


def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Body(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 준비물이 필요없어.놀이 방법을 알려줄게!")
        break 

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        time.sleep(1)
        text_to_speech("파이보가 신체 부위 한 곳을 말할거야. 그러면 그 신체 부위를 악기처럼 두드리면서 소리를 내면 돼.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("파이보가 음악을 틀어줄게. 음악 속도에 맞춰서 신체를 두드려보자.")
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
        global i
        i=1;
        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("첫번째 악기는 손바닥이야. 손바닥을 마주쳐 짝짝 소리를 내보자!")
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("음악을 틀어줄게.")
            #행동인식 - 사진, 영상 촬영
            break
        choicelist=random.choice(body)
        def start_1():
            global i
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/신체악기.mp3", out='local', volume=-1000, background=False)
            if 1<=i<4:
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech(f"{random.choice(body)}로 소리를 내보자!")
                    i=i+1
                    
                    #행동인식 - 사진, 영상 촬영
                    return start_1()
                
            elif i==4:
                behavior_list.do_joy()
                while True:
                    
                    text_to_speech("정말 재미있는 소리다!")   
                    break
        
        start_1()
        

        

        behavior_list.do_waiting_C()
        while True:
            text_to_speech(f"마지막으로{random.choice(body)}로 소리를 내보자!") 
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/신체악기.mp3", out='local', volume=-1000, background=False)
            #행동인식 - 사진, 영상 촬영
            break

        behavior_list.do_praise_S()
        while True:
            
            text_to_speech("우리 몸에서 나는 소리가 정말 악기 소리같아!")   
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
                text_to_speech("정말 신나는 신체 악기 연주였어!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 어떤 신체 부위 소리가 제일 재미있었어?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말? 어떤 소리가 났어?")
        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그런 소리가 났구나. 정말 신기하다~")

       
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("소리가 잘 안나는 신체부위도 있었어?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그랬구나. {user_name}이가 조금 더 자라면 더 큰 소리를 낼 수 있을거야!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게.신나게 박수를 쳐봐!")
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
