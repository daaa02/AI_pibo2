#!/usr/bin/python3
# cognition: 인지/지각/사고

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

def Play_Fisherman(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 준비물이 필요 없어. 놀이 방법을 알려줄게!")
        
        break

    

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        text_to_speech("이번 놀이는 어부 역할과 나그네 역할이 필요해. 어부는 강을 건너가는 방법을 알려주고, 나그네는 그 동작을 흉내 내며 건너가면 돼.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 함께 상상의 강을 건너보자. 강은 수영해서 갈 수도 있고, 노를 저어 갈 수도 있어.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비 됐으면 시작하자고 말해줘.")

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
            time.sleep(1)
            text_to_speech("방 한가운데 상상의 강을 만들어보자~ 몸으로 상상의 강을 표현해 봐.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("강을 다 만들었으면 다 만들었어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    time.sleep(2)
                    text_to_speech(f"{user_name}이가 먼저 강을 건너는 나그네 역할을 해보자. 어부역할 친구는 상상의 강 한가운데 배를 타고 기다릴 거야.노를 젓는 흉내를 내줘.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break
        
        def start_1(): 
            global i  
            behavior_list.do_waiting_B()
            while True:
                text_to_speech("준비가 됐으면 준비 됐어 라고 말해줘.")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_suggestion_L()
                    while True:
                        time.sleep(2)
                        text_to_speech("이제 어부한테 물어보자. “어부야, 어부야, 물이 얼마나 깊니?” 나를 따라해 봐. 시작!")
                        user_said = speech_to_text()
                        break
                else:
                    behavior_list.do_waiting_B()
                    wait_for('DONE')
                    continue
                break

            behavior_list.do_praise_S()
            while True:
                time.sleep(1)
                text_to_speech("잘했어!")
                break

            behavior_list.do_suggestion_S()
            while True:
                time.sleep(1)
                text_to_speech("이번엔 어부가 대답해줘.")
                user_said = speech_to_text()
                break

            behavior_list.do_suggestion_L()
            while True:
                time.sleep(1)
                text_to_speech("이제 어부에게 한번 더 물어보자. “어부야, 어부야, 물을 어떻게 건너갈 수 있니?” 나를 따라해 봐. 시작!")
                user_said = speech_to_text()
                break

            behavior_list.do_praise_S()
            while True:
                time.sleep(1)
                text_to_speech("잘 따라했어!")
                break

            behavior_list.do_waiting_A()
            while True:
                time.sleep(1)
                text_to_speech("이제 어부가 어떻게 건너갈 수 있는지 동작을 알려줘.")
                user_said = speech_to_text()
                break

            
            if i == 1:    
                behavior_list.do_waiting_B()
                while True:
                    text_to_speech("좋았어. 어부가 정하는 대로 강을 다 건너왔으면 다 왔어 라고 말해줘.")
                    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/어부.wav", out='local', volume=-1000, background=False)
                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_praise_S()
                        while True:
                            time.sleep(2)
                            text_to_speech("정말 잘 했어. 무사히 건너왔어.")
                            
                            break
                    else:
                        behavior_list.do_waiting_B()
                        wait_for('DONE')
                        continue
                    break
                    
                behavior_list.do_explain_A()
                while True:
                    print("***1회차***")
                    text_to_speech(f"이제 역할을 바꿔보자. {user_name}이가 어부가 되는 거야.")
                    i=i+1
                    start_1()
                    break
                        
            elif i==2:
                behavior_list.do_waiting_C()
                while True:
                    text_to_speech("좋았어. 어부가 정하는 대로 강을 다 건너왔으면 다 왔어 라고 말해줘.")
                    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/어부.wav", out='local', volume=-1000, background=False)
                    user_said = speech_to_text()
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_praise_S()
                        while True:
                            time.sleep(2)
                            text_to_speech("두 사람 모두 상상의 강을 열심히 건넜어!")
                            break
                    else:
                        behavior_list.do_waiting_B()
                        wait_for('DONE')
                        continue
                    break            
        start_1()
    start()


    # 2.4 놀이 완료
    behavior_list.do_question_S()
    while True:
        text_to_speech("또 해볼까? 또 하고 싶으면 또하자고 말해줘~")

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
                text_to_speech(f"열심히 놀이해 준 {user_name}이가 최고야~ 정말 신났어!")
                break
        break

    # 2.5 마무리 대화
    

    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 강을 건너는 나그네가 재밌었어,  어부 역할이 재밌었어?")

        user_said = speech_to_text()

        text_to_speech("정말? 어떤 점이 재미있었어?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그래서 재밌었구나. {user_name}이가 정말 신나 보였어.")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 강을 건너는 것 처럼 포즈를 취해봐!")
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

        if answer == 'AGAIN':       # 지금은 어떤 답변이라도 프로그램 종료됨
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
