#!/usr/bin/python3

# python module
import os
import sys

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

# 여기랑 메인문 바꿔야 해
# from src.play_scenario.<폴더명>.<파일명> import <해당 파일의 함수명>
from src.play_scenario.com.com_1 import Play_Hoop

if __name__ == "__main__":
  user_name = ("이름 입력: ")
  # <해당 파일의 함수명>(user_name)
  Play_Hoop(user_name)

  
