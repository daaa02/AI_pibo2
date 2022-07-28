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


def Play_Bear(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 베개 여러개와 이불이 필요해!")
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
        text_to_speech("이번 놀이에는 곰역할과 사람역할이 있어.")
        time.sleep(1)
        text_to_speech("사람은 자고있는 곰에게 몰래 다가가서 곰을 흔들어 깨울거야.")
        time.sleep(1)
        text_to_speech("그전에 곰에게 들키지 않게 조용이 움직여야 돼.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("먼저 동굴을 만들고 그 안에 곰이 들어 갈 거야.")
                time.sleep(1)
                text_to_speech("곰은 다가오는 사람의 발자국 소리를 듣고 있다가 가까이 오면 잡는 거야.")
                break
        else:
            behavior_list.do_waiting_B()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비 됐으면 시작하자고 말해줘~")

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
        behavior_list.do_explain_A()
        while True:
            text_to_speech("먼저 방 가운데에 베개를 쌓고 이불을 덮어서 동굴을 만들어줘.")           
            time.sleep(1)
            text_to_speech("그 다음은 출발 위치도 정해야 해.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    text_to_speech("이제 역할을 나누자. 사람과 곰 역할이 있어.")
                    time.sleep(1)
                    text_to_speech(f"{user_name}이가 먼저 사람을 하자.")    # 둘, 셋 하면 너무 빠르게 느껴짐
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("곰은 동굴 속에 들어가서 잠에 들고, 사람은 파이보와 함께 출발지에 서있자.")
            time.sleep(1)
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘~")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("정말 떨린다. 겨울잠을 자는 곰을 깨우러 조심스레 다가가 보자!")
                    time.sleep(1)
                    text_to_speech("내가 시작 하면 출발 하는거야. 준비, 시~작!")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("곰이 깨어났어?")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_agree()
                while True:
                    text_to_speech("그랬구나!")
                    start()
            else:
                behavior_list.do_waiting_A()
                wait_for('YES')
                continue
            break

        behavior_list.do_explain_A()
        while True:
            text_to_speech("이번엔 사람과 곰 역할을 바꿔보자.")           
            time.sleep(1)
            text_to_speech("곰은 동굴 속에 들어가서 잠에 들고, 사람은 파이보와 함께 출발지에 서있자.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘~")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    text_to_speech("좋아. 준비, 시~작!")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("곰이 깨어났어?")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_joy()
                while True:
                    text_to_speech("정말 재미있다!")
                    start()
            else:
                behavior_list.do_waiting_A()
                wait_for('YES')
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
                text_to_speech(f"파이보는 곰에게 들킬까봐 엄청 긴장했는데, {user_name}이는 정말 씩씩하게 잘 하던걸?")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("오늘 놀이 어땠어? 곰 역할이 더 재밌었어, 사람 역할이 더 재밌었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("그렇구나. 곰을 깨우러 갈 때 안 무서웠어?")

        user_said = speech_to_text()

        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech(f"그랬구나. {user_name}이는 언제 가장 무서워?")

        user_said = speech_to_text()

        break

    behavior_list.do_sad()
    while True:
        text_to_speech("정말 무서웠겠다! 다음에는 오늘처럼 용기를 내보자!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 곰 처럼 포즈를 취해봐!")        
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

Play_Bear("슬기")