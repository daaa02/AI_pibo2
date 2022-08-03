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
    tts.play(filename, 'local', '-1500', False)

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break

def Play_Pcup(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 종이컵이 필요해~")
        text_to_speech("종이컵 갯수는 많으면 많을수록 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()    # stt open
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)   # stt 결과 처리 (NLP.py 참고)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(1)
                text_to_speech("좋았어. 놀이 방법을 알려줄게!")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('DONE')    # DONE 답변 들어올 때까지 stt open 반복
            continue
        break

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        text_to_speech("이번 놀이는 종이컵을 던져보고 높게 쌓아보는 놀이야. ")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("놀이 전에 먼저 종이컵의 생김새는 어떤지 살펴보자.")
                text_to_speech("다음엔 어떻게 해야 정확하게 던지고 쌓을 수 있을지 생각해봐.")
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
        behavior_list.do_explain_A()
        while True:
            time.sleep(1)
            text_to_speech("먼저 종이컵을 던져 골인 시킬 곳을 정해봐. 그 곳에 상자나 훌라후프 같은 걸 놓아도 좋아.")
            time.sleep(5)
            break

        behavior_list.do_explain_B()
        while True:
            time.sleep(1)
            text_to_speech("이제 종이컵 여러 개를 손에 들고 다섯 발자국 정도 떨어져 서서  보자. ")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비가 됐으면 준비 됐어 라고 말해줘. ")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    time.sleep(2)
                    text_to_speech("좋아. 이제 종이컵을 골인 시키는거야. 한번에 못 넣으면 또 던져도 돼.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 넣었으면 다 넣었다고 말해줘!")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_praise_L()
                while True:
                    time.sleep(2)
                    #행동인식-사진,영상 촬영
                    text_to_speech("와, 원래 처음에는 어려운데 잘하는걸?")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('YES')
                continue
            break

        behavior_list.do_explain_A()
        while True:
            text_to_speech("이번에는 종이컵 탑을 쌓아보자.")
            text_to_speech("어떤 모양의 탑을 쌓을지 생각해봐.")
            break

        behavior_list.do_question_L()
        while True:
            text_to_speech(f"{user_name}이는 어떤 모양으로 쌓고 싶어?")
            user_said = speech_to_text()
            break

        behavior_list.do_praise_L()
        while True:
            text_to_speech(f"좋은 생각이야! 어떤 모양이든 {user_name}만의 탑을 쌓아봐.")
            
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("끝났으면 끝났어 라고 말해줘!")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    #행동인식-사진,영상 촬영
                    text_to_speech("잘했어! 정말 멋지다.")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

    start()

    # 2.4 놀이 완료

    behavior_list.do_suggestion_L()
    while True:
            text_to_speech("이제 자리에 누워 몸 위에 종이컵을 올려놓자. ")
            text_to_speech("많이 올릴 수록 좋아.")
            break

    behavior_list.do_waiting_C()
    while True:
            text_to_speech("다 올렸으면 다 올렸어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    
                    text_to_speech("좋았어. 이제 내가 하나, 둘, 셋을 세면 벌떡 일어나서 종이컵을 떨어뜨리는 거야.")
                    text_to_speech("자, 준비~ 하나, 둘, 셋!")
                    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/종이컵놀이.wav", out='local', volume=-1000, background=False)
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break
         
    behavior_list.do_question_S()
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
                text_to_speech("종이컵 놀이 정말 잘하더라. 파이보도 그렇게 잘 하고 싶어.")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 오늘 종이컵 놀이 하면서  잘 안 되는 게 있었어? 언제?")
        user_said = speech_to_text()
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech("그렇구나. 파이보는 몰랐어. 그럼 잘 된 건 어떻게 해서 더 잘된 것 같아?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그렇구나. {user_name}이의 생각을 들어보니 정말 그런 것 같아!")
       
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 종이컵을 들고 포즈를 취해봐!")
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
