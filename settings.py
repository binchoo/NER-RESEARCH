
ROOT_DIR = '.'
OUTPUT_DIR = './output'

TRAIN_FILE = 'ner_train.txt'
DEV_FILE = 'ner_dev.txt'

WORD_VOCAB_FILE = "vocab/word_vocab.txt"
TAG_VOCAB_FILE = "vocab/tag_vocab.txt"

base_config = {
  "mode": "train",
  "root_dir": ROOT_DIR,
  "train_file": TRAIN_FILE,
  "dev_file": DEV_FILE,
  "word_vocab_file": WORD_VOCAB_FILE,
  "tag_vocab_file": TAG_VOCAB_FILE,
  "trained_model_name":"epoch_{}.pt".format(5),
  "output_dir_path":OUTPUT_DIR,
  "word_vocab_size":2160,
  "number_of_tags": 14,
  "hidden_size": 200,
  "dropout":0.2,
  "embedding_size":200,
  "max_length": 150,
  "batch_size":64,
  "epoch":20,
  "features": None,
}

from copy import copy

######                                 ######
# Configurations of Gazetteer Feature Model#
######                               ######
GAZETTEER_VOCAB = 'vocab/korean_gazette.txt'
GAZETTEER_LABEL = 'vocab/gazetteer_label.txt'

gazetteer_model_config = copy(base_config)
gazetteer_model_config['mode'] = 'train'
gazetteer_model_config['epoch'] = 30
gazetteer_model_config['features'] = ['feature.gazetteer.GazetteFeature']
gazetteer_model_config['gazette_feature_length'] = 5
gazetteer_model_config['ngrams'] = [3, 4, 5, 6, 7, 8, 9, 10]

######                               ######
# Configurations of POS Tag Feature Model#
######                             ######
POS_LABEL = 'vocab/pos_label.txt'

postag_model_config = copy(base_config)
postag_model_config['mode'] = 'train'
postag_model_config['epoch'] = 30
postag_model_config['features'] = ['feature.postag.PosTagFeature']
postag_model_config['postag_feature_length'] = 44
postag_model_config['tagger'] = 'konlpy.tag.Mecab'

######                                           ######
# Configurations of Gazetteer & Pos Tag Feature Model#
######                                         ######
gazettpos_model_config = copy(base_config)
gazettpos_model_config['mode'] = 'train'
gazettpos_model_config['epoch'] = 200
gazettpos_model_config['features'] = ['feature.gazetteer.GazetteFeature', 'feature.postag.PosTagFeature']
gazettpos_model_config['gazette_feature_length'] = 5
gazettpos_model_config['ngrams'] = [3, 4, 5, 6, 7, 8, 9, 10]
gazettpos_model_config['postag_feature_length'] = 44
gazettpos_model_config['tagger'] = 'konlpy.tag.Mecab'

######                                           ######
# Configurations of Gazetteer & Pos Tag Feature Model#
######                                         ######
gazettcnn_model_config = copy(gazetteer_model_config)
gazettcnn_model_config['num_filters'] = 16