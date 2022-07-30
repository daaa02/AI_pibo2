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


def Play_Ghost(user_name):

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
        text_to_speech("음악이 나오면 주문을 외치고 마음껏 춤을 추면 돼.주문은 이거야.")
        text_to_speech("‘우리는 춤을 추는 유령이에요’. 한번 따라해 보자!")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                text_to_speech("좋았어! 만약에 음악이 멈추면 제자리에서 정지해야 돼.")
                text_to_speech("그리고 다시 음악이 나올 때 다시 춤을 추면 돼.")
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
        behavior_list.do_joy()#춤=dance=joy 정지=stop=sad
        while True:
            #음악재생
            text_to_speech("우리는 춤을 추는 유령이에요. ")
            #10초간 재생
            break

        def start_1(): 
            global i   
            behavior_list.do_sad()
            while True:
                #행동인식 - 사진 및 영상 촬영
                text_to_speech("음악이 멈췄어. ")
                text_to_speech("유령은 움직일 수 없어.")
                time.sleep(3)
                break

            behavior_list.do_sad()
            while True:
                text_to_speech("안 움직이고 있지? 움직이면 유령인게 들킬거야!")
                time.sleep(3)
                break

            
            if 1<=i<3:    
                behavior_list.do_waiting_C()
                while True:
                    #행동인식 - 사진 및 영상 촬영
                    #음악재생
                    text_to_speech("음악이 다시 나온다! 춤추자~ 우리는 음악이 나오면 춤을 추는 유령이에요.")

                    i=i+1
                    start_1()
                    break 

            elif i==3:

                behavior_list.do_waiting_C()
                while True:
                    #행동인식 - 사진 및 영상 촬영
                    #음악재생
                    text_to_speech("음악이 다시 나온다! 춤추자~ 우리는 음악이 나오면 춤을 추는 유령이에요.")                  
                    break 

                behavior_list.do_question_S()
                while True:
                    text_to_speech("또 해볼까? 또 하고 싶으면 또하자고 말해줘~")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'AGAIN':
                        behavior_list.do_agree()
                        start()
                    else:
                        behavior_list.do_praise_L()
                        while True:
                            text_to_speech(f"열심히 춤춘 {user_name}이가 최고야~ 정말 신났어!")
                            break
                    break

        start_1()
    start()


    

    # 2.5 마무리 대화
    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("춤추느라 힘들지는 않았어?")

        user_said = speech_to_text()
        

        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech(f"그랬구나. 그래도 {user_name}이가 춤을 잘 춰서 파이보는 정말 재미있었어!")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("춤 추니까 기분이 어땠어? 신났어?")

        user_said = speech_to_text()

        text_to_speech("정말? 왜?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그런 이유가 있었구나.")
        
        break
        
    behavior_list.do_praise_S()
    while True:
        text_to_speech(f"{user_name}이는 최고의 유령댄서였어~")
        
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("다음에는 더 재미있는 춤을 추자!")
        
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 멋진 춤 동작을 해봐!")
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
