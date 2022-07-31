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
        text_to_speech("이번 놀이는 빨래집게가 필요해~")
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
        text_to_speech("서로의 옷에 빨래집게를 꽂아서 인디언 옷을 만들거야! ")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있어 라고 말해줘~")
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("인디언 옷을 완성하면신나게 춤을 추면서 집게를 떨어트릴 거야. ")
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
            text_to_speech("빨래집게를 서로의 옷에 꽂아서 인디언 옷을 만들자!")
            time.sleep(1)

            behavior_list.do_waiting_A()
            while True:
                text_to_speech("완성이 되면 다됐어 라고 말해줘.")

                user_said = speech_to_text()
                answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                if answer == 'DONE':
                    behavior_list.do_joy()
                    while True:
                        time.sleep(3)
                        text_to_speech("정말 멋진 인디언 옷이다!파이보가 신나는 음악을 틀어줄게. 춤추면서 집게를 떨어트려봐.")
                        break
                else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
                break
            break

        behavior_list.do_joy()
        while True:
            #행동인식-사진, 영상 촬영
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/인디언.mp3", out='local', volume=-1000, background=False)
            text_to_speech(" 신난다~집게를 다 떨어트리면 다됐어 라고 말해줘!")
            
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                    behavior_list.do_praise_L()
                    while True:
                        time.sleep(3)
                        #행동인식-사진, 영상 촬영
                        text_to_speech("진짜 빠르다! 춤을 정말 열심히 췄는걸?")
                        break
            else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
            break

        behavior_list.do_suggestion_L()
        while True:
            
            
            text_to_speech("이제 집게를 색깔 별로 정리해보자.")
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("다 정리하면 다했어 라고 말해줘~")
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                    behavior_list.do_praise_L()
                    while True:
                        time.sleep(3)
                        
                        text_to_speech(f"정말 깔끔하다. {user_name}이는 정리도 잘하는 구나!")
                        break
            else:
                    behavior_list.do_waiting_A()
                    wait_for('DONE')
                    continue
            break
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
                text_to_speech(f"인디언 옷을 멋지게 만들고 춤추니까 더 멋졌어. {user_name}이는 최고의 댄서야~")
                break
        break

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("오늘 인디언이 되보니까 기분이 어땠어?")
        user_said = speech_to_text()

        
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"그런 기분이었구나. {user_name}이랑 춤 출 때마다 파이보는 정말 신나!")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech("빨래집게로 옷을 만들어 보니 어땠어? 아프진 않았어?")

        user_said = speech_to_text()
        break

    behavior_list.do_explain_A()
    while True:
        text_to_speech("그랬구나. 천천히 느슨하게 꽂으면 빨래집게도 안 아프게 가지고 놀 수 있어.")
        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech("어려웠을텐데 잘 해냈어!")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 바른 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 집게를 들고 브이해봐!")
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
