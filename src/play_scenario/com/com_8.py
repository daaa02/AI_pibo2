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

import random

wheather=['비가 내리겠습니다.(약한 빗소리)', '해가 비치겠습니다(해소리)', '소나기가 내리겠습니다(센 빗소리)', '우박이 바닥에 쏟아져 내리겠습니다(우박소리)', '천둥 번개가 치겠습니다(천둥소리)', '눈이 내리겠습니다(캐롤소리)']


def text_to_speech(string):
    filename = "tts.wav"
    print("\n" + string + "\n")
    tts.tts_connection(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{string}<break time='500ms'/></prosody></voice>\
                </speak>", filename)
    tts.play(filename, 'local', '0', False)

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Hoop(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 바닥에 깔 매트가 필요해.매트가 없으면 이불을 준비해도 좋아 ~")
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
        text_to_speech(f"먼저 {user_name}이가 매트위에 엎드려 있으면, 친구가 {user_name}이 등에 날씨를 표현 할거야. 만약에 비가 오면 등을 톡톡 치면서 빗방울을 표현할 수 있어. 날씨는 파이보가 알려줄게.")
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
                text_to_speech("날씨는 맑은 날씨, 비, 우박, 천둥 번개, 눈 등이 있어.")
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
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech(f"바닥에 매트를 깔고 {user_name}이가 먼저 엎드려줘. ")
            break
        i=1;
        def start_1():
         global i
         behavior_list.do_waiting_B()
         while True:
            time.sleep(1)
            text_to_speech("준비가 다 됐으면 준비 됐어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
             
               behavior_list.do_explain_B()
               while True:
                 text_to_speech("좋았어.일기 예보를 들려줄게!")
                 break
            else:
                behavior_list.do_waiting_A()
                wait_for('YES')
                continue
            break

            behavior_list.do_explain_A()
         while True:
            #행동인식-사진, 영상 촬영
            text_to_speech("오늘의 일기 예보입니다. ")
            time.sleep(1)
            text_to_speech("오늘은 ", random(wheather))
            break
         behavior_list.do_explain_B()
         while True:
            #행동인식-사진, 영상 촬영
            time.sleep(10)#날씨 효과음
            text_to_speech("그리고 ", random(wheather))
            break

         behavior_list.do_explain_A()
         while True:
            #행동인식-사진, 영상 촬영
            time.sleep(10)#날씨 효과음
            text_to_speech("갑자기 ", random(wheather))
            break

         behavior_list.do_joy()
         while True:
            text_to_speech("정말 재미있다~")

            
            break
        
        if i == 1:
             behavior_list.do_suggestion_L()
             while True:
              text_to_speech(f"이번에는 역할을 바꿔보자.친구가 매트에 엎드리면 {user_name}이가 등에 날씨를 표현해줘. ")
              break
             #행동인식 - 사진, 영상 촬영
             print("*** 1회차 ***")
             i=i+1
             start_1()
             
        elif i==2:     
                 
            behavior_list.do_praise_S()
            while True:
               print("*** 2회차 ***")
               text_to_speech("우와 정말 생동감 있는 날씨 표현이야~")
            

    start()        

    

        # 2.4 놀이 완료
    behavior_list.do_question_S()
    while True:
            text_to_speech("한 번 더 해볼까? 또 하고 싶으면 또 하자라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'AGAIN':
                behavior_list.do_agree()
                text_to_speech("그래 또 하자!")
                start()
            else:
                behavior_list.do_praise_L()
                while True:
                    text_to_speech("다양한 날씨를 멋지게 표현했어. 정말 최고야~")
                    break
            break

    start()

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 어떤 날씨가 제일 재미있었어?")

        user_said = speech_to_text()
       

        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말? 왜 재미있었어?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇구나.")
        
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"파이보도 {user_name}이가 재미있어보여서 신났어!")
        
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}는 평소에 어떤 날씨를 제일 좋아해?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("맞아. 파이보도 정말 좋아해~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 햇님을 표현해봐!")
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
