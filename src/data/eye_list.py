#!/usr/bin/python3

# python module
import time

# openpibo module
from openpibo.device import Device

"""
눈 색 변화 기본: eye_on(R,G,B)
ex. device.eye_on(255,255,255)

눈 색 변화 옵션: send_raw('#21:R,G,B,<ms>')
21: 속도 d(ms)만큼 천천히 변경
22: 밝기 조절(기본 64)
"""

device = Device()


def e_question():
    device.eye_on(108,209,239)


def e_suggestion():
    device.eye_on(108,209,239)


def e_explain():
    device.eye_on(108,209,239)


def e_photo():
    device.eye_on(153,255,51)


def e_stamp():
    device.eye_on(255,51,255)


def e_waiting():
    device.eye_on(108,209,239)


def e_compliment():
    device.send_raw('#21:255,180,232,5')
    time.sleep(0.5)
    device.send_raw('#21:120,230,208,5')
    time.sleep(0.1)
    device.send_raw('#21:251,245,155,5')


def e_agree():
    device.eye_on(108,209,239)


def e_joy():
    device.send_raw('#21:255,180,232,5')
    time.sleep(0.5)
    device.send_raw('#21:120,230,208,5')
    time.sleep(0.1)
    device.send_raw('#21:251,245,155,5')


def e_sad():
    device.eye_on(152,66,186)

