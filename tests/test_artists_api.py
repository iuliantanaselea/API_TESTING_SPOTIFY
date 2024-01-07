from api_requests.artists_requests import *
from test_data.artists_data import *


class TestArtistsAPI:
    def test_get_artist(self):
        artist = get_artist(ARTISTS_IDS['Alternosfera']).json()
        assert artist['id'] == ARTISTS_IDS['Alternosfera']
        assert artist['name'] == "Alternosfera"
        assert artist['type'] == 'artist'

    def test_get_several_artists(self):
        artist_ids = f"{ARTISTS_IDS['Alternosfera']},{ARTISTS_IDS['Jurjak']}"
        artists = get_several_artists(artist_ids).json()
        assert len(artists['artists']) == 2
        for artist in artists['artists']:
            assert artist['id'] == ARTISTS_IDS['Alternosfera'] or artist['id'] == ARTISTS_IDS['Jurjak']

    def test_get_artist_albums(self):
        artist_albums = get_artist_albums(ARTISTS_IDS['Alternosfera']).json()['items']
        assert (len(artist_albums) >=1 )
        for album in artist_albums:
            for element in album['artists']:
                assert element['name'] == "Alternosfera"

    def test_get_artist_albums_filtered(self):
        artist_albums_filtered = get_artist_albums_filtered(ARTISTS_IDS["Jurjak"],'RO',3).json()['items']
        assert len(artist_albums_filtered) == 3
        for album in artist_albums_filtered:
            for element in album['artists']:
                assert element['name'] == "Jurjak"

    def test_get_artist_related_artists(self):
        artist_related_artists = get_artist_related_artists(ARTISTS_IDS['Jurjak']).json()['artists']
        related_artists_list=[]
        for artist in artist_related_artists:
            related_artists_list.append(artist['name'])
        assert 'Les Elephants Bizarres' in related_artists_list