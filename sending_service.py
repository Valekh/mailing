import requests

token = 'TOKEN'


def send_message(message_id: int, phone: int, text: str):
    data = {"id": message_id,
            "phone": phone,
            "text": text}
    link = f'https://probe.fbrq.cloud/v1/send/{message_id}'

    res = requests.post(link, headers={'Authorization': f'{token}'}, json=data, timeout=30)
    return res.status_code
