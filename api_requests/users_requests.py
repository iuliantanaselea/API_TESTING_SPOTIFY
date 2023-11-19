from pprint import pprint
from utils.constants import *
import requests

def get_current_user_profile():
    response = requests.get(f'{API}/me', headers=HEADER)
    return response

pprint(get_current_user_profile().json())
