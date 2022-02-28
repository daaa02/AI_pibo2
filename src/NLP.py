import re

from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Okt
from pandas import DataFrame, Series
import pandas as pd


class Dictionary:
    def __init__(self):
        self.Yes = ['yes', '네', '예', '응', '어', '있어', '좋아', '그래', '맞아', '알았어', '알겠어', '당연', '됐어']

        self.No = ['no', '아니', '안', '별로', '글쎄', '싫어', '싫', '못 하', '못 하겠어', '못해', '없었어', '없어', '없네',
                   '없는', '몰라', '모르', '몰라', '그만']

        self.Done = ['done', '완료', '됐어', '했어', '하자', '할래', '왔어', '시작', '끝', '다 만들었어', '다 그렸어', '다 오렸어']

        self.Again = ['again', '다시', '또', '같은', '한 번 더', '한번 더', '계속']

        self.Animal = ['치타', '타조', '돌고래', '사슴', '호랑이', '고양이', '강아지', '수달', '코끼리', '토끼', '사자', '표범']
        
        self.Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        
        self.Number_word = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']


class NLP:
    def __init__(self):
        self.kk = Kkma()
        self.km = Komoran()
        self.okt = Okt()
        self.user_tag = []
        self.temp = {}
        self.n = 0

        
    def nlp_answer(self, user_said, dic):
        answer = ''
        for i in range(len(dic.Yes)):
            if dic.Yes[i] in user_said:
                answer = 'YES'
        for j in range(len(dic.No)):
            if dic.No[j] in user_said:
                answer = 'NO'
        for k in range(len(dic.Done)):
            if dic.Done[k] in user_said:
                answer = 'DONE'
        for n in range(len(dic.Again)):
            if dic.Again[n] in user_said:
                answer = 'AGAIN'
        return answer

    
    def nlp_animal(self, user_input, dic):
        """
        기존에는 '가, 랑, 을, 를, ( )' 을 split 했는데, 이러면 삭제되는 동물들이 있움 ex.호랑이
        그래서 공백, 가, 을, 를 제거하고 리스트화 ... 나중에 수정하기
        """
        a_list = re.split('[ 가을를]', user_input)  # ' ', 가, 랑, 을, 를 제거하고 리스트

        answer = [i for i in a_list if i in dic.animal]
        return answer[0]
    
    
    def nlp_number(self, user_said, dic):
        answer = -1
        ko = -1
        nb = -1
        for i, j in enumerate(dic.Number_word):
            x = user_said.find(j)
            if x != -1:
                ko = i
        for i, j in enumerate(dic.Number):
            x = user_said.find(j)
            if x != -1:
                nb = i
        answer = max(ko, nb)
        return answer
    
    
