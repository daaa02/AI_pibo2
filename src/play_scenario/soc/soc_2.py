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


def Play_Newspaper(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 신문지가 필요해~ 신문지가 없으면 큰종이도 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = input("답변 : ")
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
        text_to_speech("신문지로 비를 만들거야. 신문지를 길게 찢어서 신문지 비를 내려보자")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = input("답변 : ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("신문지를 겹쳐서 찢으면 비를 많이 만들 수 있어. 찢다가 끊어지지 않게 조심해야 해.")
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_B()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘.")

        user_said = input("답변 : ")
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
        def start_2():
            behavior_list.do_suggestion_S()
            while True:
                text_to_speech("신문지를 찢어 비를 만들어 보자!")
                time.sleep(1)

                behavior_list.do_waiting_A()
                while True:
                    text_to_speech("다 만들었으면 다 만들었다고 말해줘~")

                    user_said = input("답변 : ")
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'DONE':
                        behavior_list.do_suggestion_L()
                        while True:
                            time.sleep(3)
                            #행동인식-사진, 영상촬영
                            text_to_speech("비를 내려보자~ 자리에 서서 신문지 비를 두 손에 쥐고 하늘로 뿌려봐! 시~작.")
                            #비내리는 효과음 3초
                            break
                    else:
                        behavior_list.do_waiting_A()
                        wait_for('DONE')
                        continue
                    break
                break

            behavior_list.do_waiting_A()
            while True:
                #행동인식-사진, 영상촬영
                text_to_speech("정말 멋진 비였어. 이제 바닥에 떨어진 비를 다시 모아보자. 다 모았으면 다 모았다고 말해줘~ ")
                
                user_said = input("답변 : ")
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                        behavior_list.do_suggestion_L()
                        while True:
                            time.sleep(3)
                            #행동인식-사진, 영상촬영
                            text_to_speech("이번에는 누워서 비를 맞아보자~ 자리에 누워서 신문지 비를 두 손에 쥐고 다시 하늘로 뿌려봐! 시~작.")
                            #비내리는 효과음 3초
                            break
                else:
                        behavior_list.do_waiting_A()
                        wait_for('DONE')
                        continue
                break

            behavior_list.do_joy()
            while True:
             #행동인식-사진, 영상촬영
             text_to_speech("신문지 비가 또 내린다~")
             break
            
        start_2()        
    start()

           

    # 2.4 놀이 완료
    behavior_list.do_question_L()
    while True:
        text_to_speech("한 번 더 해볼까? 또 하고 싶으면 또 하자라고 말해줘.")

        user_said = input("답변 : ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'AGAIN':
            behavior_list.do_agree()
            while True:
                text_to_speech("그래 또 하자!")
                start()
        else:
            behavior_list.do_praise_L()
            while True:
                text_to_speech(f"{user_name}이가 내린 신문지 비는 정말 포근했어. 젖지 않는 멋진 비야~")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("신문지 비를 맞으니까 기분이 어땠어? 포근했어?")

        user_said = input("답변 : ")

        
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그런 기분이 들었구나.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 어떤 날씨를 좋아해?")

        user_said = input("답변 : ")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말? 왜 좋아?")
        user_said = input("답변 : ")
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("맞아. 파이보도 좋아해.")
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("우리 둘 다 공통점이 있구나?")
        break



    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 신문지 비를 들고 브이해봐!")
        break

    behavior_list.do_photo()
    time.sleep(5)
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3", out='local', volume=-1000, background=False)

    # 2.7 다음 놀이 제안
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("또 다른 놀이 할까? 파이보랑 또 놀고 싶으면 놀고 싶다고 말해줘!")

        user_said = input("답변 : ")
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
