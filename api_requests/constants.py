SCOPE = "user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position"
CLIENT_ID = '----' #Se gaseste in setarile din aplicatia creata
CLIENT_SECRET = '---' #Se gaseste in setarile din aplicatia creata
REDIRECT_URI = 'http://localhost:8080'
API = "https://api.spotify.com/v1"

# Se va modifica manual cu codul obtinut ruland fisierul "run_create_token.py"
ACCESS_TOKEN = "BQCe-xb23xmf1YPibAWK5UAEyuQFWOuTM2GWO14ZrGPOopHKHOMjC5tnsy154VSwn43RJipuLZ4ja_pJSAtue9EJS1M6UtDjRe2detXa4k6PjItdHt5tJZELTheFbMNyys34PO0s2C1rnMr5RUEYfv9pxB223PvSMqm5pU-a0qtpbxZ91P-a_s8ET3SVJmlzZZi2Znn_pkYPPYLUNrczKX_IHREqmGfWjL38ZjSdl_gJltfBabXiNLFzC1FYad0XxaXNliJcBMow3ydHkBnKMr7vUmwZXQ"

HEADER = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    # reprezinta valoarea token-ului de autentificare, Client secret
    'Content-Type': 'application/json'
}