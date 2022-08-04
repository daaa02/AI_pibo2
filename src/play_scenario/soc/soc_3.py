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



def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)        # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Newspaper(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 신문지가 필요해~")
        text_to_speech("신문지가 없으면 큰 종이도 좋아.")
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
        text_to_speech("노래가 시작되면 신문지 땅 위에 올라가서 춤을 춰야돼. 노래가 나올 때는 신문지 땅 밖으로 나올 수 없고, 노래가 끝나면 나올 수 있어.")
        break

    behavior_list.do_waiting_A()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                text_to_speech("노래가 끝나고 다시 시작될 때마다 신문지를 반으로 접어서 땅이 좁아지게 만들 거야. 점점 어렵겠지?")
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
        behavior_list.do_suggestion_L()
        while True:
            
            text_to_speech("노래가 시작됐어. 먼저 바닥에 신문지를 깔고 신문지 위에 올라가서 마음껏 춤춰보자!")
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/신문지위에서기.mp3", out='local', volume=-1000, background=False)
            #행동인식-사진,영상촬영
            break
        
        def start_1():
            global i 
            if 1<=i<3: 
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(15)
                    text_to_speech("노래가 끝났어. 신문지 땅 밖으로 나와도 좋아.")
                    break

                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("신문지를 반으로 접자. 몇 번 접었는지 이따 물어볼테니 잘 기억해 둬야해.")
                    break

                behavior_list.do_waiting_C()
                while True:
                    text_to_speech("다 접었으면 다 했어 라고 말해줘~")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_praise_S()
                        while True:
                            time.sleep(2)
                            text_to_speech("신문지 땅이 좁아졌구나!")
                            break
                    else:
                        behavior_list.do_waiting_A()
                        wait_for('DONE')
                        continue
                    break
            if 1<=i<=2:        
                behavior_list.do_suggestion_L()
                while True:
                    time.sleep(5)
                    text_to_speech("노래가 다시 시작 됐어. 신문지 위에 다시 올라가서 마음껏 춤춰보자.")
                    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/신문지위에서기.mp3", out='local', volume=-1000, background=False)
                    i=i+1
                        

                    start_1()
                    break

            elif i==3:
                behavior_list.do_question_S()
                while True:
                    text_to_speech("신문지를 몇번 접었는지 기억나?숫자로 몇번인지 말해줘~")

                    user_said = speech_to_text()
                    answer = NLP.nlp_number(user_said=user_said, dic=Dic)
                    #답변인식-정답
                    if answer == 3:
                        behavior_list.do_praise_S()
                        text_to_speech(f"대단한걸? {user_name}이는 기억력이 좋구나!")
                        
                    else:
                        behavior_list.do_suggestion_S()
                        while True:
                            text_to_speech("정답은 3번이야!")
                            break
                    break
                

        start_1()    
    start()

        # 2.4 놀이 완료

        

    behavior_list.do_question_L()
    while True:
        text_to_speech("또 해볼까? 또 하고 싶으면 또 하자고 말해줘.")

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
                text_to_speech(f"오늘 정말 열심히 춤췄어. 파이보는 {user_name}이가 신나게 춤추는 모습이 정말 좋아!")
                break
        break

    

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech("춤추니까 기분이 어땠어?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그런 기분이 들었구나. ")
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("파이보는 같이 노래 듣고 춤춰서 정말 즐거웠어")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 어떤 노래를 좋아해?")
        user_said = speech_to_text()
        text_to_speech("정말? 왜?")
        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그렇구나. 나중에 파이보에게도 꼭 불러줘!")
        break

    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 신문지를 들고 브이해봐!")
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
