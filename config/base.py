from copy import copy
from settings import (
    ROOT_DIR, OUTPUT_DIR,
    TRAIN_FILE, DEV_FILE,
    WORD_VOCAB_FILE, TAG_VOCAB_FILE
)

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
  "lr": 0.0003
}

def module_and_class(string):
    tok = string.split('.')
    mod = ".".join(tok[0:-1])
    cls = tok[-1]
    return __import__(mod, fromlist=[cls]), cls

def instantiate(string):
    mod, cls = module_and_class(string)
    return getattr(mod, cls)()

class BaseConfig:
    '''
    Base Properties
        mode: str = "train"(default) or "test"
        root_dir: str,
        train_file: str,
        dev_file: str,
        word_vocab_file: str,
        tag_vocab_file: str,
        trained_model_name: str, 
        output_dir_path: str,
        word_vocab_size: int = 2160(default),
        number_of_tags: int = 14(default),
        hidden_size: int = 200(default),
        dropout:float = 0.2(default),
        embedding_size: int = 200(default),
        max_length: int = 150(default),
        batch_size: int = 64(default),
        epoch: int = 20(default),
        features: List[feature.*.*],
        lr: int = 0.003(default)
    '''
    
    def __init__(self, *args, **kwargs):
        self.config_dict = copy(base_config)
        
        if self.additional_config_dict is not None:
            self.config_dict.update(self.additional_config_dict)
        
        if kwargs is not None:
            self.config_dict.update(kwargs)
        
    def __getitem__(self, key):
        return self.config_dict[key]
    
    def __setitem__(self, key, val):
        self.config_dict[key] = val
        
    def __str__(self):
        return str(self.config_dict)
        
    def feature_tool(self, idx):
        return instantiate(self.config_dict['features'][idx])