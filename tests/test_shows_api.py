from pprint import pprint

from api_requests.shows_requests import *
from test_data.shows_data import *


class TestShowsAPI:
    def test_get_show(self):
        show = get_show(SHOWS_IDS["Without Fail"], "RO").json()
        assert show['name'] == "Without Fail"
        assert show['publisher'] == "Gimlet"
        assert show['type'] == 'show'
        assert show['media_type'] == 'audio'

    def test_save_shows_for_current_user(self):
        shows_ids = f"{SHOWS_IDS['Without Fail']},{SHOWS_IDS['Giant Bombcast']}"
        status_code = save_shows_for_current_user(shows_ids).status_code
        assert status_code == 200
        items = get_user_saved_shows().json()['items']
        for item in items:
            assert item['show']['name'] == "Without Fail" or "Giant Bombcast"
        delete_status_code = remove_user_saved_shows(shows_ids).status_code
        assert delete_status_code == 200
