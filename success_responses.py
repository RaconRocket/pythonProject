import certifi
import requests as rq
import logging

logger = logging.getLogger('success_responses')


sites = ['https://www.youtube.com/',
         'https://instagram.com',
         'https://wikipedia.org',
         'https://yahoo.com',
         'https://yandex.ru',
         'https://whatsapp.com',
         'https://twitter.com',
         'https://amazon.com',
         'https://tiktok.com',
         'https://www.ozon.ru',
         ]


def requests_checker():
    for site in sites:
        # ДОПОЛНИТЬ КОД ЗДЕСЬ
        try:
            response = rq.get(url=site, timeout=3, verify=False)
            resp = response.status_code
            if resp == 200:
                logger.info(f'"{site}", response - {resp}')
            else:
                continue
        except Exception:
            continue
