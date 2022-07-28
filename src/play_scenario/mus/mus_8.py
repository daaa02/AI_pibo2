#!/usr/bin/python3
# muscle: 대근육/소근육

# python module
import os
import sys
import time

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(string):
    filename = "tts.wav"
    print("\n" + string + "\n")
    tts.tts_connection(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{string}<break time='500ms'/></prosody></voice>\
                </speak>", filename)
    tts.play(filename, 'local', '0', False)
    
def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Chef(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 나무주걱, 테이프, 소프트볼이 필요해~")
        time.sleep(1)
        text_to_speech("소프트볼이 없으면 풍선을 작게 불어서 묶어도 돼.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘~")
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
        text_to_speech("나무로 된 주걱이 요리사 도구야.")
        time.sleep(1)
        text_to_speech("주걱 위에 놓인 호박을 풍선이라 생각하고 떨어트리지 않고 운반하는 거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("어렵지 않지? 할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 요리사는 체력 연습도 할 수 있어.")
                time.sleep(1)
                text_to_speech("주걱 위에 풍선을 올려 놓고 앉았다 일어서는 연습을 하는 거야.")
                break
        else:
            behavior_list.do_waiting_B()
            wait_for('YES')
            continue
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("할 수 있지? 준비가 됐으면 시작하자고 말해줘.")

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
            text_to_speech("우선 목표점과 출발선을 정해야 해.")
            time.sleep(1)
            text_to_speech("출발할 위치에 테이프를 붙이고, 도착할 목표점에도 테이프를 붙이면 돼.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("잘했어! 이젠 공을 호박이라고 생각하고 재료를 들고 출발점에서 목표점까지 움직여보자~")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("우와 정말 빠른걸? 이제 체력 연습을 해보자.")
                    time.sleep(1)
                    text_to_speech("주걱 위에 공을 올리고 앉았다 일어나는 거야!)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("앉을 준비가 됐으면 준비 됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("좋았어! 내가 천천히 열까지 셀 동안 해보는 거야.")
                    time.sleep(1)
                    text_to_speech("중간에 공을 떨어뜨리면 다시 시작해도 돼.")
                    tiem.sleep(1)
                    text_to_speech("몇 번 성공했는지 세었다가 알려줘. 그럼 준비~ 시작!")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break


        behavior_list.do_question_L()
        while True:
            time.sleep(1)
            text_to_speech("하나, 두울, 세엣, 네엣, 다섯, 여섯, 일곱, 여덟, 아홉, 열!") 
            time.sleep(1)
            text_to_speech("이제 그만~ 몇 번 성공 했어?")

            user_said = speech_to_text()

            break

        behavior_list.do_praise_L()
        while True:
            text_to_speech("익숙하지 않았을 텐데 대단해!")
            time.sleep(1)
            text_to_speech(f"{user_name}이가 다리가 더 튼튼해진 것 같아!")
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("주걱을 꼭 쥐느라 손목 힘을 많이 사용했으니 손목을 부드럽게 돌려 봐.")
        time.sleep(1)
        text_to_speech("10초 동안 마사지 시작!")
        #time.sleep(10) 
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("손목이 좀 편안해졌지?")
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
                text_to_speech("정말 멋진 요리사 훈련 놀이였어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("어때? 요리사 훈련 해 보니까 진짜 요리사가 된 기분이 들었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("오늘 놀이에서 어려운 게 있었어?")

        user_said = speech_to_text()

        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech("그랬구나. 열심히 하는 모습이 보기 좋았어!")
        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그렇구나. 풍선을 안 떨어트리려고 할 때 힘이 많이 들것 같았어.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"{user_name}이는 어땠어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("우와 그래도 멋지게 해냈구나.")
        time.sleep(1)
        text_to_speech(f"{user_name}이가 힘들어도 끝까지 하는 모습이 보기 좋았어~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 나무 주걱을 멋지게 들고 브이를 해봐!")        
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

Play_Chef("슬기")