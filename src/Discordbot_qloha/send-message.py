import requests

def send_message(url, auth, content):
    payload = {
        "content": content
    }
    res = requests.post(url, json=payload, headers=auth)
    print(f"Sent message: {content}")