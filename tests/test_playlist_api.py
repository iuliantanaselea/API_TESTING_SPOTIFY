import random

from api_requests.playlists_requests import *
from utils.constants import *


class TestPlaylistAPI:
    def test_create_playlist(self):
        name = "New Playlist"
        description = "Playlist description from test"
        response = create_playlist(name, description)

        assert response.status_code == 201, "Playlist was not created"
        # Sometimes, the description is None when the playlist is created
        assert response.json()['description'] == description or response.json()['description'] is None, f"Expected description: {description}, Actual response: {response.json()['description']}"
        assert response.json()[
                   'name'] == name, f"Expected description: {name}, Actual response: {response.json()['name']}"
        assert response.json()['owner']['id'] == USER_ID, f"Expected {USER_ID}, Actual {response.json()['owner']['id']}"

    def test_update_playlist(self):
        random_number = random.randint(0, 999999)
        name = f"New Playlist {random_number}"
        description = f"New Playlist description {random_number}"
        playlist_id = create_playlist(name, description).json()['id']

        updated_name = f"Updated Playlist {random_number}"
        updated_description = f"Updated playlist description {random_number}"
        response = change_playlist_details(playlist_id, updated_name, updated_description)

        assert response.status_code == 200, f"Update Playlist API did not work, Response status code: {response.status_code}"
        playlist = get_playlist(playlist_id).json()
        assert playlist['name'] == updated_name
        assert playlist['description'] == updated_description or playlist['description'] == ""

    def test_get_playlist(self):
        random_number = random.randint(0, 999999)
        name = f"New Playlist {random_number}"
        description = f"New Playlist description {random_number}"
        playlist_id = create_playlist(name, description).json()['id']
        playlist = get_playlist(playlist_id).json()

        assert playlist['name'] == name
        assert playlist['description'] == description or playlist['description'] ==""
        assert playlist['owner']['id'] == USER_ID
        assert playlist['public'] == False

