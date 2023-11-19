from pprint import pprint
from utils.constants import *
import requests


def get_album(album_id):
    response = requests.get(f"{API}/albums/{album_id}", headers=HEADER)
    return response


def get_albums(album_ids):
    response = requests.get(f"{API}/albums?ids={album_ids}", headers=HEADER)
    return response

def save_albums_for_curent_user(albums_ids):
    body = {
        'ids': albums_ids
    }
    response = requests.put(f"{API}/me/albums", json=body, headers=HEADER)
    return response

def delete_albums_for_curent_user(ids):
    body = {
        'ids': ids
    }
    response = requests.delete(f"{API}/me/albums", json=body, headers=HEADER)
    return response
def get_user_saved_albums(limit=20, offset=0,market=""):
    response = requests.get(f"{API}/me/albums?limit={limit}&offset={offset}&market={market}",headers=HEADER)
    return response



# r = get_album("3a0UOgDWw2pTajw85QPMiz")
# print(r.status_code)
# pprint(r.json())
