#!/usr/bin/python3
# communication: 의사소통/언어표현

# python module
import os
import sys
import time
import random
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


def Play_Salad(user_name):

    print(f"user name: {user_name} \n")
    #과일 샐러드
    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 방석 다섯개가 필요해 .")
        text_to_speech("방석이 없다면 쿠션이나 수건을 준비해도 좋아.")
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
        text_to_speech(f"먼저 방석을 원 모양으로 놓을거야.그리고 {user_name}이는 과일 카드 다섯가지를 골라줘")
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
                text_to_speech(f"{user_name}이가 고른 과일을 파이보가 맞출 때마다 옆 방석으로 한칸씩 움직이면 돼. ")
                text_to_speech("처음 자리로 돌아오면 놀이가 끝나는거야")
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
        global i
        i=1;
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech("다섯 가지 과일카드를 고르고 첫번째 방석에 앉아봐.")
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    time.sleep(2)
                    text_to_speech(f"좋아.  파이보가 {user_name}이가 생각한 과일을 맞춰볼게.")
                    text_to_speech("맞췄으면 카드를 파이보에게 보여주고한 칸씩 옆자리로 옮기면 돼. 시작해보자!")
                    #행동인식 - 사진, 영상 촬영
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        
        
            
        def start_1():
            fruit=Dic.Fruit
            choicelist=random.choice(fruit)
            global i
            if 1<=i<6:
                behavior_list.do_question_S()
                while True:
                    text_to_speech(f"{random.choice(fruit)}!맞췄어?")#랜덤과일이름
                    #행동인식 - 사진, 영상 촬영       
                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'YES':
                        behavior_list.do_joy()
                        while True:
                            
                            text_to_speech("좋았어. 한칸 옆으로 옮기자!")
                            i=i+1
                            return start_1()
                            
                    else:
                        behavior_list.do_sad()
                        while True:
                            text_to_speech("다시 맞춰 볼게.")
                            return start_1()
                     
            elif i==6:
                behavior_list.do_joy()
                while True:
                    text_to_speech("처음 자리로 돌아왔어! 정말 빨리 도착했는 걸? ")
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
            start()
        else:
            behavior_list.do_praise_L()
            while True:
                text_to_speech(f"{user_name}이는 정말 다양한 과일 이름을 알고 있구나! 멋지다~")
                break
        break
       
    

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 어떤 과일을 제일 좋아해?")
        
        user_said = speech_to_text()
        
        text_to_speech("정말? 어떤 맛이야?")

        user_said = speech_to_text()

        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇구나. 파이보는 과일을 한번도 못 먹어봤어.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("어떤 과일이 제일 상큼해?")
        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그렇구나. 과일들은 모두 상큼할 것 같아!")
        break

    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 상큼한 과일을 먹는 표정을 하고 브이해봐!")
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
