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
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Wool(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 털실이랑 짧은 막대기가 필요해~")
        text_to_speech("나무젓가락이나 연필을 준비하면 좋아.")
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
    behavior_list.do_explain_A()
    while True:
        text_to_speech("이번 놀이는 털실을 빨리 감아보는 놀이야. 먼저 막대기에 털실을 감을 거야.")
        text_to_speech("털실을 다 감으면 털실을 풀었다가 다시 감아볼 거야.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                time.sleep(2)
                text_to_speech(f"{user_name}이가 털실을 감는 동안 파이보가 시간을 재서 얼마나 걸렸는지 알려줄게. ")
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
                time.sleep(1)
                text_to_speech("그래 시작하자!")
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
            text_to_speech("막대기에 털실을 감아보자!")
            
            break


        behavior_list.do_waiting_A()
        while True:
            
            text_to_speech("준비~ 시작!")
            start=time.time()
            text_to_speech("털실을 다 감으면 파이보에게 다 했어 라고 말해줘~")
            #행동인식 - 사진, 영상 촬영
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    time.sleep(1)
                    text_to_speech(f"{time.time() - start: .3f}초가 걸렸어! 정말 열심히 감았는 걸?")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L
        while True:
            text_to_speech("이번에는 털실을 풀면서 뒤로 걸어가보자. 장애물에 부딪치거나 넘어지지 않게 조심해야 해.")
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("털실을 다 풀면 다 풀었어 라고 말해줘~")
            #행동인식 - 사진, 영상 촬영
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_praise_L()
                while True:
                    time.sleep(1)
                    text_to_speech(f"{user_name}이는 뒤로 걷기도 잘하는 구나!좋아. 다시 털실을 감아보자.")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('YES')
                continue
            break 

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("시작하자고 말하면 파이보가 그때부터 시간을 재도록 할게.")
            
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(1)
                    text_to_speech("시작!")
                    start=time.time()
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break 

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("털실을 다 감으면 파이보에게 다했어 라고 말해줘~")
            
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    time.sleep(1)
                    text_to_speech(f"{time.time() - start: .3f}초가 걸렸어! 정말 빠른 속도야. 대단해~")
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
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
                text_to_speech("정말 열심히 털실 감기를 했어! 처음보다 훨씬 잘하는 걸?")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("털실을 풀면서 뒤로 걸으니까 어땠어? 어렵진 않았어?")
        user_said == speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)
        #어려웠어가 없음 일단은 DONE으로 넣겠음
        if answer == 'DONE':
            behavior_list.do_agree()
            while True:
                text_to_speech(f"그랬구나. 원래 뒤로 걷는건 쉽지 않아. 하지만 오늘 {user_name}이는 조심조심 잘 걷던걸?")
                
        else:
            behavior_list.do_praise_L()
            while True:
                text_to_speech(f"그랬구나. {user_name}이는 새로운 것도 금방 습득하는 것 같아!")
                break
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech("어떻게 하면 털실을 더 빨리 감을 수 있을까?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그럴 수 있겠구나. 파이보는 빨리 움직일 수 있는 {user_name}이가 너무 부러워~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 털실을 들고 브이해봐!")
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
