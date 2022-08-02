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


def Play_Smile(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 종이와 그림도구, 테이프가 필요해~")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘")
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
        text_to_speech("화장실, 부엌, 현관에 새로운 이름을 만들어보자. 만약에 화장실 이름을 박수치는 거리로 만들면, 화장실 앞에 도착할 때 박수를 쳐야해.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                text_to_speech("거리 이름은 수영하는 거리도 될 수 있고, 등산하는 거리, 피아노 치는 거리 거리처럼 다양하게 지을 수 있어.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 되면 시작하자고 말해줘")

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
        i=1;
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech("장소 마다 이름을 정해보자~")
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("먼저 화장실은 무슨 거리라고 할까?")

            user_said = speech_to_text()
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("좋아 그럼 부엌은 뭐라고 할까?")

            user_said = speech_to_text()
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("멋진데? 그럼 현관은 뭐라고 할까?")

            user_said = speech_to_text()
            break

        behavior_list.do_agree()
        while True:
            text_to_speech("그래 좋아")
        
            break

        behavior_list.do_explain_A()
        while True:
         time.sleep(1)
         text_to_speech("이제 종이랑 그림도구로 장소마다 표지판을 만들자.")
         time.sleep(1)
         text_to_speech("거리 이름을 그림으로 표현하거나 글씨로 써서 표지판을 완성해줘~")
         break


        behavior_list.do_waiting_C()
        while True:
            text_to_speech("세 개 모두 완성 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    time.sleep(2)
                    text_to_speech("멋진 표지판이 완성되었네. 이제 거리에 표지판을 붙이자~")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("다 붙이면 다 붙였어 라고 말해줘.")            
            

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_question_S()
                while True:
                    text_to_speech("좋았어. 먼저 어떤 거리로 가볼까?")
                    user_said = speech_to_text()
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('YES')
                continue
            break

        def start_1():
            global i
            behavior_list.do_agree()
            while True:
                text_to_speech("그래! 파이보를 데려가 줄래?")

                break

            behavior_list.do_waiting_B()
            while True:
                text_to_speech("도착하면 도착했어 라고 말해줘~")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_suggestion_S()
                    while True:
                        text_to_speech("이제 거리 이름처럼 흉내 내 보자!")
                        time.sleep(10)
            
                        break
                else:
                    behavior_list.do_waiting_B()
                    wait_for('DONE')
                    continue
                break

                
            behavior_list.do_praise_S()
            while True:
                text_to_speech("정말 열심히 잘 표현하는 걸?")   
                time.sleep(1)
                break

            
            if i == 1:    

                behavior_list.do_question_S()
                while True:
                    text_to_speech("또 어떤 거리를 가볼까?") 
                    user_said = speech_to_text()  
                    print("*** 2회차 ***")
                    i=i+1
                    start_1()
                    break

            elif i==2:
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
                            text_to_speech("거리 이름에 따라 정말 열심히 표현했어~우리만의 멋진 동네를 만든 것 같아!")
                            break
                    break

                
        start_1()

    start()
            

    

        # 2.4 놀이 완료

    

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech("이제 잠시 자리에 앉아 쉬어보자.")
        time.sleep(3)
        text_to_speech("놀이가 어렵지는 않았어? ")

        user_said = speech_to_text()
        

        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나. 처음해보는 건 원래 쉽지 않아.")
        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech(f"하지만 {user_name} 이의 열심히 하는 모습은 정말 멋졌어!")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("어떤 거리가 제일 즐거웠어?")

        user_said = speech_to_text()

        text_to_speech("정말? 왜 즐거웠어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f" {user_name}이는 열심히 하는 모습이 정말 멋졌어. 파이보는 {user_name}이랑 갔던 거리가 다 재미있었어~")

        break

    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 거리를 걷는 자세를 취해봐!")
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

    