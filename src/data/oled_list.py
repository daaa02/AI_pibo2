#!/usr/bin/python3

# openpibo module
import openpibo
from openpibo.oled import Oled

o = Oled()

# draw_image 하고 바로 show 해야 안 사라짐

def run():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_물음표1.png")
    o.show()


def o_question():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_물음표1.png")
    o.show()


def o_suggestion():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_물음표1.png")    # 물음표2.png size error
    o.show()


def o_explain():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_현재단계1.png")
    o.show()


def o_photo():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_카메라.png")
    o.show()


def o_stamp():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_스탬프1.png")
    o.show()


def o_waiting():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_시계.png")
    o.show()


def o_cheer():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_음표1.png")
    o.show()


def o_compliment():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_엄지1.png")
    o.show()


def o_concil():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")    # default2.png size error
    o.show()


def o_search():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_감지1.png")
    o.show()


def o_sleep():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_잠자기1.png")
    o.show()


def o_wakeup():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_날씨.png")
    o.show()


def o_agree():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_긍정.png")
    o.show()


def o_deny():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_부정.png")
    o.show()


def o_joy():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")
    o.show()


def o_angry():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")    # default2.png size error
    o.show()


def o_sad():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")    # default2.png size error
    o.show()


def o_tired():
    o.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_배터리1.png")
    o.show()
