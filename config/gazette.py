from .base import BaseConfig

class GazetteModelConfig(BaseConfig):
    
    additional_config_dict = {
        'features': ['feature.gazetteer.GazetteFeature'],
        'gazette_feature_length': 7,
        'ngrams': [2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    
    def __init__(self, *args, **kwargs):
        '''
        Additional Properties
            features: List[feature.*.*] = ['feature.gazetter.GazetterFeature'],
            gazette_feature_length: int
            ngrams: List[int]
        '''
        super(GazetteModelConfig, self).__init__(*args, **kwargs)