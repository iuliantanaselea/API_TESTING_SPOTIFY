from utils.constants import *
import requests


def get_show(show_id, market):
    response = requests.get(f'{API}/shows/{show_id}?market={market}', headers=HEADER)
    return response


def get_user_saved_shows():
    response = requests.get(f'{API}/me/shows', headers=HEADER)
    return response


def save_shows_for_current_user(shows_ids):
    response = requests.put(f'{API}/me/shows?ids={shows_ids}', headers=HEADER)
    return response


def remove_user_saved_shows(shows_ids):
    response = requests.delete(f'{API}/me/shows?ids={shows_ids}', headers=HEADER)
    return response

