#!/usr/bin/python3
# cognition: 인지/지각/사고

# python module
import os
from re import T
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

def Play_World(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 천이 한장 필요해~")
        text_to_speech("보자기나 손수건 처럼 얇고 가벼운 천이면 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘~")
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
        text_to_speech("이번 놀이는 보자기 안에 물건을 숨기고 맞춰보는 놀이야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 보자기 안에 든 물건을 맞추기 위해 스무 고개를 해 볼 거야.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘~")

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
            text_to_speech(f"먼저 물건을 숨길 사람과 맞출 사람을 정해야 해. {user_name}이가 먼저 맞춰보자.")
            text_to_speech(f"친구가 물건을 숨기는 동안 {user_name}이는 눈을 감고 있어.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("친구는 다 숨기고 다 숨겼어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech(f"자, 이제 {user_name}이가 눈을 떠!")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('YES')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("스무 고개를 해 보자. 어떤 물건인지 맞출 수 있도록 질문을 해 보는 거야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("정답을 알겠으면 정답이라고 외쳐줘.")

            user_said = speech_to_text()
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("정답을 맞췄어?")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("대단한걸? 정말 빨리 맞췄어.")
                    break
            else:
                behavior_list.do_suggestion_L()
                text_to_speech("아쉽다! 거의 맞출 수 있었는데! 이제 정답을 이야기 해줘!")
                user_said = speech_to_text()
                wait_for('YES')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이번엔 {user_name}이가 물건을 숨겨보자. 물건을 숨기는 동안 친구는 눈을 감아줘.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech(f"{user_name}이는 다 숨기고 나면 다 숨겼어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("자, 이제 눈을 뜨고 스무 고개를 해 보자.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('YES')
                continue
            break
        
        behavior_list.do_waiting_B()
        while True:
            text_to_speech("친구는 정답을 알겠으면 정답이라고 외쳐줘.")

            user_said = speech_to_text()
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("정답을 맞췄어?")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("정말 잘 맞추는 구나!")
                    break
            else:
                behavior_list.do_suggestion_L()
                text_to_speech("아쉽다! 정답이 뭐야?")
                user_said = speech_to_text()
                wait_for('YES')
                continue
            break

    start()

    # 2.4 놀이 완료
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
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"열심히 놀이해준 {user_name}이가 최고야~ 파이보도 똑똑해진 것 같아!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 사용한 물건을 제자리에 가져다 놓자~")
        time.sleep(5)

        text_to_speech("정리가 끝나면 다 했어 라고 말해줘.")
        

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"{user_name}이는 정리도 잘 하는구나!")
                time.sleep(1)
                break
        else:
            behavior_list.do_waiting_C()
            wait_for('DONE')
            continue
        break

    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("오늘 보자기 안에 있던 물건 중에 가장 좋아하는 물건은 뭐야?")

        user_said = speech_to_text()

        text_to_speech("정말? 그렇구나~ 가장 맞추기 힘들었던 물건은 뭐야?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 파이보는 {user_name}가 질문도 잘 하고 놀이를 재치 있게 잘 했다고 생각해~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 보자기를 들고 브이를 해봐!")
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
