from .base import BaseConfig

class PostagModelConfig(BaseConfig):
    
    additional_config_dict = {
        'features': ['feature.postag.PosTagFeature', 'konlpy.tag.Mecab'],
        'postag_feature_length': 44,
    }
    
    def __init__(self, *args, **kwargs):
        '''
        Additional Properties
            postag_feature_length: int = 44(default)
        '''
        super(PostagModelConfig, self).__init__(*args, **kwargs)
   
    def tagger_tool(self):
        last = len(self.config_dict['features']) - 1
        return self.feature_tool(last)