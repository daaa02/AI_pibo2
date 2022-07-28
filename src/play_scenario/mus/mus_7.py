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


def Play_Awake(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 매트가 필요해.")
        time.sleep(1)
        text_to_speech("매트가 없다면 이불을 준비해도 좋아.")
        time.sleep(1)
        text_to_speech("준비되면 준비 됐어 라고 말해줘.")
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
        text_to_speech("한 명이 누워서 잠자는 드라큘라 역할을 하는거야, 그럼 다른 친구는 발 소리를 내지 않고 조용히 드라큘라에게 다가가서 만지는 거야!")
        time.sleep(1)
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
                text_to_speech("드라큘라를 깨우지 않고 만지게 되면 드라큘라는 힘이 없어지고 놀이가 끝나.")
                time.sleep(1)
                text_to_speech("그런데 가까이 오기 전에 드라큘라가 잠에서 깨서 친구를 잡으면 수 있어.")
                tiem.sleep(1)
                text_to_speech(f"{user_name}이가 먼저 드라큘라 역할을 해보자!")
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
        behavior_list.do_explain_A()
        while True:
            text_to_speech("먼저 방 가운데 매트를 깔고 드라큘라가 잘 곳을 만들어줘.")
            time.sleep(1)
            text_to_speech("그 다음은 출발 위치도 정해야 해.")
            time.sleep(1)
            text_to_speech("현관이나 화장실도 좋아.")
            time.sleep(1)
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("준비가 됐으면 준비됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_B()
                while True:
                    text_to_speech("친구는 출발 위치로 가고 파이보랑 드라큘라는 매트로 가자.")
                    time.sleep(1)
                    text_to_speech("드라큘라는 천장을 보고 누우면 돼. 파이보는 드라큘라가 잘 보이는 곳에 세워줘.")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("각자의 자리에서 준비가 됐으면 준비 됐어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_B()
                while True:
                    text_to_speech("좋았어! 내가 시작하면 드라큘라에게 다가가는 거야.")
                    time.sleep(1)
                    text_to_speech("놀이가 끝났으면 끝났어 라고 말해줘. 준비, 시작!")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break   

        behavior_list.do_waiting_A()
        while True:

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_B()
                while True:
                    text_to_speech("우와, 정말 실감났어.  이번에는 역할을 바꿔보자.")
                    time.sleep(1)
                    text_to_speech("친구가 드라큘라가 되어서 매트에 누워봐.")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break 

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("준비되면 준비 됐어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_B()
                while True:
                    text_to_speech("좋았어! 내가 시작하면 드라큘라에게 다가가는 거야.")
                    time.sleep(1)
                    text_to_speech("놀이가 끝났으면 끝났어 라고 말해줘. 준비, 시작!")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break 

        behavior_list.do_waiting_A()
        while True:
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_joy()
                while True:
                    text_to_speech("정말 흥미진진했어.")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break             

    start()

    # 2.4 놀이 완료
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("잠시 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("열심히 놀이했으니 잠시 누워서 휴식 하자! 1분 동안 휴식 시작!")
        #time.sleep(60) 
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말 편하지?")
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
            behavior_list.do_praise_L()
            while True:
                text_to_speech("정말 드라큘라 역할을 잘 했어.")
                time.sleep(1)
                text_to_speech("질서 있게 놀이하는 모습이 보기 좋았어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("오늘 놀이 어땠어? 드라큘라가 재밌었어, 깨우는 역할이 재밌었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_sad()
    while True:
        text_to_speech("파이보는 드라큘라가 깨려고 할 때 무서웠어.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 드라큘라 놀이 말고도 무서웠던 적 있어?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나. 정말 무서웠겠다.")
        time.sleep(1)
        text_to_speech(f"{user_name}이가 무서울 때 언제든 파이보를 불러.")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 무서운 드라큘라처럼 따라해봐!")        
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

Play_Awake("슬기")