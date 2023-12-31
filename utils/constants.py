SCOPE = "user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position"
CLIENT_ID = 'YOUR CLIENT ID' #You can find it in the application dashboard
CLIENT_SECRET = 'YOUR CLIENT SECRET' #You can find it in the application dashboard
REDIRECT_URI = 'http://localhost:8080'
API = "https://api.spotify.com/v1"
USER_ID = "YOUR USER ID"


#Va fi inlocuit manual cu codul obtinut ruland fisierul "run_create_token.py"
ACCESS_TOKEN = "BQBQewNVmwgQaAEUGdSaXu_PIspapLxohBTrh1VLk0YK9HTPZMDAt0RbK_AOr15leLDIKB0WokkEHo8u6aQ3v74nl3UFcBKbcGdjlNe5ASBBXp4jp_sL9TDmQ8U02R4L28jfxwEtvhbDD_-O4HpxqXxxCChh2OifQZnDkqCd8HJYzYQUukBJTxJ84bkibt3eyI8CvpoZtMMQzoS64yPnhKqSBOskc13nciR6t6tWUTmib1lLFNgTBIFs3_iRVIKOjC2Pjfj0RdT7y0g0AUk-cNUBlQSzLQ"

HEADER = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    # reprezinta valoarea tokenului de autentificare
    'Content-Type': 'application/json'
}