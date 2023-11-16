from pprint import pprint
from constants import *
import requests

artist_id = "0TnOYISbd1XYRBk9myaseg"
def get_artist(artist_id):
    response = requests.get(f'{API}/artists/{artist_id}', headers=HEADER)
    return response



def get_several_artists(artists_ids):
    response = requests.get(f'{API}/artists?ids={artists_ids}', headers=HEADER)
    return response

artists_ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"


def get_artist_albums(artist_id):
    response = requests.get(f'{API}/artists/{artist_id}/albums',headers=HEADER)
    return response



def get_artist_albums_filtered(artist_id,market,limit):
    response = requests.get(f'{API}/artists/{artist_id}/albums?market={market}&limit={limit}', headers=HEADER)
    return response

artist_id = "0TnOYISbd1XYRBk9myaseg"
market= "RO"
limit=2



def get_artist_top_tracks(artist_id,market):
    response = requests.get(f'{API}/artists/{artist_id}/top-tracks?market={market}',headers=HEADER)
    return response



def get_artist_related_artists(artist_id):
    response = requests.get(f'{API}/artists/{artist_id}/related-artists',headers=HEADER)
    return response

# pprint(get_artist(artist_id).json())
# pprint(get_several_artists(artists_ids).json())
# pprint(get_artist_albums(artist_id).json())
# pprint(get_artist_albums_filtered(artist_id,market,limit).json())
# pprint(get_artist_top_tracks(artist_id,market).json())
pprint(get_artist_related_artists(artist_id).json())
