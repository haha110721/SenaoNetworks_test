import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'normal': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
    },
    
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': './log.txt',
            'formatter': 'normal',
        }
    },
    
    'loggers': {
        'file_logger': {
            'handlers': ['file_handler'],
            'level': 'INFO',
        }
    }
}
