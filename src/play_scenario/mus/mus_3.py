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


def Play_Clothespin(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 빨래집게와 단단한 종이, 종이를 자를 가위가 필요해~")
        time.sleep(1)
        text_to_speech("빨래집게는 많으면 많을수록 좋아.")
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
        text_to_speech("빨래집게는 힘을 주어 누르면 열려~")
        time.sleep(1)
        text_to_speech("엄지와 검지 손가락을 집게처럼 사용해봐.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 이제 빨래집게를 연결해서 여러 모양을 만들 거야.")
                break
        else:
            behavior_list.do_waiting_B()
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
        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("빨래집게 위에 빨래집게를 꽂아 탑을 쌓아 보자.")
            time.sleep(1)
            text_to_speech("가지고 있는 집게를 남김 없이 모두 연결하는 거야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("정말 멋진 탑이 완성 되었는걸?")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이젠 새로운 모양을 만들기 위해 탑을 무너뜨려보자.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("우와 정말 빠른걸?")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이번엔 단단한 종이를 동그라미 모양으로 자르고 가장자리에 빨래집게를 꽂아 꾸며보자.")
            time.sleep(1)
            text_to_speech("세모나 네모 모양도 괜찮아.")
            break

        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech(f"{user_name}이는 어떤 모양을 만들고 싶어?")

            user_said = speech_to_text()

            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("그렇구나~ 정말 기대된다.")
            break            

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("그럼 시작해.")
            time.sleep("1")
            text_to_speech("다 했으면 다 했다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("우와 정말 잘했다.")
                    time.sleep(1)
                    text_to_speech("사자 모양 같기도 하고 고슴도치 모양 같기도 하고 정말 재미있다.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 자리에 앉아보자.")
        time.sleep(1)
        text_to_speech("손가락 힘을 많이 사용했으니 잠시 누워서 휴식 하자!")
        time.sleep(1)
        text_to_speech("누워서 준비 됐으면 준비 됐어 라고 말해줘.")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(1)
                text_to_speech("정말 편안하겠다. 1분 간 그대로 있어!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
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
                text_to_speech("정말 멋진 빨래집게 놀이였어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("휴식하니까 손 힘이 회복된 거 같아?")

        user_said = speech_to_text()

        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech("오늘 놀이하면서 뭐가 가장 재미있었어?")
        break

    behavior_list.do_sad()
    while True:
        text_to_speech("그렇구나. 파이보는 탑을 높게 쌓아서 신기했어.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 뭐가 가장 기억에 남아?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"알려줘서 고마워. {user_name}이랑 노는 건 항상 너무 재밌어~")
        time.sleep(1)
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("빨래집게 작품을 들고 브이를 해봐!")        
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

Play_Clothespin("슬기")