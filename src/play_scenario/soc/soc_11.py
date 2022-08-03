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


def Play_Body(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 전지와 크레파스가 필요해. 전지가 없다면 종이를 이어붙여 크게 만들어도 좋아 ~ ")
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
        time.sleep(1)
        text_to_speech("바닥에 전지를 붙이고 한 사람이 전지 위에 누우면, 다른 친구는 크레파스로 몸을 본떠 그림자를 그릴거야.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("그림자를 그린 후에 다시 똑같은 자세로 그림자 안에 들어가 보는거야.")
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
            global i
            i=1;
            behavior_list.do_suggestion_L()
            while True:
                text_to_speech("먼저 전지를 바닥에 붙여봐.")
                time.sleep(1)

                behavior_list.do_waiting_A()
                while True:
                    text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_suggestion_L()
                        while True:
                            time.sleep(3)
                            text_to_speech(f"좋아. {user_name}이가 먼저 전지 위에 누워보자. 친구가 누워있는 그림자를 그려줄거야. ")
                            break
                    else:
                        behavior_list.do_waiting_A()
                        wait_for('DONE')
                        continue
                    break
                break
            
            def start_1():
                global i
                behavior_list.do_waiting_B()
                while True:
                    text_to_speech("다 그리면 다 그렸다고 말해줘.")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_joy()
                        while True:
                            time.sleep(2)
                            text_to_speech("일어서서 그림자를 보자! 사람 모습 그대로 그려졌는 걸?")
                            break
                    else:
                        behavior_list.do_waiting_B()
                        wait_for('DONE')
                        continue
                    break
                        

           
                if i == 1:

                    behavior_list.do_suggestion_L()
                    while True:
                        text_to_speech("이번에는 친구가 그림자 안에 들어가봐.")
                        
                        behavior_list.do_waiting_A()
                        while True:
                            text_to_speech("딱 맞게 들어가면 파이보에게 다 됐다고 말해줘.")

                            user_said = speech_to_text()
                            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                            if answer == 'DONE':
                                behavior_list.do_praise_L()
                                while True:
                                    time.sleep(3)
                                    text_to_speech(f"정말 딱 맞게 들어갔네!이번에는 역할을 바꿔보자.{user_name}이가 친구를 그리고 다 그리면 다 그렸다고 말해줘. ")
                                    i=i+1
                                    print("****2회차****")
                                    start_1()
                                    break
                            else:
                                behavior_list.do_waiting_A()
                                wait_for('DONE')
                                continue
                            break
                        break
                elif i==2:
                    behavior_list.do_suggestion_L()
                    while True:
                        text_to_speech("이번에는 친구가 그림자 안에 들어가봐.")
                        
                        behavior_list.do_waiting_A()
                        while True:
                            text_to_speech("딱 맞게 들어가면 파이보에게 다 됐다고 말해줘.")

                            user_said = speech_to_text()
                            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                            if answer == 'DONE':
                                behavior_list.do_praise_L()
                                while True:
                                    time.sleep(3)
                                    text_to_speech("정말 똑같은 걸? 이번에도 그림자에 딱 맞게 들어갔어.")
                                    
                                    break
                            else:
                                behavior_list.do_waiting_A()
                                wait_for('DONE')
                                continue
                            break
                        break
                    
            start_1()        
    start()

               

    # 2.4 놀이 완료
    behavior_list.do_question_L()
    while True:
        text_to_speech("한번 더 해볼까? 또 하고 싶으면 또하자라고 말해줘.")

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
                text_to_speech("그림자를 멋지게 그리고 그림자 모양도 정말 잘 따라했어. ")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 친구 그림자를 그려보니까 어땠어? 어려웠어?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나. 그림자 그림은 파이보가 본 그림중에 가장 커서 멋있었어!")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("그림자를 똑같이 따라하는건 힘들지 않았어?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech("그래? 정말 열심히 따라하던걸?")
        break

   

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 그림자를 들고 브이해봐!")
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
