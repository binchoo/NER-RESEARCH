from settings import POS_LABEL
import numpy as np

class PosTagFeature:
    
    def __init__(self):
        self.label2idx = self.load_label(POS_LABEL)
    
    def set_tagger(self, tagger):
        self.tagger = tagger
        
    def load_label(self, label_file):
        with open(label_file, 'r', encoding='utf8') as f:
            label2idx = {nertag.strip():idx for idx, nertag in enumerate(f.readlines())}
        return label2idx
                    
    def transform_end2end(self, line, max_length, hot_label=True):
        '''
        음절로 띄어쓰기 된 End2End 데이터 셋
        문장을 가젯 특성으로 변환
        입력: 음절로 띄어쓰기 된 문장 스트링
        출력: (시퀀스 최대 길이, 태그 레이블 수)
        '''
        sentence = line.replace('<SP>', ' ')[:max_length]
        hot = []
        for word, pos in self.tagger.pos(sentence):
            pos_index = self.label2idx.get(pos, self.label2idx['UNK'])
            for char in word:
                hot.append(pos_index)
        
        if len(hot) > max_length:
            hot = hot[:max_length]
        
        if hot_label:
            feature = np.zeros((max_length, len(self.label2idx)))
            feature[np.arange(max_length)[:len(hot)], hot] = 1
            return feature
        else:
            feature = np.zeros(max_length)
            feature[: len(hot)] = np.array(hot)
        return feature
        
        