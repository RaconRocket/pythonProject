import logging
import requests as rq
from success_responses import sites

logger = logging.getLogger('bad_responses')


def bad_requests_checker():
    for site in sites:
        # ДОПОЛНИТЬ КОД ЗДЕСЬ
        try:
            response = rq.get(site, timeout=3, verify=False)
            if response.status_code != 200:
                logger.warning(f'"{site}", response - {response.status_code}')
            else:
                continue
        except Exception:
            continue


if __name__ == '__main__':
    bad_requests_checker()
