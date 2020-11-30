from settings import GAZETTEER_VOCAB, GAZETTEER_LABEL
from konlpy.tag import mecab
import numpy as np

class PosTagFeature:
    
    def __init__(self, ):
        pass
    
                    
    def transform_end2end(self, line, max_length, ngram=4):
        '''
        음절로 띄어쓰기 된 End2End 데이터 셋
        문장을 가젯 특성으로 변환
        입력: 음절로 띄어쓰기 된 문장 스트링
        출력: (시퀀스 최대 길이, 태그 레이블 수)
        '''
        sentence = line.split()
        if len(sentence) <= max_length:
            sentence += ['<UNK>'] * (max_length - len(sentence))
        else:
            sentence = sentence[:max_length]
        feature = self.transfrom_charaterized_line(sentence, ngram)
        return feature