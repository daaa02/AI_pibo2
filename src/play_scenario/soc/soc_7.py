#!/usr/bin/python3
# social: 사회성/정서

# python module
from ast import While
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


def Play_Stork(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 준비물이 필요없어.놀이 방법을 알려줄게!")
        
        break

    

    # 2.2 놀이 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech(f"먼저 {user_name}이가 엎드려 있으면, 황새가 된 친구가 {user_name}이를 천천히 콕콕 찌를거야. {user_name}이는 친구가 어디를 찔렀는지 맞추면 돼.")
        break
    
    behavior_list.do_question_L
    while True:

        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("정답을 못맞추면 황새가 콕콕 찌르는 속도가 빨라질거야. 황새는 사람이 아프지 않게 살살 찔러야해. ")
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
            behavior_list.do_suggestion_S()
            while True:
                text_to_speech(f"바닥에  {user_name}이는 엎드리고 친구는 옆에 앉아줘.")
                time.sleep(1)
                break
              
            def start_1():
                global i
                behavior_list.do_waiting_A()
                while True:
                    text_to_speech("준비가 다 됐으면 준비 됐어 라고 말해줘~")

                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_explain_B()
                        while True:
                            
                            text_to_speech("황새는 목표 신체부위를 마음속으로 정해줘.")
                            time.sleep(5)
                            text_to_speech("시작할게!")
                            break
                    else:
                        behavior_list.do_waiting_A()
                        wait_for('DONE')
                        continue
                    break
                  

                behavior_list.do_explain_A()
                while True:
                    time.sleep(1)
                    text_to_speech("황새가 콕콕 찌르기 시작했어.")
                    break

                behavior_list.do_waiting_A()
                while True:
                    time.sleep(1)
                    text_to_speech("사람은 황새가 찌르는 신체 부위를 이야기 해줘.")
                    break

                behavior_list.do_explain_A()
                while True:
                    text_to_speech("황새가 찌른 신체부위를 맞췄으면 맞았어 라고 해줘")
                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'YES':
                        behavior_list.do_praise_S()
                        while True:
                            text_to_speech("정말 잘 알아채는 걸?또 해보자!")
                            break
                    else:
                        behavior_list.do_waiting_C()
                        wait_for('YES')
                        continue
                    break    

                behavior_list.do_explain_A()
                while True:
                    time.sleep(1)
                    text_to_speech("황새는 목표 신체 부위를 마음속으로 정해줘. ")
                    break

                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(5)
                    text_to_speech("시작할게!")
                    break

                behavior_list.do_explain_A()
                while True:
                    time.sleep(1)
                    text_to_speech("황새가 콕콕 찌르기 시작했어.")
                    break

                behavior_list.do_waiting_A()
                while True:
                    time.sleep(1)
                    text_to_speech("사람은 황새가 찌르는 신체 부위를 이야기 해줘.")
                    break

                behavior_list.do_explain_B()
                while True:
                    text_to_speech("황새가 찌른 신체부위를 맞췄으면 맞았어 라고 해줘")
                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'YES':
                        behavior_list.do_joy()
                        while True:
                            text_to_speech("정말 빠르다~")
                            break
                    else:
                        behavior_list.do_waiting_C()
                        wait_for('YES')
                        continue
                    break

                 
                if i == 1:

                    behavior_list.do_suggestion_L()
                    while True:            
                        text_to_speech(f"이번에는  역할을 바꿔보자. 친구가 엎드리면 {user_name}이가 황새처럼 콕콕 찔러줘. ")
                        text_to_speech("*** 2회차 ***")
                        i=i+1
                        return start_1()                    
                        
                elif i==2:
                    behavior_list.do_praise_S()
                    while True:
                    #행동인식 - 사진, 영상 촬영
                        text_to_speech("황새 역할도 재미있게 잘 하는걸?")
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
                text_to_speech(f"{user_name}이는 다양한 신체 부위 명칭을 알고 있구나? 대단해~")
                break
        break





           
    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 어떤 부위가 제일 간지러웠어?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("정말? 신기하다.")
        break

    behavior_list.do_sad()
    while True:
        text_to_speech("이건 비밀인데 파이보는 간지러움을 잘 못 느껴. ")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이도 비밀이 있어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그렇구나. 둘만의 비밀이 생기다니 파이보는 기뻐!")
        break

    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 황새를 표현해봐!")
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
