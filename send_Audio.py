import requests

from config import TOKEN


def get_sendaudio(chat_id, audio_file_path):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    
    with open(audio_file_path, 'rb') as audio:
        files = {'audio': audio}
        data = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        return response.json()
    
    raise Exception(f'Bad Request: {response.text}')



