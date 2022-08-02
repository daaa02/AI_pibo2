#!/usr/bin/python3
# communication: 의사소통/언어표현

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


def Play_Parcel(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 훌라후프, 종이와 그림도구, 가위, 테이프가 필요해~")
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
        text_to_speech("종이에 과일을 그리고 오린 다음에 공에 붙이면 과일 택배가 완성돼. 과일 택배는 손으로 굴려서 훌라후프 안에 넣을거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                text_to_speech("과일택배를  빠르게 훌라후프 안으로 배달해보자.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘")

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
        
         behavior_list.do_question_L()
         while True:
            time.sleep(1)
            text_to_speech(f"{user_name}이가 좋아하는 과일카드를 보여줘. 카드가 없으면 이름을 말해도 좋아.")
            
            user_said = speech_to_text()
            fruit = NLP.nlp_fruit(user_said=user_said, dic=Dic)
            break

         behavior_list.do_suggestion_S()
         while True:
            text_to_speech(f"{fruit}이네. 그러면 {fruit}를 종이에 그려보자! ")

            
            break

         behavior_list.do_waiting_A()
         while True:
          text_to_speech("다 그리면 다 그렸어 라고 말해줘~")

          user_said = speech_to_text()
          answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

          if answer == 'DONE':
             behavior_list.do_praise_S()
             while True:
                time.sleep(2)
                text_to_speech(f"정말 맛있어 보이는 {fruit}이다.")
                break
          else:
            behavior_list.do_waiting_A()
            wait_for('DONE')
            continue
          break
    

         behavior_list.do_waiting_A()

         while True:
          text_to_speech("이제 그림을 오려서 공에 붙이면 과일 택배 완성이야. 다 붙이면 다 붙였어 라고 말해줘~")

          user_said = speech_to_text()
          answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

          if answer == 'YES':
            behavior_list.do_suggestion_L()
            while True:
                time.sleep(2)
                text_to_speech(f"좋아.이제 훌라후프를 바닥에 놓고 훌라후프 바깥에 {user_name}이가 서.")
                break
          else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
          break

         behavior_list.do_joy()
         while True:
          text_to_speech("내가 시~작! 하면 공을 손으로 굴려서 훌라후프 안으로 배달해 보자! 준비~~ 시작!")

          time.sleep(5) 
          break

         behavior_list.do_waiting_A()
         while True:
          text_to_speech("다 옮겼으면 다 옮겼어 라고 말해줘~")

          user_said = speech_to_text()
          answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

          if answer == 'YES':
            behavior_list.do_praise_S()
            while True:
                time.sleep(2)
                text_to_speech("정말 빠르게 배달했는걸?")
                break
          else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
          break


        # 2.4 놀이 완료

         behavior_list.do_question_S()
         while True:
            text_to_speech("한 번 더 해볼까? 또 하고 싶으면 또 하자라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'AGAIN':
                behavior_list.do_agree()
                text_to_speech("그래 또 하자!")
                start()
            else:
                behavior_list.do_praise_S()
                while True:
                    text_to_speech("과일 택배를 열심히 배달했어. 고생했어!")
                    break
            break

    start()

    

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name} 이는 어떤 과일을 좋아하고, 어떤 과일을 싫어해?")
        time.sleep(3)
    

        user_said = speech_to_text()
        

        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("정말? 왜 싫어해?")
        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇구나. 파이보는 상큼한 향이 나는 과일이 좋아. ")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 좋아하는 향기가 있어?")

        user_said = speech_to_text()

    
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("맞아. 정말 좋지. 생각만 해도 기분이 좋다~")

        break

    

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 과일 택배를 들고 브이해봐!")
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
