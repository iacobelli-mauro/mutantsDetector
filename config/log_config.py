from logging.config import dictConfig
import logging

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        },
        'detailed': {
            'format': '%(asctime)s %(threadName)s %(module)-17s line:%(lineno)-4d ' \
            '%(levelname)-8s %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': logging.DEBUG,
            'formatter': 'detailed',
            'filename': 'logs/MutantDetector.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': logging.INFO,
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file', 'console']
    },
    'disable_existing_loggers': False
    
})
