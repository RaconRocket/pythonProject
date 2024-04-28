import logging.config
from logging_hw.hw_log_settings import log_config
from success_responses import requests_checker
from blocked_responses import blocked_requests_checker
from bad_responses import bad_requests_checker

logging.config.dictConfig(log_config)

requests_checker()
blocked_requests_checker()
bad_requests_checker()
