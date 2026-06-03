
import requests

from config import TOKEN


def get_updates(offset: int | None = None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"offset": offset}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["result"]

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    raise Exception("Bad Request")


def send_message(chat_id: int, text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.get(url, params=params)


def send_photo(chat_id: int, photo: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    params = {"chat_id": chat_id, "photo": photo}
    requests.get(url, params=params)


def send_voice(chat_id: int, voice: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVoice"
    params = {"chat_id": chat_id, "voice": voice}
    requests.get(url, params=params)

def send_video(chat_id: int, video: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    params = {"chat_id": chat_id, "video": video}
    requests.get(url, params=params)

def send_location(chat_id: int, location: dict):
    url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
    params = {"chat_id": chat_id, location: "location"}
    requests.get(url, params=params)
def main():
    update_id = None

    while True:
        for update in get_updates(offset=update_id):
            if update.get("message"):
                print(f"Update: {update}")
                if update["message"].get("text"):
                    send_message(
                        chat_id=update["message"]["chat"]["id"],
                        text=update["message"]["text"],
                    )
                elif update['message'].get('photo'):
                    send_photo(
                        chat_id=update["message"]["chat"]["id"],
                        photo=update["message"]["photo"][0]['file_id']
                    )
                elif update['message'].get('voice'):
                    send_voice(
                            chat_id=update["message"]["chat"]["id"],
                            voice=update["message"]["voice"]["file_id"]
                    )
                elif update['message'].get('video'):
                    send_video(
                            chat_id=update["message"]["chat"]["id"],
                            video=update["message"]["video"]["file_id"]
                    )
                elif update['message'].get('location'):
                    send_location(
                        chat_id=update["message"]["chat"]["id"],
                        location=update["message"]["location"]
                    )
                update_id = update["update_id"] + 1
main()