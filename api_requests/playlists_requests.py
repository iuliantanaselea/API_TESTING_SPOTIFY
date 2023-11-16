from pprint import pprint
from constants import *
import requests

def get_playlist(playlist_id):
    response = requests.get(f"{API}/playlists/{playlist_id}", headers=HEADER)
    return response

playlist_id = "3cEYpjA9oz9GiPac4AsH4n"


# pprint(get_playlist(playlist_id).json())

def change_playlist_details(playlist_id, new_name, new_description):
    body = {
        'name': new_name,
        'description': new_description,
        'public': False
    }
    response = requests.put(f'{API}/playlists/{playlist_id}', json=body, headers=HEADER)
    return response


playlist_id = "0MVvvW8Q9fk4j55oCMxXKq"
new_name = "Updated Playlist Name"
new_description = "Updated playlist description"

# pprint(change_playlist_details(playlist_id, new_name, new_description).status_code)


def create_playlist(user_id,name,description):
    body = {
        'name': name,
        'description': description,
        'public': False
    }
    response = requests.post(f'{API}/users/{user_id}/playlists',json=body, headers=HEADER)
    return response

name = "New Playlist_2"
description = "New playlist description"
user_id = 'iuliantanaselea'

# pprint(create_playlist(user_id,name,description).status_code)