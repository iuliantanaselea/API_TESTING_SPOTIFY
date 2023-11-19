from pprint import pprint
from utils.constants import *
import requests


def get_audiobook(audiobook_id):
    response = requests.get(f'{API}/audiobooks/{audiobook_id}', headers=HEADER)
    return response


audiobook_id = "7iHfbu1YPACw6oZPAFJtqe"
market = "RO"

pprint(get_audiobook(audiobook_id).json())
# Will return message: "Non existing id: 'spotify:show:7iHfbu1YPACw6oZPAFJtqe'", because audiobooks
#   are only available for the US,UK,Ireland, New Zealand and Australia markets.
