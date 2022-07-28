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


def Play_Flower(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 준비물이 필요 없고 벽 앞에 술래가 서야 돼!")
        time.sleep(1)
        text_to_speech("벽을 정하고 준비가 되면 준비 됐다고 말해줘~")
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
        text_to_speech("술래는 벽을 보고 서있을거야.")
        time.sleep(1)
        text_to_speech("술래가 '무궁화 꽃이 피었습니다'를 말하는 동안 친구들은 술래를 향해 조금씩 다가면 돼.")
        time.sleep(1)
        text_to_speech("술래가 뒤돌아 보면 다른 친구들은 제자리에서 멈춰야해.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_joy()
            while True:
                text_to_speech("좋았어!")
                break
        else:
            behavior_list.do_waiting_B()
            wait_for('YES')
            continue
        break

    behavior_list.do_explain_B()
    while True:
        text_to_speech("술래가 뒤돌아 볼 때 움직이는 친구는 탈락이고 술래에게 무사히 도착하면 성공이야.")
        time.sleep(1)
        text_to_speech(f"{user_name}이가 먼저 술래를 해보자.")
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("각자 자리에 준비가 됐으면 시작하자고 말해줘.")

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
            text_to_speech("술래는 벽을 보고 ‘무궁화 꽃이 피었습니다.’하고 외치는 거야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("여러 번 하다가 놀이가 끝났으면 끝났어를 외쳐줘. 시작!")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_question_S()
                while True:
                    text_to_speech("좋았어! 움직인 사람 있어?")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'YES':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("움직인 사람은 술래에게 가서 손가락을 걸어.")
                    time.sleep(1)
                    text_to_speech("술래는 다시 구호를 외쳐줘.")
                    start()
                    break
            elif answer == 'NO':
                behavior_list.do_suggestion_S()
                while True: 
                    text_to_speech("술래는 다시 구호를 외쳐줘.")
                    start()
                    break
            elif answer = 'DONE':
                behavior_list.do_suggesion_L()
                while True:
                    text_to_speech("와, 정말 잘한다. 파이보도 그렇게 빨리 움직일 수 있으면 좋겠어.")
                    time.sleep(1)
                    break        
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("잠시 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("열심히 놀이했으니 잠시 누워서 휴식 하자! 1분 동안 휴식 시작!")
        #time.sleep(60) 
        break
    
    behavior_list.do_question_S()
    while True:
        text_to_speech("정말 편하지?")
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
                text_to_speech("정말 재미있는 놀이 시간이었어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("몸을 일으켜 앉아보자.")
        time.sleep(1)
        text_to_speech(f"{user_name}이는 무궁화 꽃이 피었습니다 놀이 전에도 해 본 적 있어? 파이보랑 같이 한 거랑 달랐어?")

        user_said = speech_to_text()

        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("그랬구나. 파이보가 기억해 둘게. ")
        break


    behavior_list.do_question_L()
    while True:
        text_to_speech("술래를 했을 때는 기분이 어땠어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그렇구나. 모두 재미있게 놀았으니 서로 악수하고 놀이를 마치도록 하자! 정말 멋있었어!")
        time.sleep(1)
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 놀이에서처럼 움직이지 않고 서봐!")        
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

Play_Flower("슬기")