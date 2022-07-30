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


def Play_Treasure(user_name):

    print(f"user name: {user_name} \n")
    #마법사의 보물
    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 마법 지팡이가 필요해.")
        text_to_speech("마법 지팡이가 없다면 긴 막대기를 준비해도 좋아 ~")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘.")
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
        text_to_speech(f"먼저 {user_name}이가 보물을 숨기면 친구가 보물을 찾을거야")
        text_to_speech(f"{user_name}이는 친구가 보물을 찾기 어렵게 거북이나 나무늘보처럼 느린 동물로 변하는 마법을 거는거야.")
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
                text_to_speech("동물 마법은 10초동안 유지되고, 한 번 마법을 건 동물로는 또 마법을 걸 수 없어.")
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
        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech(f"{user_name}이가 먼저 보물 쪽지를 만들어서 숨겨줘.")
            break
        def start_1():    
            behavior_list.do_waiting_A()
            while True:
                text_to_speech("다 숨기고 나면 준비 됐어 라고 말해줘~")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_suggestion_L()
                    while True:
                        time.sleep(2)
                        text_to_speech("좋아. 마법을 걸 동물카드를 파이보에게 먼저 보여주고 동물 주문을 걸어줘.")
                        text_to_speech("카드가 없으면 동물 이름을 말해도 좋아.")
                        break
                else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
                break

            behavior_list.do_waiting_A()
            while True:
                text_to_speech("동물이름을 말하고 변해라 얍! 이라고 하면 돼~ 시작!")
                break
            def start_2():    
                global i
                behavior_list.do_joy()
                while True:
                    #행동인식 - 사진, 영상 촬영
                    break

                behavior_list.do_waiting_A()
                while True:
                    #동물인식
                    #뾰로롱소리+동물소리
                    time.sleep(20)
                    break

                behavior_list.do_explain_A()
                while True:
                    text_to_speech("마법이 풀렸어~")
                    break

                behavior_list.do_waiting_B()
                while True:
                    text_to_speech("같은 방법으로 다시 마법을 걸어보자. 시작!")
                    break

                behavior_list.do_joy()
                while True:
                    #행동인식 - 사진, 영상 촬영
                    break

                behavior_list.do_waiting_A()
                while True:
                    #동물인식
                    #뾰로롱소리+동물소리
                    time.sleep(20)
                    break

                behavior_list.do_explain_A()
                while True:
                    text_to_speech("마법이 풀렸어~")
                    break

                
                if i == 1:

                    behavior_list.do_waiting_A()
                    while True:
                        text_to_speech("보물을 찾으면 찾았다고 말해줘~")

                        user_said = speech_to_text()
                        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                        if answer == 'YES':
                            behavior_list.do_praise_S()
                            while True:
                                time.sleep(2)
                                text_to_speech("정말 주문을 잘 걸었어~")
                                
                                
                                
                                break
                        else:
                            behavior_list.do_waiting_A()
                            text_to_speech("같은 방법으로 다시 마법을 걸어보자. 시작!")
                            start_2()
                            continue
                        break

                    behavior_list.do_suggestion_L()
                    while True:
                        text_to_speech(f"이번에는 역할을 바꿔보자. 친구가 보물을 숨기고 {user_name}이가 보물을 찾아줘.")
                        i=i+1
                        start_1()
                        break

                elif i == 2:
                    behavior_list.do_waiting_A()
                    while True:
                        text_to_speech("보물을 찾으면 찾았다고 말해줘~")

                        user_said = speech_to_text()
                        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                        if answer == 'YES':
                            behavior_list.do_praise_S()
                            while True:
                                time.sleep(2)
                                text_to_speech("벌써? 대단한 걸?")
                                
                                break
                        else:
                            behavior_list.do_waiting_A()
                            wait_for('YES')
                            continue
                        break
                    
            start_2()        
        start_1()
                

            

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
                    text_to_speech("보물을 열심히 지키고 찾느라 수고했어!")
                    break
            break

    start()

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 보물을 지키는게 재미있었어 아니면 찾는게 재미있었어?")
        user_said = speech_to_text()
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("정말? 왜?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그렇구나. 파이보는 {user_name}이가 다양한 동물을 알아서 정말 신났어!")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}는 어떤 동물을  제일 잘 따라하는 것 같아?")
        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("맞아. 파이보도 정말 깜짝 놀랐어!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 마법 지팡이를 들고 브이해봐!")
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
