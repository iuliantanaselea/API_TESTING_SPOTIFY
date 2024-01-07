# SCOPE determina ce permisiuni are utilizatorul
SCOPE = "user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position"
# CLIENT_ID = 'YOUR CLIENT ID' #Valoarea se gaseste in panoul de comanda al aplicatiei Spotify
CLIENT_ID = '32cbf2e3eb0b43b29f6f1da9813ef669' #Valoarea se gaseste in panoul de comanda al aplicatiei Spotify
# CLIENT_SECRET = 'YOUR CLIENT SECRET' #Valoarea se gaseste in panoul de comanda al aplicatiei Spotify
CLIENT_SECRET = 'da930ff5d67a4da08e83d02ae77d5f63' #Valoarea se gaseste in panoul de comanda al aplicatiei Spotify
REDIRECT_URI = 'http://localhost:8080'
API = "https://api.spotify.com/v1"
# USER_ID = "YOUR USER ID"
USER_ID = "317eaadf4s4xlnf5n5dqoo33swd4"


#Va fi inlocuit manual cu codul obtinut ruland fisierul "run_create_token.py"
ACCESS_TOKEN = 'BQBilV-bsjBLN-AVaS9XpMXU0S_Uwxm9GKZf_V1wk7SXK2IjT87RMZpB4LRxK2BpdA7kSrpyM1CVx4hvnHJOQYG4II-LBpY5H4k6voNvW3U9kqkqmAP4H0YmPL5KxfiZ1xGp9ljCjlpH399_b7xhGExDfblX_mFikNAPOhJaR2cmTrS8oqqKRH3aWwbDvo7N_lqR7hTt89V0__PxehdG9NBXTjsyIJ86Gh8pVHFVnSMGgu_VOkphYTUonYscOJrUIKWSCfsxvrsE70VlrUTVBhfwhUgMQY3yUSxvNPRkvxQ'

HEADER = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    # reprezinta valoarea tokenului de autentificare
    'Content-Type': 'application/json'
}