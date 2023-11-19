from pprint import pprint
from utils.constants import *
import requests


def get_episode(episode_id, market):
    response = requests.get(f'{API}/episodes/{episode_id}?market={market}', headers=HEADER)
    return response


episode_id = "512ojhOuo1ktJprKbVcKyQ"
market = "RO"


# pprint(get_episode(episode_id, market).json())


def get_several_episodes(episode_ids, market):
    response = requests.get(f'{API}/episodes?ids={episode_ids}&market={market}', headers=HEADER)
    return response


episode_ids = "6XLYRBk4nzGUHkMYA3NpB3,0Q86acNRm6V9GYx55SXKwf"


# pprint(get_several_episodes(episode_ids, market).json())

def get_user_saved_episodes(market):
    response = requests.get(f"{API}/me/episodes?market={market}", headers=HEADER)
    return response


market = "RO"
pprint(get_user_saved_episodes(market).json())

def save_episodes_for_current_user(ids):
    body = {
        'ids': ids
    }
    response = requests.put(f'{API}/episodes', json=body, headers=HEADER)
    return response


episodes_ids = "6XLYRBk4nzGUHkMYA3NpB3"
# save_episodes_for_current_user(episodes_ids)


def check_user_saved_episodes(episode_ids):
    response = requests.get(f'{API}/me/episodes/contains?ids={episode_ids}', headers=HEADER)
    return response

# pprint(check_user_saved_episodes(episodes_ids).json())
