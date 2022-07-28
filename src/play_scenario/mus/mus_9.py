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


def Play_Star(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 풍선과 가벼운 천이 필요해~")
        time.sleep(1)
        text_to_speech("스카프나 보자기를 준비하면 좋아.")
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
        text_to_speech("풍선 매듭에 천을 묶고 풍선을 던져볼 거야.")
        time.sleep(1)
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
                text_to_speech("좋았어! 밤하늘을 가로지르는 별똥별처럼 보일거야~")
                time.sleep(1)
                text_to_speech("풍선을 최대한 높이 던져보고, 벽이나 천장에 던져보기도 하자.")
                break
        else:
            behavior_list.do_waiting_B()
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
        behavior_list.do_suggestion_L()
        while True:
            text_to_speech("풍선을 불어서 묶어보자.")
            time.sleep(1)
            text_to_speech("풍선에 꼭지에 천을 묶으면 별똥별 완성이야.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("우와 정말 빠른걸? 이번엔 친구랑 같이 별똥별을 주고 받아보자.")
                    time.sleep(1)
                    text_to_speech("혼자 던질 때랑 별똥별 모양이 어떻게 다른지 관찰해봐.")    # 둘, 셋 하면 너무 빠르게 느껴짐
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘~")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("좋았어! 내가 노래 한 곡을 틀어줄게.")
                    time.sleep(1)
                    text_to_speech("노래가 끝날 때까지 풍선을 주고 받는 거야. 준비~ 시작!")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        #1분간 노래 재생

        behavior_list.do_praise_S()
        while True:
            text_to_speech("우와, 정말 하늘에서 별이 막 떨어지는 것 같았어!")
            break

    start()

    # 2.4 놀이 완료
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("풍선을 따라 열심히 움직인 다리와 눈을 쉬게 하자!")
        time.sleep(1)
        text_to_speech("손끝으로 다리와 눈 주위를 꾹꾹 눌러줘.")
        time.sleep(1)
        text_to_speech("10초 동안 마사지 시작!")
        #time.sleep(10) 
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("다리와 눈이 편해졌지?")
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
                text_to_speech("정말 멋진 별똥별 놀이였어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("어때? 별똥별을 만들고 날려보니 기분이 어땠어?")

        user_said = speech_to_text()

        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나. 파이보는 별똥별을 본 적이 없지만 꼭 한번 보고 싶어.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"별똥별을 보면 소원이 이루어진대. {user_name}이는 소원이 있어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech("그 소원 꼭 이뤄지면 좋겠다. 파이보도 같이 빌어줄게!")
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
        text_to_speech("사진을 찍어 줄게. 별똥별을 들고 브이를 해봐!")        
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

Play_Star("슬기")