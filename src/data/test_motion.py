# motion test

# python module
import os
import sys
import time

# openpibo module
import openpibo
from openpibo.oled import Oled
from openpibo.motion import Motion

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

oled = Oled()
motion = Motion()


def motion_test():
    """
    <현재 사용 방법>
    /usr/local/lib/python3.7/.../openpibo/motion.py 에서
    사용할 모션 파일 경로를 /home/pi/AI_pibo2/data/motion_db.json 로 지정하고
    set_motion(name="", cycle=n) 함수 사용해서 모션 실행

    <다른 방법>
    (example.json 이라는 새로운 모션 파일을 만든다는 가정 하에)
    motion.set_motion("<name>", path="/path/to/example.json") 으로
    라이브러리에 설정된 경로 말고 내 임의의 경로에서 모션 파일 실행 및 동작 가능할 듯
    """

    oled.set_font(size=20)
    oled.draw_text((10, 10), "질문하기_L")
    oled.show()
    motion.set_motion(name="m_question_L", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "질문하기_S")
    oled.show()
    motion.set_motion(name="m_question_S", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "제안하기_L")
    oled.show()
    motion.set_motion(name="m_suggestion_L", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "제안하기_S")
    oled.show()
    motion.set_motion(name="m_suggestion_S", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "설명하기_A")
    oled.show()
    motion.set_motion(name="m_explain_A", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "설명하기_B")
    oled.show()
    motion.set_motion(name="m_explain_B", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "사진찍기")
    oled.show()
    motion.set_motion(name="m_photo", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "스탬프찍기")
    oled.show()
    motion.set_motion(name="m_stamp", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "기다리기_A")
    oled.show()
    motion.set_motion(name="m_waiting_A", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "기다리기_B")
    oled.show()
    motion.set_motion(name="m_waiting_B", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "기다리기_C")
    oled.show()
    motion.set_motion(name="m_waiting_C", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "칭찬하기_L")
    oled.show()
    motion.set_motion(name="m_praise_L", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "칭찬하기_S")
    oled.show()
    motion.set_motion(name="m_praise_S", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "동의하기")
    oled.show()
    motion.set_motion(name="m_agree", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "기쁨")
    oled.show()
    motion.set_motion(name="m_joy", cycle=1)
    oled.clear()

    oled.set_font(size=20)
    oled.draw_text((10, 10), "슬픔")
    oled.show()
    motion.set_motion(name="m_sad", cycle=1)
    oled.clear()


if __name__ == "__main__":
    motion_test()
