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

def Play_cup(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 컵받침이 필요해~")
        text_to_speech("깨지지 않는 종이나 나무로 된 컵받침이 필요해. 많으면 많을수록 좋아.")
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
        text_to_speech("이번 놀이는 컴받침을 쌓아보고 모양을 만들어 보는 놀이야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지?할 수 있으면 할 수 있어라고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 컵받침을 쌓고 모양을 만든 뒤에는 컵받침의 개수를 세어 볼 거야.")
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
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech("먼저 곳곳에 휴지 섬을 만들자. ")
            break

        behavior_list.do_explain_B()
        while True:
            time.sleep(1)
            text_to_speech("컵받침을 높이 쌓아봐.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    time.sleep(2)
                    text_to_speech("이제 높이 쌓은 컵받침의 개수를 세어보자!")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 세면 몇 개인지 말해줘.")
            #행동인식 - 사진, 영상 촬영
            user_said = speech_to_text()
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech(f"{user_name}이는 정말 수를 잘 세는구나!")
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("이제 컵받침을 하나씩 빼면서 남은 개수를 세어보자.")
            
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 했으면, 다 했다고 말해줘!")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("제법인걸?")
                   
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("이제 컵받침을 바닥에 깔아보자.")
            text_to_speech("세모, 네모, 동그라미 같은 다양한 모양을 만들 거야.")
            
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("할 수 있지?")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_S()
                while True:
                    text_to_speech("좋았어. 재밌는 모양으로 만들어보자.")
                   
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('YES')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 만들고 나면 컵받침이 몇 개 필요한지 알려줘.")
            #행동인식 - 사진, 영상 촬영
            user_said = speech_to_text()
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech(f"굉장하다. {user_name}이는 정말 똑똑한 것 같아. ")
            break    

    start()

    # 2.4 놀이 완료

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 바닥에 누워봐. 누워서 몸에 컵받침을 올려 보자.")
        text_to_speech("떨어뜨리지 않고 1분 동안 쉬어 보는 거야.")
        break

    behavior_list.do_waiting_C()
    while True:
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘!")
        time.sleep(1)

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)
        time.sleep(60)

        if answer == 'DONE':
            behavior_list.do_suggestion_S()
            while True:
                text_to_speech("1분이 지났어. 정말 대단해!")
                
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
            behavior_list.do_praise_S()
            while True:
                text_to_speech(f"열심히 따라해준 {user_name}이가 최고야~ 파이보도 똑똑해진 것 같아!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 사용한 컵받침을 정리하자~")
        time.sleep(5)

        text_to_speech("정리가 끝나면 다 했어 라고 말해줘. ")
        
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
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
        text_to_speech("오늘 컵받침 놀이는 재미있었어?")

        user_said = speech_to_text()

        text_to_speech("정말? 어렵진 않았어?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 파이보는 {user_name}가 열심히 놀이 하는 모습이 멋졌어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 컵받침을 들고 브이를 해봐!")
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
