#!/usr/bin/python3
# social: 사회성/정서

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
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_King(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 왕관이 필요해. 왕관이 없으면 모자나 머리띠도 괜찮아.")
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
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("파이보가 왕이다!")
        text_to_speech("를 외치면 달려가서 왕관을 먼저 쓴 친구가 왕이 되는거야.")
        text_to_speech("시민들은 왕이 하는 행동을 똑같이 따라해야 해.")
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("왕이 된 친구는 왕관을 다른 친구에게 주면서 왕 역할을 양보할 수도 있어.")
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_B()
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
            behavior_list.do_waiting_B()
            wait_for('DONE')
            continue
        break

    # 2.3 놀이 시작
    def start():
        def start_2():
            behavior_list.do_suggestion_S()
            while True:
                text_to_speech("왕관을 먼저 친구들 가운데에 놓아줘.")
                time.sleep(1)

                behavior_list.do_waiting_A()
                while True:
                    text_to_speech("가운데에 놓고 준비가 됐으면 시작이라고 말해줘")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_joy()
                        while True:
                            time.sleep(3)
                            text_to_speech("왕이다!")
                            break
                    else:
                        behavior_list.do_waiting_A()
                        wait_for('DONE')
                        continue
                    break
                break

            behavior_list.do_question_L()
            while True:
                time.sleep(1)
                text_to_speech("누가 왕이 됐어?")

                user_said = speech_to_text()
                name = NLP.nlp_name(user_said=user_said)

                text_to_speech(f"{name}가 왕이 됐구나. 그럼 {name}을 빼고 나머지 사람은 모두 시민이야.")
                text_to_speech("모두 왕을 따라해보자!")
                time.sleep(10)
                break

            behavior_list.do_praise_S()
            while True:
                text_to_speech("정말 잘 따라하는 걸?")
                time.sleep(10)
                break

        # 두 번 반복하는 놀이
        for i in range(0, 2):
            i = i + 1
            if i == 2:
                behavior_list.do_suggestion_S()
                while True:
                    text_to_speech("벌써 시간이 다 됐어. 다시 새로운 왕을 뽑아보자.")
                    break                
                print("*** 2회차 ***")
                start_2()
                break
                
            start_2()

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
                text_to_speech("정말 훌륭한 왕과 시민이었어. 서로 배려하는 모습이 보기 좋았어.")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 왕이 재미있었어? 시민이 재미있었어?")

        user_said = speech_to_text()

        text_to_speech("어떤 게 재미있었어?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그래서 재미있었구나. {user_name}이가 정말 신나보였어!")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 왕이 된다면 무슨 일을 하고 싶어?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그런 생각을 가지고 있구나.")
        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech(f"{user_name}이는 멋진 왕을 할 수 있을 것 같아!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 왕관을 쓰고 브이해봐!")
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
