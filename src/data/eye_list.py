# python module
import time

# openpibo module
from openpibo.device import Device

"""
NEOPIXEL(20) -> ex) #20:255,255,255:!

# 20: 색 변경
# 21: 속도 d(ms)만큼 천천히 변경
# 22: 밝기 조절(기본 64)
# 25: 무지개 눈, d(ms)의 속도로 색 변화

"""

device = Device()


def e_question():
    device.send_cmd(21, '108,209,239,10')


def e_suggestion():
    device.send_cmd(21, '108,209,239,10')


def e_explain():
    device.send_cmd(21, '108,209,239,10')


def e_photo():
    device.send_cmd(20, '120,230,208')


def e_stamp():
    device.send_cmd(25, '20')


def e_waiting():
    device.send_cmd(21, '108,209,239,20')


def e_praise():
    device.send_cmd(25, '20')


def e_agree():
    device.send_cmd(21, '108,209,239,20')


def e_joy():
    device.send_cmd(25, '10')


def e_sad():
    device.send_cmd(21, '186,147,223,50')
