import base64
from pprint import pprint

import requests

from api_requests.constants import CLIENT_ID, REDIRECT_URI, SCOPE, CLIENT_SECRET

encoded_credentials = base64.b64encode(
    CLIENT_ID.encode() + b":" + CLIENT_SECRET.encode()).decode('utf-8')


def create_token():
    header = {
        'Authorization': 'Basic ' + encoded_credentials,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post('https://accounts.spotify.com/api/token?grant_type=client_credentials', headers=header)


# ACCESS_TOKEN = "BQADjI4cNDls9EPPAeiQqqd5f2wzke16cig3eqO2SsjbE8pSnpKxPNxjJWqeXknF7m9gmBnyBsiOTh48EesSCbEiZlpeKPEXkBdOxoLbSZdP50PbX-o"


# Se ruleaza comanda de mai jos pentru a obtine un nou token, si modificati token-ul de mai sus
# pprint(create_token().json())

def get_auth():
    return requests.get(
        f'https://accounts.spotify.com/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}')




def request_access_token(authorization_code):
    header = {
        'Authorization': 'Basic ' + encoded_credentials,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post(f'https://accounts.spotify.com/api/token?grant_type=authorization_code&code={authorization_code}&redirect_uri={REDIRECT_URI}', headers = header)
