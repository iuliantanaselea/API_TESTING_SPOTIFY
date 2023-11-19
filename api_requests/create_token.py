import base64

import requests

from utils.constants import CLIENT_ID, REDIRECT_URI, SCOPE, CLIENT_SECRET

encoded_credentials = base64.b64encode(
    CLIENT_ID.encode() + b":" + CLIENT_SECRET.encode()).decode('utf-8')


def create_token():
    header = {
        'Authorization': 'Basic ' + encoded_credentials,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post('https://accounts.spotify.com/api/token?grant_type=client_credentials', headers=header)

def get_auth():
    return requests.get(
        f'https://accounts.spotify.com/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}')




def request_access_token(authorization_code):
    header = {
        'Authorization': 'Basic ' + encoded_credentials,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post(f'https://accounts.spotify.com/api/token?grant_type=authorization_code&code={authorization_code}&redirect_uri={REDIRECT_URI}', headers = header)
