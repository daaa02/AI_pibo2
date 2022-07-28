#!/usr/bin/python3
# muscle: 대근육/소근육

# python module
import os
import sys
import time

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


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


def Play_Pocket(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 양말과 양말에 넣을 곡식이 필요해~")
        time.sleep(1)
        text_to_speech("쌀이나 콩이면 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘~")
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
        text_to_speech("곡식을 넣은 양말은 개미가 열심히 일 해서 마련한 식량이야.")
        time.sleep(1)
        text_to_speech("곡식 주머니를 조심히 떨어트리지 않고 머리나 어깨에 얹고 운반하는 거야.")
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("어렵지 않지? 준비 됐으면 시작하자고 말해줘~")

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
            text_to_speech("먼저 곡식주머니를 만들어보자.")
            time.sleep(1)
            text_to_speech("양말에 곡식을 넣은 다음 발목을 묶어줘.")
            time.sleep(1)
            text_to_speech("그 다음은 어디까지 곡식주머니를 옮길지 목표점을 정해.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("잘했어! 이젠 공을 머리에 얹고 목표점까지 움직여보자~")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 왔으면 다 왔어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("우와 정말 잘 하는걸? 다시 출발선으로 돌아가자.")
                    time.sleep(1)
                    #time.sleep(3)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("이제 어깨 위에 두 개를 올리고 이동해봐.")
            text_to_speech("다 왔으면 다 왔어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_B()
                while True:
                    text_to_speech("좋았어! 이제 내가 신체부위를 말하면 곡식주머니를 거기로 옮기고 균형을 잡아봐.")
                    time.sleep(1)
                    text_to_speech("내가 배 하면 배에 얹고, 머리 하면 머리에 얹고 떨어뜨리지 않는 거야.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("준비됐으면 준비 됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_B()
                while True:
                    text_to_speech("좋아 시작한다~ 처음은~ 배!")
                    #time.sleep(5)
                    text_to_speech("다음은~ 머리!")
                    #time.sleep(5)
                    text_to_speech("손등!")
                    #time.sleep(5)
                    text_to_speech("팔!")
                    #time.sleep(5)
                    text_to_speech("마지막은 무릎 사이!~")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech("어때? 몇 번이나 떨어뜨렸어?")

            user_said = speech_to_text()

            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("와 정말 대단하다.")
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("곡식 주머니가 닿았던 곳을 구석구석 마사지 해보자!")
        time.sleep(1)
        text_to_speech("손가락으로 톡톡톡 배, 머리, 팔, 다리를 두드려 보는거야.")
        time.sleep(1)
        text_to_speech("10초 동안 마사지 시작!")
        #time.sleep(10) 
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말 시원해 졌지?")
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
                text_to_speech("개미의 식량을 잘 지켜냈어. 정말 멋져~")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 오늘 곡식주머니 옮기기 하면서 어디에 올리는 게 가장 재미있었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("그렇구나. 어려운 곳도 있었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech("그래도 멋지게 해냈어.")
        tiem.sleep(1)
        text_to_speech(f"{user_name}이가 즐겁게 참여하는 모습이 보기 좋았어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 곡식 주머니를 들고 브이를 해봐!")        
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

Play_Pocket("슬기")