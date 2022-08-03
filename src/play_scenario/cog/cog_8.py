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

def Play_Sound(user_name):
    
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 여러가지 소리 나는 도구들이 필요해~")
        text_to_speech(" 열쇠 고리, 접시와 수저, 냄비 뚜껑, 신문지, 책 같은걸 준비하면 좋아.")
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
        text_to_speech("이번 놀이는 한 사람은 눈을 감고  다른 사람은 물건을 이용해서 소리를 낼거야. 눈을 감은 사람은 어떤 물건의 소리인지 알아 맞추면 돼.")
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
                text_to_speech("좋았어! 먼저 각각의 물건들을 관찰해 보고, 소리를 들어보면 쉬울거야.")
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
        behavior_list.do_explain_B()
        while True:
            time.sleep(1)
            text_to_speech(f"먼저 {user_name}이가 소리를 내고 친구가 맞춰보기를 하자. 눈을 꼭 감고 뒤를 돌아서 소리를 집중해서 듣는 거야. ")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비가 됐으면 준비됐어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    time.sleep(2)
                    text_to_speech("이제 열심히 두드려봐. ")
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("어떤 소리가 나? 정답을 맞췄어?")
            user_said = speech_to_text()
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("좋아. 정말 훌륭한 소리였어.")
            
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이제 역할을 바꿔보자. {user_name}이는 눈을 꼭 감고 뒤를 돌아 앉아보는거야.")
            
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비가 됐으면 준비됐어 라고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    time.sleep(2)
                    text_to_speech("이제 열심히 두드려봐. ")
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("어떤 소리가 나? 정답을 맞췄어?")
            user_said = speech_to_text()
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech("물건을 보지 않고도 정말 잘 알아채는 구나!")
            
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
                text_to_speech(f"열심히 놀이해 준 {user_name}이가 최고야~ 파이보도 다양한 소리를 알게 된 것 같아!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 사용한 물건들을 제자리에 가져다 놓자~")
        break

    behavior_list.do_waiting_C
    while True:

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
        text_to_speech("오늘 소리 맞추기 놀이할 때, 문제 내는게 재미있었어, 맞추는게 재미있었어?")

        user_said = speech_to_text()

        text_to_speech("정말? 어떤 소리가 가장 맞추기 어려웠어?")

        user_said = speech_to_text()
        break

    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"그랬구나. 파이보는  {user_name}이가 소리를 집중해서 듣는 모습이 멋졌어~")
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
