import requests

def send_post_request(url, payload, headers=None):
    if headers is None:
        headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response
