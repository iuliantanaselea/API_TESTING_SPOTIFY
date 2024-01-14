# SCOPE determines what  permisions the user has
SCOPE = "user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position"
CLIENT_ID = 'YOUR CLIENT ID' # You can find it in the application dashboard
CLIENT_SECRET = 'YOUR CLIENT SECRET' # You can find it in the application dashboard
REDIRECT_URI = 'http://localhost:8080'
API = "https://api.spotify.com/v1"
USER_ID = "YOUR USER ID"


# Will be modified manually with the code obtained running the "run_create_token.py" file
ACCESS_TOKEN = 'BQAqCjhuuvCJYMhQSWAJ_eDqoRMqJBEej-UlY1XmIAqu2UkfeyJhFoh-qUAXxh4erYEyPGCrgyrl4OF4aK_b560tG1Up_O0RB6p1P9pbkEoZ19LUFt2LE7iUdzeBEPCRnOPUJnPVU8YUt5NFGWxGdEBoX8OTqTiOT0FGkH7Du5lg36vylSds1tzjITF0IGpw8cEfzz7jl2Z9TpnEnWFf7fGKWyJdVVij7DOHbH_5BCcOoP3rUB2v-YDreKh70ieC88ZNbfGbRg08sCy0ep7wuKEooxTCTwnRWKuUq-ogstM'

HEADER = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    # Represents the value of the authentication token
    'Content-Type': 'application/json'
}