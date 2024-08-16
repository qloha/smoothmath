import requests

def check_for_message(url, auth, message):
    headers = {
        "Authorization": auth
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        messages = res.json()
        for message in messages[:5]:
            if message in message['content'].lower():
                return True
    return False