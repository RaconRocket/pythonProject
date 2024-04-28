import logging
import requests as rq
from success_responses import sites

logger = logging.getLogger('blocked_responses')


def blocked_requests_checker():
    for site in sites:
        # ДОПОЛНИТЬ КОД ЗДЕСЬ
        try:
            response = rq.get(url=site, timeout=3, verify=False)
            if response.status_code is None:
                continue
        except Exception:
            logger.error(f'"{site}", NO CONNECTION')


if __name__ == '__main__':
    blocked_requests_checker()
