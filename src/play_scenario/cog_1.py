# cognition: 인지/지각/사고

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


def text_to_speech(string):
    filename = "tts.wav"
    print("\n" + string + "\n")
    tts.tts_connection(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{string}<break time='500ms'/></prosody></voice>\
                </speak>", filename)
    tts.play(filename, 'local', '0', False)


def Play_Tissue(user_name):

    print(f"user name: {user_name} \n")

    # 2.1 준비물 설명
    behavior_list.do_explain_A()
    while True:
        time.sleep(1)
        text_to_speech("놀이를 위해 휴지가 필요해~ 두루마리 휴지를 준비해줘.")
        text_to_speech("많으면 많을 수록 좋아. ")
        time.sleep(1)
        text_to_speech("준비가 되면 준비 됐다고 말해줘")
        break

    behavior_list.do_waiting_A()
    while True:
        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_joy()
            while True:
                time.sleep(1)
                text_to_speech("좋았어. 놀이 방법을 알려줄게!")
                break
        else:
            print("*** Yes 기다리는 중 ***")
            continue
        break

    # 2.2 놀이 설명
    behavior_list.do_explain_B()
    while True:
        text_to_speech("휴지를 풀어서 길을 만들어 볼 거야. 어렵지 않지?")
        break

    behavior_list.do_question_S()
    while True:
        time.sleep(1)
        text_to_speech("할 수 있으면 할 수 있다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'YES':
            behavior_list.do_explain_A()
            while True:
                text_to_speech("좋았어! 휴지 길은 미끄러울 수 있어서 뛰면 안돼. ")
                break
        else:
            print("*** Yes 기다리는 중 ***")
            continue
        break

    behavior_list.do_waiting_A()
    while True:
        text_to_speech("준비 됐으면 시작하자고 말해줘.")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                text_to_speech("그래, 시작하자!")
                break
        else:
            print("*** Done 기다리는 중 ***")
            continue
        break

    # 2.3 놀이 시작
    def start():
        behavior_list.do_suggestion_S()
        while True:
            time.sleep(1)
            text_to_speech("먼저 곳곳에 휴지 섬을 만들자. 휴지를 통째로 놓고 쌓아줘.")
            break

        behavior_list.do_explain_B()
        while True:
            time.sleep(1)
            text_to_speech("휴지를 통째로 놓고 쌓아줘.")
            break

        behavior_list.do_waiting_B()
        while True:
            text_to_speech("다 만들었으면 다 만들었다고 말해줘~")

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    time.sleep(2)
                    text_to_speech("정말 멋진 섬이 완성 되었는걸? 휴지로 만들어서 포근해 보여.")
                    break
            else:
                print("*** Done 기다리는 중 ***")
                continue
            break

        behavior_list.do_explain_A()
        while True:
            text_to_speech("좋았어! 이제 섬끼리 연결되는 휴지 길을 만들어보자.")
            text_to_speech("휴지를 풀어서 만들어줘.")
            break

        behavior_list.do_waiting_C()
        while True:
            text_to_speech("다 만들었으면 다 만들었다고 말해줘~")
            time.sleep(1)

            user_said = speech_to_text()
            answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

            if answer == 'DONE':
                behavior_list.do_praise_L()
                while True:
                    text_to_speech("정말 열심히 만들었는걸?")
                    text_to_speech("정말 휴지길로 걸어서 섬에 가 보고 싶어.")
                    time.sleep(5)
                    break
            else:
                print("*** Done 기다리는 중 ***")
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
                text_to_speech(f"열심히 따라해준 {user_name}이가 최고야~ 정말 신났어!")
                break
        break


    # 2.5 마무리 대화
    behavior_list.do_suggestion_L()
    while True:
        text_to_speech("이제 입으로 바람을 만들어서 휴지를 날려보자.")
        time.sleep(5)

        text_to_speech("길이었던 휴지를 찢어서 휴지 섬에 눈을 내려보자.")
        text_to_speech("끝났으면 끝났다고 말해줘~")

        user_said = speech_to_text()
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            behavior_list.do_joy()
            while True:
                text_to_speech("휴지 눈이 내리니까 정말 포근하다~")
                time.sleep(1)
                break
        else:
            print("*** Done 기다리는 중 ***")
            continue
        break

    behavior_list.do_question_L()
    while True:
        time.sleep(1)
        text_to_speech(f"{user_name}이는 언제 포근함을 느껴?")

        user_said = speech_to_text()

        text_to_speech("정말? 왜 포근해?")

        user_said = speech_to_text()
        break

    behavior_list.do_joy()
    while True:
        text_to_speech(f"생각만 해도 기분이 좋아. ")
        break

    # 2.6 놀이 기록
    behavior_list.do_stamp()
    while True:
        text_to_speech(f"{user_name}이가 열심히 놀이를 했으니, 오늘은 똑똑 스탬프를 찍어줄게.")
        break

    behavior_list.do_suggestion_S()
    while True:
        text_to_speech("사진을 찍어 줄게. 휴지섬 앞에 서서 포즈를 취해봐!")
        break

    behavior_list.do_photo()

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
