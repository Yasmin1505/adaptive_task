import traceback

import requests
from common.config import Config


def get_wiki_article(article_name):
    try:
        url = f'{Config.WIKIPEDIA_BASE_URL}/{article_name}'
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(url=url, headers=headers)

        return response
    except Exception as ex:
        print(f'Failed to fetch Wikipedia article "List of Animal names" with exception: {ex}, Traceback: {traceback.format_exc()}') # [YS] I would use some kind of logger
        raise Exception(f'Failed to fetch Wikipedia article "List of Animal names" with exception: {ex}, Traceback: {traceback.format_exc()}')