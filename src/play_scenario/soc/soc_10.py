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


def Play_Robot(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 준비물이 필요없어.놀이 방법을 알려줄게!")
        
        break

    

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        time.sleep(1)
        text_to_speech(f"먼저 친구가 로봇 역할을 하고, {user_name}이는 로봇을 조종하는 조종사 역할을 할거야. 로봇의 오른 손을 당기면 오른쪽으로 움직이고, 왼 손을 당기면 왼쪽으로 움직일거야.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("역할은 번갈아 가면서 하자. 로봇차례에는 로봇을 실감나게 표현해봐~")
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
        def start_1():
            global i
            behavior_list.do_question_L()
            while True:
                text_to_speech("먼저 출발지와 목적지를 정하자. 어디로 하는게 좋을까?")
                time.sleep(1)
                user_said = speech_to_text()
                break

            behavior_list.do_suggestion_L()
            while True:
                text_to_speech(f"좋아. 파이보를 목적지에 세워 주고 {user_name}이는 출발지에 파이보에게 오면 돼. 이제 로봇 조종을 시작해보자!")

                break

           
            if i == 1:
                behavior_list.do_waiting_B()
                while True:
                    text_to_speech("파이보에게 도착하면 도착했다고 말해줘.")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_praise_L()
                        while True:
                            time.sleep(2)
                            text_to_speech("조종을 정말 잘하는걸? 이번에는 역할을 바꿔보자. ")
                            print("*** 2회차 ***")
                            i=i+1
                            return start_1()
                        
                    
                    else:
                        behavior_list.do_waiting_B()
                        wait_for('DONE')
                        continue
                    

            elif i==2:

                behavior_list.do_waiting_B()
                while True:
                    text_to_speech("파이보에게 도착하면 도착했다고 말해줘.")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_praise_L()
                        while True:
                            time.sleep(2)
                            text_to_speech("로봇 흉내를 정말 잘 내는 걸? 정말 빠르게 도착했어.")
                            
                            break
                    else:
                        behavior_list.do_waiting_B()
                        wait_for('DONE')
                        continue
                    break
                
        start_1()
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
                text_to_speech(" 정말 멋진 로봇과 조종사였어. 친구와 환상의 짝꿍이야!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 로봇이랑 조종사 중에 어떤 역할이 더 재미있었어?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말? 왜 재미있었어?")
        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그렇구나. 그렇지만 {user_name}이는 두가지 역할을 모두 잘 해냈어!")

       
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 파이보가 로봇이라서 어떤 점이 좋아?")
        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그래? 정말 감동이야~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게.로봇을 표현해봐!")
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
