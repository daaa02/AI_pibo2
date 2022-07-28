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


def Play_Spider(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("이번 놀이는 거미줄을 만들 털실이 필요해~")
        time.sleep(1)
        text_to_speech("털실이 없으면 끈으로 해도 좋아.")
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
        text_to_speech("털실을 길게 풀어서 거미줄을 만들거야~")
        time.sleep(1)
        text_to_speech("식탁이나 책상 밑에 들어가서 다리 사이에 줄을 걸치는 거야.")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("그 다음엔 거미줄에 닿지 않게 조심하면서 거미줄 사이를 지나가 볼 거야")
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
        behavior_list.do_explain_A()
        while True:
            text_to_speech("거미줄을 칠 식탁이나 책상을 찾아서 파이보를 그 옆으로 옮겨줘.")
            time.sleep(1)
            text_to_speech("다음은 다리마다 털실을 걸고, 중간 중간에 털실을 묶어 매듭을 지어.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("준비 됐으면 준비 됐다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("다 했으면 다 했어 라고 말해줘.")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_explain_B()
        while True:
            text_to_speech(f"이제 {user_name}이가 들어가서 너무 좁은 곳은 없는지 살펴봐 줘")
            time.sleep(1)
            text_to_speech("줄을 추가하거나, 줄을 당겨 모양을 바꿔도 좋아.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 했으면 다 했어 라고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("꼼꼼하게 잘 했어! 이번엔  거미줄 사이를 지나서 통과해 보자.")
                    time.sleep(1)
                    break
            else:
                behavior_list.do_waiting_B()
                wait_for('DONE')
                continue
            break

        behavior_list.do_question_S()
        while True:
            time.sleep(1)
            text_to_speech(f"{user_name}이는 어떤 거미로 변신하고 싶어?")

            user_said = speech_to_text()

            break

        behavior_list.do_suggestion_S()
        while True:
            text_to_speech("그렇구니~ 정말 기대된다. 그럼 시작해보자!")
            time.sleep(1)
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 통과했으면 다 통과했다고 말해줘.")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_suggestion_L()
                while True:
                    text_to_speech("조심조심 집중해서 통과하는 모습이 정말 멋있었어.")
                    time.sleep(1)
                    text_to_speech(f"{user_name}이는 뭐든 잘 할 수 있는 아이 같아!")
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
        text_to_speech("열심히 놀이했으니 잠시 누워서 휴식 하자!")
        time.sleep(1)
        text_to_speech("1분 동안 휴식 시작!")
        #time.sleep(10) 
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
                text_to_speech("정말 재미있는 거미줄 놀이였어.")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        time.sleep(1)
        text_to_speech("누웠던 자리에서 천천히 몸을 일으켜 보자.")
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech(f"오늘 {user_name}이는 거미줄을 몇 번 통과 했어?")

        user_said = speech_to_text()
        break

    behavior_list.do_question_L()
    while True:
        text_to_speech(f"그렇구나 파이보는 {user_name}가 어려운 것도 척척 해내는 모습이 보기 좋았어.")

        user_said = speech_to_text()
        break

    behavior_list.do_question_S()
    while True:
        text_to_speech("그렇구나. 거미줄을 통과할 때 어렵진 않았어?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"그랬구나. 파이보는 {user_name}이가 어려운 것도 척척 해내는 모습이 보기 좋았어.")
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
        text_to_speech("사진을 찍어 줄게. 거미줄 앞에 멋지게 서서 브이를 해봐!")        
        break

    behavior_list.do_photo()
    time.sleep(5)
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3", out='local', volume=-1000, background=False)

    # 2.7 다음 놀이 제안
    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech("또 다른 놀이 할까? 거미줄 앞에 멋지게 서서 브이를 해봐!")

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

Play_Spider("슬기")