# python module
import re
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Okt
from pandas import DataFrame, Series
import pandas as pd


class Dictionary:
    def __init__(self):
        self.Yes = ['yes', '네', '예', '응', '어', '있어', '좋아', '좋은', '좋다', '그래', '맞아', '알았어', '알겠어', '당연', '됐어']

        self.No = ['no', '아니', '안', '별로', '글쎄', '싫어', '싫', '못 하', '못 하겠어', '못해', '없었어', '없어', '없네',
                   '없는', '몰라', '모르', '몰라', '그만']

        self.Done = ['done', '완료', '됐어', '했어', '하자', '할래', '왔어', '렸어', '시작', '끝', '다 만들었어', '다 그렸어', '다 오렸어', '다 올렸어', '성공']

        self.Again = ['again', '다시', '또', '같은', '한 번 더', '한번 더', '계속']

        self.Animal = ['치타', '타조', '돌고래', '사슴', '호랑이', '고양이', '강아지', '수달', '코끼리', '토끼', '사자', '표범', 
                       '기린', '앵무새', '새', '공룡', '곰', '원숭이', '달팽이', '개미', '닭', '돼지', '소', '고슴도치', '개', '물고기', '다람쥐']
        
        self.Fruit = ['사과', '딸기', '복숭아', '포도', '귤', '오렌지', '감', '파인애플', '자두', '청포도', '바나나', '망고', '수박',
                        '배','참외', '앵두', '']

        self.One = ['1', '일', '첫']

        self.Two = ['2', '이', '두']

        self.Three = ['3', '삼', '세']

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
        """
        사용자가 발화한 내용에 포함되는 단어가 있다면 return answer '_'
        ex. input: 좋은 것 같아 ==> Yes=[..'좋은'..] ==> answer: YES
        """
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
        print(answer)
        return answer


    def nlp_animal(self, user_said, dic):
        """
        공백, 가, 을, 를 split 해서 리스트화
        ex. input: 나는 호랑이가 좋아! ==> animal: 호랑이   ... 나중에 수정하기
        => 이 부분에 komoran noun 적용하면 될 거 같음 (추후 수정!)
        """
        a_list = re.split('[ 가을를]', user_said)  

        animal = [i for i in a_list if i in dic.Animal]
        return animal[0]

    def nlp_fruit(self, user_said, dic):

        a_list = re.split('[ 가을를]', user_said)
        fruit = [i for i in a_list if i in dic.Fruit]
        return fruit[0]


    def nlp_name(self, user_said):
        """
        공백, 이, 가 split 해서 한 단어씩 리스트화
        ex. input: 두준이가 왕이 됐어! ==> name: 두준   ... 나중에 수정하기 2
        """
        a_list = re.split('[ 이가]', user_said)  
        name = a_list[0]
        return name


    def nlp_number(self, user_said, dic):
        answer = ''
        for i in range(len(dic.One)):
            if dic.One[i] in user_said:
                answer = '1'
        for j in range(len(dic.Two)):
            if dic.Two[j] in user_said:
                answer = '2'
        for k in range(len(dic.Three)):
            if dic.Three[k] in user_said:
                answer = '3'
        print(answer)
        return answer

    
    # def nlp_number(self, user_said, dic):
    #     answer = -1
    #     ko = -1
    #     nb = -1
    #     for i, j in enumerate(dic.Number):
    #         x = user_said.find(j)
    #         if x != -1:
    #             ko = i
    #     for i, j in enumerate(dic.Number_Word):
    #         x = user_said.find(j)
    #         if x != -1:
    #             nb = i
    #     answer = max(ko, nb)
    #     return answer

    def nlp_number(self, user_said, dic):
        number = -1
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
        number = max(ko, nb)
        return number
    
