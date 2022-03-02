import time

import openpibo
from openpibo.oled import Oled

o = Oled()

# draw_image 하고 show 해야 바로 안 사라짐


def o_question():
    o.draw_image("/icon/화면_물음표1.png")
    o.show()


def o_suggestion():
    o.draw_image("/icon/화면_물음표1.png")    # 물음표2.png size error
    o.show()


def o_explain():
    o.draw_image("/icon/화면_현재단계1.png")
    o.show()


def o_photo():
    o.draw_image("/icon/화면_카메라.png")
    o.show()


def o_stamp():
    o.draw_image("/icon/화면_스탬프1.png")
    o.show()


def o_waiting():
    o.draw_image("/icon/화면_시계.png")
    o.show()

    
def o_praise():
    o.draw_image("/icon/화면_엄지1.png")
    o.show()


def o_agree():
    o.draw_image("/icon/화면_긍정.png")
    o.show()


def o_joy():
    o.draw_image("/icon/화면_default1.png")
    o.show()


def o_sad():
    o.draw_image("/icon/화면_default1.png")    # default2.png size error
    o.show()

