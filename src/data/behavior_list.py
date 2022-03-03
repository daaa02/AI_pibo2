# behavior = motion + eye + oled + sound

# python module
import os
import sys
import time
import json
from threading import Thread

# openpibo module
import openpibo
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.oled import Oled

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import eye_list
import src.data.oled_list as oled_list
from text_to_speech import TextToSpeech

motion = Motion()
audio = TextToSpeech()

# 스탬프 찍기, 사진 찍기는 말 하고 나서 효과음 재생

def do_question_L():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_question(), args=())
    m = Thread(target=motion.set_motion, args=("m_question_L", 1))
    o = Thread(target=oled_list.o_question(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_question_S():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_question(), args=())
    m = Thread(target=motion.set_motion, args=("m_question_S", 1))
    o = Thread(target=oled_list.o_question(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_suggestion_L():
    # e = Thread(target=eye_list.e_suggestion(), args=())
    m = Thread(target=motion.set_motion, args=("m_suggestion_L", 1))
    o = Thread(target=oled_list.o_suggestion, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_suggestion_S():
    # e = Thread(target=eye_list.e_suggestion(), args=())
    m = Thread(target=motion.set_motion, args=("m_suggestion_S", 1))
    o = Thread(target=oled_list.o_suggestion, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_explain_A():
    # e = Thread(target=eye_list.e_explain(), args=())
    m = Thread(target=motion.set_motion, args=("m_explain_A", 3))
    o = Thread(target=oled_list.o_explain, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_explain_B():
    # e = Thread(target=eye_list.e_explain(), args=())
    m = Thread(target=motion.set_motion, args=("m_explain_B", 3))
    o = Thread(target=oled_list.o_explain, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_photo():
    # e = Thread(target=eye_list.e_photo(), args=())
    m = Thread(target=motion.set_motion, args=("m_photo", 1))
    o = Thread(target=oled_list.o_photo, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_stamp():
    # e = Thread(target=eye_list.e_stamp(), args=())
    m = Thread(target=motion.set_motion, args=("m_stamp", 1))
    o = Thread(target=oled_list.o_stamp, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_waiting_A():
    # e = Thread(target=eye_list.e_waiting(), args=())
    m = Thread(target=motion.set_motion, args=("m_waiting_A", 2))
    o = Thread(target=oled_list.o_waiting(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_waiting_B():
    # e = Thread(target=eye_list.e_waiting(), args=())
    m = Thread(target=motion.set_motion, args=("m_waiting_B", 2))
    o = Thread(target=oled_list.o_waiting(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_waiting_C():
    # e = Thread(target=eye_list.e_waiting(), args=())
    m = Thread(target=motion.set_motion, args=("m_waiting_C", 2))
    o = Thread(target=oled_list.o_waiting(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_praise_L():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_compliment(), args=())
    m = Thread(target=motion.set_motion, args=("m_praise_L", 1))
    o = Thread(target=oled_list.o_compliment, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_praise_S():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_compliment(), args=())
    m = Thread(target=motion.set_motion, args=("m_praise_S", 1))
    o = Thread(target=oled_list.o_compliment, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_agree():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/딩동댕3.mp3", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_agree(), args=())
    m = Thread(target=motion.set_motion, args=("m_agree", 1))
    o = Thread(target=oled_list.o_agree(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_joy():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/기분좋음.mp3", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_joy(), args=())
    m = Thread(target=motion.set_motion, args=("m_joy", 1))
    o = Thread(target=oled_list.o_joy(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_sad():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/슬픈소리.wav", out='local', volume=-1000, background=False)
    # e = Thread(target=eye_list.e_sad(), args=())
    m = Thread(target=motion.set_motion, args=("m_sad", 1))
    o = Thread(target=oled_list.o_sad(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()

