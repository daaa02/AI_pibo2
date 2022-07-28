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
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def Play_Hoop(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 훌라후프, 종이와 그림도구, 가위가 필요해~")
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
        text_to_speech("종이에 동물을 그리고 오린 다음에, 입으로 바람을 불어서 훌라후프 안에 넣을거야.")
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
                text_to_speech("입으로 바람을 불기 힘들면 도구를 사용해서 바람을 일으켜도 좋아")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 되면 준비 됐다고 말해줘")

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
        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech(f"{user_name} 이가 좋아하는 동물 카드를 보여줘")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("카드가 없으면 동물 이름을 말해도 좋아")

            user_said = speech_to_text()
            animal = NLP.nlp_animal(user_said=user_said, dic=Dic)
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech(f"그럼 {animal}를 종이에 그려보자!")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 그렸으면 다 그렸다고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    time.sleep(2)
                    text_to_speech(f"우와 정말 귀여운 {animal}이다. 다른 동물들도 더 그려보자.")
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_A()
        while True:
            text_to_speech("시간을 5분 줄게 자유롭게 그려봐. 다 그렸으면 다 그렸다고 말해줘.")            
            # print("300sec ...")
            # time.sleep(300)     # 진짜진짜진짜 5분임

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_S()
                while True:
                    text_to_speech("좋아. 이번에는 그림 모양대로 종이를 오리자")
                    time.sleep(5)
                    break
            else:
                behavior_list.do_waiting_A()
                wait_for('DONE')
                continue
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 오렸으면 다 오렸다고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("그럼 이제 훌라후프를 바닥에 놓고 주변에 동물그림을 뿌려놓자.")
                    time.sleep(1)
                    text_to_speech("내가 시~작! 하면 입으로 바람을 불어서 동물들을 훌라후프 안에 날려 넣는거야.")
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        text_to_speech("준비~~~~~ 시작!")
        behavior_list.do_joy()
        while True:
            text_to_speech("후우우우~~~~")     # 효과음 넣기!!!!! ;마땅한 거 못 찾음
            time.sleep(7)
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech("동물들을 모두 날려 넣었어?")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 했으면 다 했다고 말해줘")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech("우와~ 우리만의 동물원이 완성된 것 같아. 멋지다~!")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_C()
                wait_for('DONE')
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
                start()
            else:
                behavior_list.do_praise_L()
                while True:
                    text_to_speech("오늘 다양한 동물그림을 정말 열심히 만들었어! 자랑스러워")
                    break
            break

    start()

    # 2.5 마무리 대화
    behavior_list.do_question_L()
    while True:
        text_to_speech(f"{user_name}이는 오늘 만든 동물 중에 어떤 동물 그림이 제일 마음에 들었어?")

        user_said = speech_to_text()
        answer = NLP.nlp_animal(user_said=user_said, dic=Dic)

        break

    behavior_list.do_agree()
    while True:
        text_to_speech("그랬구나. 파이보도 참 잘 그렸다고 생각했어")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 키워보고 싶은 동물이 있어?")

        user_said = speech_to_text()

        text_to_speech("왜 키우고 싶어?")

        user_said = speech_to_text()
        break

    behavior_list.do_agree()
    while True:
        text_to_speech(f"그렇구나. {user_name}이는 동물을 정말 정성껏 잘 돌봐줄 것 같아")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("사진을 찍어 줄게. 가장 마음에 드는 동물 그림을 들고 브이해봐!")
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
