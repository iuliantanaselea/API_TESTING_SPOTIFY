from utils.constants import *
import requests


def get_playlist(playlist_id):
    response = requests.get(f"{API}/playlists/{playlist_id}", headers=HEADER)
    return response


def change_playlist_details(playlist_id, new_name, new_description):
    body = {
        'name': new_name,
        'description': new_description,
        'public': False
    }
    response = requests.put(f'{API}/playlists/{playlist_id}', json=body, headers=HEADER)
    return response


def create_playlist(name, description):
    body = {
        'name': name,
        'description': description,
        'public': False
    }
    response = requests.post(f'{API}/users/{USER_ID}/playlists', json=body, headers=HEADER)
    return response
