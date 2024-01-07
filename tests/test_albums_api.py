from api_requests.albums_requests import *
from test_data.albums_data import *


class TestAlbumsAPI:
    def test_get_album(self):
        album = get_album(ALBUMS_IDS['Arhitectul_din_Babel']).json()

        assert album['id'] == ALBUMS_IDS['Arhitectul_din_Babel']
        assert album['name'] == "Arhitectul Din Babel"
        assert album['type'] == 'album'

    def test_get_several_albums(self):
        album_ids = f"{ALBUMS_IDS['Arhitectul_din_Babel']},{ALBUMS_IDS['Haosoleum']}"
        albums = get_albums(album_ids).json()

        assert len(albums['albums']) == 2
        for album in albums['albums']:
            assert album['id'] == ALBUMS_IDS['Arhitectul_din_Babel'] or album['id'] == ALBUMS_IDS['Haosoleum']

    def test_save_albums_for_current_user(self):
        albums_ids = [ALBUMS_IDS['Arhitectul_din_Babel'],ALBUMS_IDS['Haosoleum']]
        status_code = save_albums_for_curent_user(albums_ids).status_code
        assert status_code == 200
        items = get_user_saved_albums(market="RO").json()['items']
        for item in items:
            assert (item['album']['id'] == ALBUMS_IDS['Arhitectul_din_Babel'] or
                    item['album']['id'] == ALBUMS_IDS['Haosoleum'])

        delete_status_code = delete_albums_for_curent_user(albums_ids).status_code
        assert delete_status_code == 200
