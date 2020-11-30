
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
  "hidden_size": 100,
  "dropout":0.2,
  "embedding_size":100,
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
gazetteer_model_config['epoch'] = 50
gazetteer_model_config['features'] = ['feature.gazetteer.GazetteFeature']
gazetteer_model_config['gazette_feature_length'] = 7
gazetteer_model_config['ngram'] = 4