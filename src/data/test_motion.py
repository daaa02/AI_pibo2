# motion test

# python module
import os
import sys
import time

# openpibo module
import openpibo
from openpibo.motion import Motion

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

motion = Motion()


def motion_test():
    print("***질문하기_Long***")
    motion.set_motion(name="m_question_L", cycle=1)

    print("***질문하기_Short***")
    motion.set_motion(name="m_question_S", cycle=1)

    print("***제안하기_Long***")
    motion.set_motion(name="m_suggestion_L", cycle=1)

    print("***제안하기_Short***")
    motion.set_motion(name="m_suggestion_S", cycle=1)

    print("***설명하기_type-A***")
    motion.set_motion(name="m_explain_A", cycle=1)

    print("***설명하기_type-B***")
    motion.set_motion(name="m_explain_B", cycle=1)

    print("***사진찍기***")
    motion.set_motion(name="m_photo", cycle=1)

    print("***스탬프찍기***")
    motion.set_motion(name="m_stamp", cycle=1)

    print("***기다리기_type-A***")
    motion.set_motion(name="m_waiting_A", cycle=1)

    print("***기다리기_type-B***")
    motion.set_motion(name="m_waiting_B", cycle=1)

    print("***기다리기_type-C***")
    motion.set_motion(name="m_waiting_C", cycle=1)

    print("***칭찬하기_Long***")
    motion.set_motion(name="m_praise_L", cycle=1)

    print("***칭찬하기_Short***")
    motion.set_motion(name="m_praise_S", cycle=1)

    print("***동의하기***")
    motion.set_motion(name="m_agree", cycle=1)

    print("***기쁨***")
    motion.set_motion(name="m_joy", cycle=1)

    print("***슬픔***")
    motion.set_motion(name="m_sad", cycle=1)


if __name__ == "__main__":
    motion_test()
