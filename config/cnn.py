from .base import BaseConfig
from .gazette import GazetteModelConfig

class CnnModelConfig(BaseConfig):
    
    additional_config_dict = {
        'num_filters': 16
    }
    
    def __init__(self, *args, **kwargs):
        '''
        Additional Properties
            num_filters: int = 16(default)
        '''
        super(CnnModelConfig, self).__init__(*args, **kwargs)
        
        
class CnnGazetteModelConfig(CnnModelConfig):
    
    def __init__(self, *args, **kwargs):
        '''
        Create a CNN model configuration, combining a Gazette model.
        '''
        super(CnnGazetteModelConfig, self).__init__(*args, **kwargs)
        gazette_config = GazetteModelConfig(*args, **kwargs)
        self.config_dict.update(gazette_config.config_dict)