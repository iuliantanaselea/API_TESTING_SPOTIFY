from utils.constants import *
import requests


def get_episode(episode_id, market):
    response = requests.get(f'{API}/episodes/{episode_id}?market={market}', headers=HEADER)
    return response


def get_several_episodes(episode_ids, market):
    response = requests.get(f'{API}/episodes?ids={episode_ids}&market={market}', headers=HEADER)
    return response


def get_user_saved_episodes(market):
    response = requests.get(f"{API}/me/episodes?market={market}", headers=HEADER)
    return response


def save_episodes_for_current_user(ids):
    body = {
        'ids': ids
    }
    response = requests.put(f'{API}/episodes', json=body, headers=HEADER)
    return response


def check_user_saved_episodes(episode_ids):
    response = requests.get(f'{API}/me/episodes/contains?ids={episode_ids}', headers=HEADER)
    return response
