from pprint import pprint

import requests

from api_requests.create_token import ACCESS_TOKEN

API = "https://api.spotify.com/v1"

headers = {
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    # reprezinta valoarea token-ului de autentificare, Client secret

}


def get_album(album_id):
    response = requests.get(f"{API}/albums/{album_id}", headers=headers)
    return response


def get_albums(album_ids):
    response = requests.get(f"{API}/albums?ids={album_ids}", headers=headers)
    return response

album_ids='382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo'

r= get_albums(album_ids)


# r = get_album("3a0UOgDWw2pTajw85QPMiz")
print(r.status_code)
pprint(r.json())
