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


def Play_Toe(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 훌라후프, 휴지나 신문지, 줄이 필요해~")
        time.sleep(1)
        text_to_speech("줄 대신 스카프나 천을 가져와도 좋아.")
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
        text_to_speech("발가락 사이에 휴지나 신문지를 끼워서 옮기고 둘이서 발가락 씨름을 할 거야.")
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
                text_to_speech("좋았어! 손가락 대신에 발가락을 이용하여 물건을 집는다고 생각하면 돼.")
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
        behavior_list.do_explain_B()
        while True:
            text_to_speech("바닥에 훌라후프를 놓고 훌라후프 바깥쪽에 휴지와 신문지 조각을 떨어트려줘.")
            time.sleep(1)
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    text_to_speech("잘했어! 이젠 발가락으로 휴지를 집어 올려서 훌라후프 안에 넣어봐~")
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
                behavior_list.do_explain_A()
                while True:
                    text_to_speech("우와 정말 빠른걸? 이번엔 발가락 씨름을 해보자.")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("두 명이 짝을 이루어 발가락 사이에 줄을 끼우고 서로 당기는 거야.")
            time.sleep(1)
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("당길 준비가 됐으면 준비 됐어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_explain_A()
                while True:
                    text_to_speech("좋았어! 내가 시작이라고 말하면 줄을 당기는 거야.")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_explain_B()
        while True:
            text_to_speech("이긴 사람은 이겼다 라고 말해줘.")
            time.sleep(5)
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("둘 다 이겼으면 둘 다 이겼다 라고 말해줘. 준비~ 시작!")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_joy()
                while True:
                    text_to_speech("우와, 두 사람 다 막상막하였어!")
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
        text_to_speech("이제 자리에 앉아보자.")   
        time.sleep(1)
        text_to_speech("발가락 힘을 많이 사용했으니 발가락도 쉬게 하자!") 
        break

    behavior_list.do_explain_A()
    while True:
        text_to_speech("손가락으로 하나씩 발가락을 누르는거야.") 
        time.sleep(1)
        text_to_speech("준비 됐으면 준비 됐어 라고 말해줘.")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_suggestion_L()
            while True:
                time.sleep(1)
                text_to_speech("좋아. 시작! 10초 간 열심히 마사지 해보자.")
                #time.sleep(10)
                text_to_speech("정말 편안하겠다.")
                break
        else:
            behavior_list.do_waiting_A()
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
                text_to_speech("정말 멋진 발가락 놀이였어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("어때? 발가락도 쉬게 해주니까 발가락 힘이 회복된 거 같아?")

        user_said = speech_to_text()

        break

    behavior_list.do_praise_S()
    while True:
        text_to_speech("오늘 놀이에서 어려운 게 있었어?")
        break

    behavior_list.do_sad()
    while True:
        text_to_speech("그렇구나. 파이보는 처음에 발가락이 잘 움직여서 어려웠어.")
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 뭐가 가장 기억에 남아?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"알려줘서 고마워. {user_name}이가 오늘 재밌게 노는 모습이 보기 좋았어~")
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
        text_to_speech("사진을 찍어 줄게. 발가락을 멋지게 들고 브이를 해봐!")        
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

Play_Toe("슬기")