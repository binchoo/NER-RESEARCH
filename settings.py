#directories


#config for gazetteer feature
GAZETTEER_VOCAB = 'vocab/korean_gazette.txt'
GAZETTEER_LABEL = 'vocab/gazetteer_label.txt'

gazetteer_model_config = {
  "mode": "train",
  "root_dir"='.',
  "output_dir"='./output',
  "train_file":"ner_train.txt",
  "dev_file": "ner_dev.txt",
  "word_vocab_file":"vocab/word_vocab.txt",
  "tag_vocab_file":"vocab/tag_vocab.txt",
  "trained_model_name":"epoch_{}.pt".format(5),
  "output_dir_path":output_dir,
  "word_vocab_size":2160,
  "number_of_tags": 14,
  "hidden_size": 100,
  "dropout":0.2,
  "embedding_size":100,
  "max_length": 150,
  "batch_size":64,
  "epoch":50,
  "features": ['feature.gazetteer.GazetteFeature'],
  "ngram":4,
}