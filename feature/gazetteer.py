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
                nertag = nertag.strip()
                tagset = vocab.get(korword, set())
                tagset.add(nertag)
                vocab[korword] = tagset
        return vocab
    
    def transform(self, X):
        '''
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
        입력: (시퀀스 최대 길이)
        출력: (시퀀스 최대 길이, 가젯 레이블 수)
        '''
        feature = np.empty((len(line), len(self.label2idx)))
        for i, word in enumerate(line):
            feature[i] = self.transform_word(word)
        return feature
                
    def transform_word(self, word):
        if word in self.vocab:
            hot = [self.label2idx[nertag] for nertag in self.vocab[word]]
        else:
            hot = [self.label2idx['O']]
         
        feature = np.zeros(len(self.label2idx))
        for idx in hot:
            feature[idx] = 1
        return feature
   