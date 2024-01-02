from pprint import pprint
from utils.constants import *
import requests


def get_artist(artist_id):
    response = requests.get(f'{API}/artists/{artist_id}', headers=HEADER)
    return response


def get_several_artists(artists_ids):
    response = requests.get(f'{API}/artists?ids={artists_ids}', headers=HEADER)
    return response


def get_artist_albums(artist_id):
    response = requests.get(f'{API}/artists/{artist_id}/albums', headers=HEADER)
    return response


def get_artist_albums_filtered(artist_id, market, limit):
    response = requests.get(f'{API}/artists/{artist_id}/albums?market={market}&limit={limit}', headers=HEADER)
    return response


def get_artist_top_tracks(artist_id, market):
    response = requests.get(f'{API}/artists/{artist_id}/top-tracks?market={market}', headers=HEADER)
    return response


def get_artist_related_artists(artist_id):
    response = requests.get(f'{API}/artists/{artist_id}/related-artists', headers=HEADER)
    return response
