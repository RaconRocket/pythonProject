log_config = {
    'version': 1,
    'formatters': {
        'success_responses_formatter': {
            'format': '%(levelname)s: %(message)s'
        },
        'bad_responses_formatter': {
            'format': '%(levelname)s: %(message)s'
        },
        'blocked_responses_formatter': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'success_responses_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'success_responses_formatter',
            'filename': 'success_responses.log',
            'encoding': 'utf-8',
        },
        'bad_responses_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'bad_responses_formatter',
            'filename': 'bad_responses.log',
            'encoding': 'utf-8',
        },
        'blocked_responses_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'blocked_responses_formatter',
            'filename': 'blocked_responses.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'success_responses': {
            'handlers': ['success_responses_handler'],
            'level': 'INFO',
        },
        'bad_responses': {
            'handlers': ['bad_responses_handler'],
            'level': 'WARNING',
        },
        'blocked_responses': {
            'handlers': ['blocked_responses_handler'],
            'level': 'ERROR',
        },
    },
}
