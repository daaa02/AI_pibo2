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


def Play_Indian(user_name):
    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 의자랑 담요가 필요해. ")
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
        time.sleep(1)
        text_to_speech("친구와 인디언 집을 만들거야. 의자를 양 쪽에 세우고 그 위에 담요를 덮으면 돼. ")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech(" 담요가 흘러 내리면 빨래집게로 고정해도 돼.")
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
        
        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("의자랑 담요로 인디언 집을 만들자.")
            time.sleep(1)

            behavior_list.do_waiting_A()
            while True:
                text_to_speech("완성이 되면 다 됐다고 말해줘.")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_praise_S()
                    while True:
                        time.sleep(3)
                        text_to_speech("멋지게 잘 만들었는걸?")
                        break
                else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
                break
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"이제 인디언 집 내부를 꾸며 보자.{user_name}이와 친구가 좋아하는 장난감이나 인형으로 꾸밀 수 있어. ")
            
            behavior_list.do_waiting_A()
            while True:
                text_to_speech("다 꾸미면 다 됐다고 말해줘.")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_joy()
                    while True:
                        time.sleep(3)
                        text_to_speech("너무 기대된다! 파이보를 인디언 집에 데려가줘.")
                        break
                else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
                break
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("도착하면 도착했다고 말해줘! ")
            
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                    behavior_list.do_joy()
                    while True:
                        time.sleep(3)
                        text_to_speech("우와~ 정말 아늑하다!다 같이 편하게 누워보자!")
                        break
            else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("다 눕고 누웠어 라고 말해줘~")
            
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                    behavior_list.do_joy()
                    while True:
                        time.sleep(3)
                        text_to_speech("눈을 감고 귀 기울려봐. 숲소리가 들리는 것 같아.")
                        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/숲소리.wav", out='local', volume=-1000, background=False)
            
                        break
            else:
                    behavior_list.do_waiting_A()
                    wait_for('YES')
                    continue
            break
    start()


    # 2.4 놀이 완료
    behavior_list.do_question_L()
    while True:
        text_to_speech("인디언 집을 또 만들어볼까? 또 하고 싶으면 또하자라고 말해줘.")

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
                text_to_speech(f"인디언 집을 정말 멋지게 만들었어. 열심히 만든 {user_name}이 최고야!")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이가 만든 집에서 쉬니까 어땠어? 포근한 기분이 들었어?")

        user_said = speech_to_text()

        
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나. 파이보는 마치 엄마품에 있는 것 같아서 마음이 편했어. ")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 언제 제일 마음이 편해?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("정말? 생각만 해도 기분이 좋다.")
        break

   

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 인디언 집 앞에서 브이해봐")
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
