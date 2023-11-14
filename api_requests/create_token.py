import base64
from pprint import pprint

import requests

encoded_credentials = base64.b64encode(
    'ccf82a4afbf94835b03d7111b8bd310d'.encode() + b":" + '12452e0e406b435386be3de011a4e28f'.encode()).decode('utf-8')


def create_token():
    header = {
        'Authorization': 'Basic ' + encoded_credentials,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post('https://accounts.spotify.com/api/token?grant_type=client_credentials', headers=header)

TOKEN = "BQArQgB0wKLBE8H6pIm8cE__AkI35rdo7_RGzsmDGXStlkPjkUiuMk6uGOPuiEcQXKg0ZZyI3Y18DhOZ6EtdpAOaqIvYA1593clCIz-dEd9q-iYTjZ4"

# Se ruleaza comanda de mai jos pentru a obtine un nou token, si modificati token-ul de mai sus
# pprint(create_token().json())
