#!/usr/bin/python3
# communication: 의사소통/언어표현

# python module
import os
import sys
import time
import random
import string

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


def Play_Magic(user_name):

    print(f"user name: {user_name} \n")
    #마술에 걸린 동물들
    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 마법지팡이로 쓸 막대기가 필요해 ~")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐어 라고 말해줘~")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = input("답변 : ")
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
        text_to_speech(f"파이보가 먼저 마법사 역할을 할게.{user_name}이가 동물을 진짜 같이 재미있게 표현해줘.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있으면 할 수 있어 라고 말해줘~")

        user_said = input("답변 : ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_B()
            while True:
                text_to_speech("마법사가 ‘그대로 멈춰라’라고 말하면 제자리에서 멈춰야 돼.마법사 역할은 한 번씩 돌아가면서 해보자.")
                break
        else:
            behavior_list.do_waiting_A()
            wait_for('YES')
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비가 됐으면 시작하자고 말해줘~")

        user_said = input("답변 : ")
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
        global i
        i=1;
        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech(f"{user_name}이가 좋아하는 동물카드를 보여줘.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("카드가 없으면 동물 이름을 말해도 좋아")

            user_said = input("답변 : ")
            animal = NLP.nlp_animal(user_said=user_said, dic=Dic)
            break

        behavior_list.do_joy()
        while True:
            text_to_speech(f"좋았어! {animal}으로 변해라 얍!")
            #행동인식 - 사진 및 영상 촬영
            break

        behavior_list.do_joy()
        while True:
            time.sleep(5)
            text_to_speech("정말 실감나는 걸? 또 주문을 걸게. 그대로 멈춰라 얍! ")
            break
        
        Animal=Dic.Animal
        for j in range(0,26):
            Animals=random.randint(0,26)
            Animal.append(Animals)
        print(Animal[0])
        
        

        behavior_list.do_joy()
        while True:
            time.sleep(5)
            text_to_speech(f"이제 마법이 풀렸어. 이번에는 {(Animal[0])}로 변해라 얍!")
            #행동인식 - 사진 및 영상 촬영
            break

        behavior_list.do_question_S()
        while True:
            time.sleep(5)
            text_to_speech(f"지금 {(Animal[0])}는 뭘 하고 있어?")
            user_said == input("답변 : ")
            break

        behavior_list.do_praise_S()
        while True:
            text_to_speech(f"그렇구나. {user_name}이는 표현을 정말 잘하는 것 같아.")
            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("이번에는 역할을 바꿔 보자.")
            break

        behavior_list.do_explain_B()
        while True:
            text_to_speech("파이보에게 주문을 걸어줘~ “변해라 얍”이라고 말하고, 동물 카드를 보여줘.")
            text_to_speech("카드가 없으면 이름을 말해도 좋아. 지금부터 세 번 변신해볼게! 시작!")
            user_said = input("답변 : ")
            animal = NLP.nlp_animal(user_said=user_said, dic=Dic)
            break
        def start_1():
            global i
            if 1<=i<=3:
                behavior_list.do_joy()#동물 흉내 세번 반복 do_animal -> do_joy로 테스트
                while True:
                    text_to_speech(f"{animal} 흉내")
                    i=i+1
                    return start_1()

            elif i==4:
                behavior_list.do_joy()
                while True:
                    text_to_speech("너무 재미있다!정말 주문을 잘 걸었어!")
                    break

                # 2.4 놀이 완료
                behavior_list.do_question_S()
                while True:
                    text_to_speech("한 번 더 해볼까? 또 하고 싶으면 또 하자라고 말해줘.")

                    user_said = input("답변 : ")
                    answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

                    if answer == 'AGAIN':
                        behavior_list.do_agree()
                        start()
                    else:
                        behavior_list.do_praise_L()
                        while True:
                            text_to_speech(f"{user_name}이가 오늘 동물 표현을 정말 실감나게 잘 했어~ 진짜 동물이 나타난 줄 알고 깜짝 놀랐어!")
                            break
                    break
        start_1()

        # 2.5 마무리 대화
        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("이제 잠시 자리에 앉아 쉬어보자. ")
            time.sleep(3)
            text_to_speech(f"{user_name}이가 좋아하는 {animal}는 어떻게 자? 잠자는 모습을 표현해 보자~")
            break

        behavior_list.do_agree()#피곤?
        while True:
            text_to_speech("파이보도 잠이 올 것만 같아.")
            break

        behavior_list.do_question_S()
        while True:
            text_to_speech(f"{user_name}이는 {animal}가 왜 좋아?")
            user_said = input("답변 : ")
            break

        behavior_list.do_agree()
        while True:
            text_to_speech("그렇구나. 파이보가 기억해 둘게. ")
            break

        # 2.6 놀이 기록
        behavior_list.do_stamp()
        while True:
            text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄게.")
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
            break

        behavior_list.do_suggestion_L()
        while True:
            text_to_speech(f"사진을 찍어 줄게.{animal}처럼 포즈를 취해봐!")
            break

        behavior_list.do_photo()
        time.sleep(5)
        tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3", out='local', volume=-1000, background=False)

        # 2.7 다음 놀이 제안
        behavior_list.do_question_L()
        while True:
            time.sleep(1)
            text_to_speech("또 다른 놀이 할까? 파이보랑 또 놀고 싶으면 놀고 싶다고 말해줘!")

            user_said = input("답변 : ")
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
        
    start()