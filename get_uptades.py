import requests

from config import TOKEN


def get_uptades():
    url = f'https://api.telegram.org/bot{TOKEN}/'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    raise Exception('Bad Request')


data = get_uptades()
print(data)

