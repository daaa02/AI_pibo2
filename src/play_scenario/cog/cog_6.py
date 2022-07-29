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

def Play_Fashion(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 보자기, 빨래집게가 필요해~ ")
       
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
        text_to_speech("이번 놀이는 보자기에 빨래집게를 꽂아서 멋진 옷을 만들어 볼 거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("옷을 완성한 다음에는 모델처럼 패션쇼를 해 볼거야.")
                text_to_speech(f"먼저 {user_name}이가 모델역할을 하고 친구가 디자이너가 돼서 옷을 만들도록 하자.")
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
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech(f"모델 {user_name}이는 가만히 서서 디자이너가 옷을 만드는 동안 기다려줘.")
            break

       

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("옷이 멋지게 완성되면 다 됐어 라고 말해줘. 그럼 시작!")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    time.sleep(2)
                    text_to_speech("정말 멋진 옷이다!")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이젠 예쁜 보자기 옷을 입은 모델이 패션쇼를 해 보자.")
            text_to_speech("모델이 옷을 입고 멋지게 걷다가 마지막 부분에서 멋진 자세를 취하는 거야~")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech(" 멋지다! 진짜 모델 같아.")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이제 {user_name}이도 옷을 만들어보자. 모델 신체에 보자기를 두르고 빨래집게를 고정하는 거야! ")
            
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("할 수 있지?")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("좋았어.친구에게 멋진 옷을 만들어 주자. ")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('YES')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("완성되면 다 됐어 라고 말해줘. 그럼 시작!")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech(f"굉장하다. {user_name}이의 멋진 보자기 옷이 모델을 더 아름답게 만들어 주는 것 같아! ")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이제 모델이 옷을 입고 멋지게 걷다가 마지막 부분에서 멋진 자세를 취해줘~")
            
            break


        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")
            
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_joy()
                while True:
                    text_to_speech("정말 멋진 패션쇼였어!")
                    
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("이제 옷을 만들었던 보자기와 집게를 풀어서 정리하자.")
            time.sleep(5)
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
                text_to_speech(f"열심히 놀이해 준 {user_name}이가 최고야~ 파이보도 아름다워진 것 같아!")
                break
        break

    # 2.5 마무리 대화

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech(f"{user_name}이는 전에도 보자기를 본 적이 있어?")
        
        break

    behavior_list.do_waiting_C()
    while True:
        text_to_speech("보자기는 어디에 쓰는 물건일까?")
        user_said = speech_to_text()
        time.sleep(1)
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"정말 재미있는 생각이다. {user_name}는 보자기로 진짜 옷을 만들면 어떨 것 같아?")
        user_said = speech_to_text()
        time.sleep(1)
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그런 생각을 했구나!")
        
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 오늘 패션쇼 놀이에서 디자이너가 재미있었어? 모델이 재미있었어?")
        user_said = speech_to_text()
        time.sleep(1)
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 파이보는 {user_name}가 아름답게 표현하는 모습이 멋졌어~")
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
