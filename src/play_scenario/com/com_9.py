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


def Play_Pizza(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 바닥에 깔 매트가 필요해. 매트가 없다면 이불을 준비해도 좋아 ~ ")
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
        text_to_speech(f"먼저 {user_name}이가 매트위에 엎드려 있으면, 친구가 {user_name}이 등에 피자 만들기를 표현해줄거야. 레시피는 파이보가 알려줄게.")
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
                text_to_speech("피자 도우를 반죽하는 단계에서는 친구 등을 살살 주무르면서 반죽을 표현할 수 있어.")
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
                text_to_speech("그래 시작하자!")
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
            time.sleep(1)
            text_to_speech(f"바닥에 매트를 깔고 {user_name}이가 먼저 엎드려줘.  친구는 {user_name}이 옆에 앉아서 등에 손을 올리면 돼. ")
            break
        
        def start_1():
            global i   
            behavior_list.do_waiting_B()
            while True:
                text_to_speech("준비가 다 됐으면 준비 됐어 라고 말해줘~")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_joy()
                    while True:
                        time.sleep(2)
                        text_to_speech(" 좋아.  시작한다!")
                        break
                else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
                break

            behavior_list.do_explain_A()
            while True:
                #행동인식-사진, 영상 촬영
                text_to_speech("피자 레시피를 알려줄게.")
                time.sleep(1)
                text_to_speech("먼저 피자 도우를 만들어 주세요.")
                break

            behavior_list.do_explain_A()
            while True:
                #행동인식-사진, 영상 촬영
                time.sleep(10)#요리 효과음
                text_to_speech("토마토 소스를 발라주세요.")
                
                break

            behavior_list.do_explain_A()
            while True:
                #행동인식-사진, 영상 촬영
                time.sleep(10)#요리 효과음
                text_to_speech("원하는 토핑을 말하고 토핑을 올려 주세요.")
                
                break

            behavior_list.do_explain_A()
            while True:
                #행동인식-사진, 영상 촬영
                time.sleep(10)#요리 효과음
                text_to_speech("치즈를 뿌려주세요.")
                
                break

            behavior_list.do_explain_A()
            while True:
                #행동인식-사진, 영상 촬영
                time.sleep(10)#요리 효과음
                text_to_speech("피자를 오븐에 데워주세요.")
                
                break

            
            if i == 1:

                behavior_list.do_joy()
                while True:
                    #행동인식-사진, 영상 촬영
                    time.sleep(10)#요리 효과음
                    text_to_speech("맛있는 피자가 완성됐어~ ")
                    
                    break

                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech(f"이번에는 역할을 바꿔보자.친구가 매트에 엎드리면 {user_name}이가 피자를 만들어줘. ")
                    print("*** 2회차 ***")
                    i=i+1
                    start_1()
                    break
                
                    
                    
                
        
            elif i==2:
                behavior_list.do_joy()
                while True:
                    time.sleep(10)#요리 효과음
                    
                    text_to_speech("맛있는 피자 완성! 진짜 피자 냄새가 나는 것만 같아!")
                    break
        start_1()    

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
                    text_to_speech("피자 만들기를 멋지게 표현했어. 최고의 요리사였어~")
                    break
            break

         


    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 피자에 어떤 토핑이 제일 좋아?")

        user_said = speech_to_text()
        

        break

    behavior_list.do_joy()
    while True:
        text_to_speech("정말? 파이보도 좋아해! ")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 제일 좋아하는 음식이 뭐야?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇구나.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("파이보는 못 먹어봤어. 어떤 맛이야?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"정말? {user_name}이가 얘기해주니까 배가 고픈 것 같아!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 셰프처럼 멋지게 브이해봐!")
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
