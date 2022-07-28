#!/usr/bin/python3
# muscle: 대근육/소근육
# NLP.py에 self.Chance = ['5점', '10점', '찬스'] 추가

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


def Play_Tennis(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 풍선과 풍선을 칠 막대기가 필요해~")
        time.sleep(1)
        text_to_speech("막대기는 종류에 상관 없이 여러 개를 준비하면 좋아.")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘")
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
        text_to_speech("풍선으로 테니스 공을 만들고 테니스 치듯이 공을 주고 받아 볼거야.")
        time.sleep(1)
        text_to_speech("공이 상대방 땅에 떨어지면 내가 1점을 얻고, 내 땅에 떨어지면 상대가 1점을 얻어.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("어렵지 않지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 중간에 찬스를 써서 다른 테니스채로 바꿔 보거나, 상대방의 테니스채를 서로 바꿔서 쳐 볼거야.")
                break
        else:
            behavior_list.do_waiting_B()
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
        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("먼저 풍선을 불어서 꼭지를 묶어 공을 만들자.")
            time.sleep(1)
            text_to_speech("그 다음은 각자 테니스채를 골라.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("좋아! 이젠 풍선을 쳐서 상대방에게 보내보자~")
                    time.sleep(1)
                    text_to_speech("풍선이 내려오기 전에 막대기로 풍선을 다시 쳐 올려서, 상대방 땅에 떨어지도록 보내는 거야.")  
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("한쪽이 먼저 5점을 얻으면 ‘5점 찬스’ 라고 외쳐줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'CHANCE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("우와 정말 잘 하는걸? 이제 테니스채를 한번 바꿔보자.")
                    time.sleep(1)
                    text_to_speech("손에 움켜쥘 수 있는 도구를 가져와.")  
                    tiem.sleep(1)
                    text_to_speedh("신문지를 돌돌 말아 새로 만들어도 좋아.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('CHANCE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("좋았어! 한쪽이 먼저 10점을 얻으면 ‘10점 찬스’라고 외쳐줘. 준비~ 시작!")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
    
            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'CHANCE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("우와, 이번엔 서로 만든 테니스채를 상대방과 바꿔서 진행해보자!")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('CHANCE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("이제 마지막 5점이야. 15점을 먼저 얻는 사람이 승리 하는거야.")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("이긴 사람이 ‘내가 이겼어’라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech("정말 멋진 경기였어.")
                    time.sleep(1)
                    text_to_speech("두 사람 모두 최선을 다하는 모습이 멋졌어.")
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
        text_to_speech("이제 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("경기 하느라 테니스 치느라 팔에 힘을 많이 주었으니 양 손으로 꾹꾹 눌러볼거야.")
        time.sleep(1)
        text_to_speech("10초 동안 마사지 시작!")
        #time.sleep(10) 
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("팔이 편해졌지?")
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
                text_to_speech("정말 멋진 풍선 테니스였어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("어때? 마사지를 해주니까 팔 힘이 회복된 거 같아?")

        user_said = speech_to_text()

        break

    behavior_list.do_question_L()
    while True:
        text_to_speech("그렇구나. 오늘 놀이에서 어려운 게 있었어?")

        user_said = speech_to_text()
        break


    behavior_list.do_praise_L()
    while True:
        text_to_speech(f"{user_name}이는 팔 힘도 세고 테니스 경기도 열심히 잘 했어. 정말 자랑스러워~")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 튼튼 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 풍선을 들고 브이를 해봐!")        
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

Play_Balloon("슬기")