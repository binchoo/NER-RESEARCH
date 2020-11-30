from settings import GAZETTEER_VOCAB, GAZETTEER_LABEL
import numpy as np

class GazetteFeature:
    
    def __init__(self):
        self.label2idx = self.load_label(GAZETTEER_LABEL)
        self.vocab = self.load_vocab(GAZETTEER_VOCAB)
    
    def load_label(self, label_file):
        with open(label_file, 'r', encoding='utf8') as f:
            label2idx = {nertag.strip():idx for idx, nertag in enumerate(f.readlines())}
        return label2idx
    
    def load_vocab(self, vocab_file):
        vocab = {}
        with open(vocab_file, 'r', encoding='utf8') as f:
            for korword, nertag in [line.split('\t') for line in f.readlines()]:
                korword = korword.strip()
                nertags = nertag.strip().split(',')
                
                tagset = vocab.get(korword, set())
                for nertag in nertags:
                    tagset.add(nertag)
                vocab[korword] = tagset
        return vocab
    
    def transform(self, X):
        '''
        단어로 구분된 데이터 셋
        배치를 가젯 특성으로 변환
        입력: (배치, 시퀀스 최대 길이)
        출력: (배치, 시퀀스 최대 길이, 가젯 레이블 수)
        '''
        constant_length = len(X[0])
        feature = np.empty((len(X), constant_length, len(self.label2idx)))
        for i, seq in enumerate(X):
            assert(constant_length == len(seq))
            feature[i] = self.transform_line(seq)
        return feature
    
    def transform_line(self, line):
        '''
        단어로 구분된 데이터 셋
        문장을 가젯 특성으로 변환
        입력: (시퀀스 최대 길이)
        출력: (시퀀스 최대 길이, 가젯 레이블 수)
        '''
        feature = np.empty((len(line), len(self.label2idx)))
        for i, word in enumerate(line):
            feature[i] = self.transform_word(word)
        return feature
                
    def transform_word(self, word):
        '''
        단어로 구분된 데이터 셋
        단어를 가젯 특성으로 변환
        입력: 자연어 단어 하나
        출력: (가젯 레이블 수,)
        '''
        if word in self.vocab:
            hot = [self.label2idx[nertag] for nertag in self.vocab[word]]
        else:
            hot = []
         
        feature = np.zeros(len(self.label2idx))
        for idx in hot:
            feature[idx] = 1
        return feature
    
    def transform_charaterized(self, X, ngram):
        '''
        음절로 구분된 데이터 셋
        배치를 가젯 특성으로 변환
        입력: (배치, 시퀀스)
        출력: (배치, 시퀀스 최대 길이, 가젯 레이블 수)
        '''
        constant_length = len(X[0])
        feature = np.empty((len(X), constant_length, len(self.label2idx)))
        for i, seq in enumerate(X):
            assert(constant_length == len(seq))
            feature[i] = self.transform_charaterized_line(seq, ngram)
        return feature
    
    def transform_charaterized_line(self, line, ngram):
        '''
        음절로 구분된 데이터 셋
        문장을 가젯 특성으로 변환
        입력: (시퀀스 최대 길이)
        출력: (시퀀스 최대 길이, 가젯 레이블 수)
        '''
        line_length = len(line)
        feature = np.zeros((len(line), len(self.label2idx)))
        for charpos in range(line_length - ngram + 1):
            ngram_word = "".join(line[charpos: ngram])
            ngram_word_feature = self.transform_word(ngram_word)
            for attach in range(ngram):
                feature[charpos+attach] += ngram_word_feature
        return feature
                    
    def transform_end2end(self, line, max_length, ngram=4):
        '''
        음절로 띄어쓰기 된 End2End 데이터 셋
        문장을 가젯 특성으로 변환
        입력: 음절로 띄어쓰기 된 문장 스트링
        출력: (시퀀스 최대 길이, 가젯 레이블 수)
        '''
        sentence = line.split()
        if len(sentence) <= max_length:
            sentence += ['<UNK>'] * (max_length - len(sentence))
        else:
            sentence = sentence[:max_length]
        feature = self.transform_charaterized_line(sentence, ngram)
        return feature
    
    def transform_end2end_complex_ngrams(self, line, max_length, ngrams):
        '''
        음절로 띄어쓰기 된 End2End 데이터 셋
        문장을 가젯 특성으로 변환
        입력: 음절로 띄어쓰기 된 문장 스트링
        출력: (시퀀스 최대 길이, 가젯 레이블 수)
        '''
        feature = self.transform_end2end(line, max_length, ngrams[0])
        for i, ngram in enumerate(ngrams):
            if 0 != i:
                feature = np.hstack((feature, self.transform_end2end(line, max_length, ngram)))
        return feature
    
  