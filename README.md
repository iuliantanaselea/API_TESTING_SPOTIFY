Acest program are rolul de a testa functionalitatile API-ului Spotify.

[Spotify Web API](https://developer.spotify.com/documentation/web-api)

### Prerechizite
Pentru rularea programului, este necesar ca python 3.11, venv si pip sa fie instalate.
1. python 3.11

Este necesar ca versiunea de python instalata sa fie cel putin 3.11 . Poti verifica daca ai Python
instalat ruland in Terminal comanda: ```python --version```. Daca rezultatul afiseaza o versiune, Python este deja instalat. 
Daca nu vezi o versiune afisata, sau este o versiune anterioara, poti descarca versiunea necesara urmarind link-ul urmator:  https://www.python.org/downloads/
2. pip

pip este managerul de pachete Python de referință. Este folosit pentru a instala și actualiza pachete într-un mediu virtual.

Poti verifica daca ai pachetul pip instalat ruland in Terminal comanda: ```pip --version```.
Daca rezultatul afiseaza o versiune, pachetul pip este deja instalat si nu sunt necesare
alte actiuni. Daca nu este instalat, instructiuni pentru instalarea pachetului pot fi gasite
urmarind link-ul urmator: https://pip.pypa.io/en/stable/cli/pip_download/

3. venv (Virtual Environment)

Este necesara crearea unui mediu virtual (venv) in prealabil. Pentru informatii despre cum 
poate fi creat unul, instructiunile pot fi gasite urmarind link-ul urmator: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment


## Pasul 1 Crearea unui cont Spotify

Acest program se bazeaza pe API-ul Spotify. Pentru a putea folosi programul, 
este necesara crearea unui cont de dezvoltator pe Spotify.

 
1. Viziteaza site-ul [Spotify for developers](https://developer.spotify.com/). 
 Acceseaza sectiunea "Log in". Daca ai un cont, introdu datele de autentificare. 
 Daca nu, acceseaza sectiunea "Inregistreaza-te la Spotify" si urmeaza pasii necesari
 pentru a crea un cont. Dupa logare sau inregistrare, acceseaza [panoul
 de comanda al contului](https://developer.spotify.com/dashboard).

2. Apasa pe butonul "Create App". Seteaza numele si descrierea noii aplicatii, 
completeaza campul "REDIRECT URIs" cu valoarea "http://localhost:8080", accepta
Termenii si Conditiile si apasa butonul "Save"

3. Apasa pe butonul "Settings". Sub campul Client ID, va fi afisat un link cu textul 
"View client secret". Apasa pe acesta pentru a afisa campul Client Secret. Copiaza 
informatiile din campurile Client ID si Client Secret in calculator, deoarece va fi nevoie
de ele la initializarea aplicatiei.

4. Acceseaza sectiunea [Editeaza profilul](https://www.spotify.com/ro-ro/account/profile/)
pe site-ul [Spotify](https://www.spotify.com/ro-ro/account/overview/) si copiaza 
sirul de caractere din campul _Nume utilizator_ 

## Pasul 2 Instalarea si initializarea aplicatiei 

I. Creaza un folder in calculator, unde doresti sa salvezi codul pentru rularea aplicatiei.

II. Instaleaza pachetele Python necesare ruland in Terminal comanda: 
```commandline
pip install -r requirements.txt
```
III. In fisierul _constants.py_, inlocuieste valorile din constantele 
_CLIENT_ID, CLIENT_SECRET_ cu cele obtinute la pasul 1.3 si valoarea din
constanta _USER_ID_ cu cea copiata la pasul 1.4 :

```
# SCOPE determina ce permisiuni are utilizatorul
SCOPE = "user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position"

# CLIENT_ID = 'YOUR CLIENT ID' #Valoarea se gaseste in panoul de comanda al aplicatiei Spotify

# CLIENT_SECRET = 'YOUR CLIENT SECRET' #Valoarea se gaseste in panoul de comanda al aplicatiei Spotify

REDIRECT_URI = 'http://localhost:8080'
API = "https://api.spotify.com/v1"

# USER_ID = "YOUR USER ID"


#Va fi inlocuit manual cu codul obtinut ruland fisierul "run_create_token.py"
ACCESS_TOKEN = "YOUR_GENERATED_ACCESS_TOKEN
```


## Pasul 3 Autentificarea

Spotify utilizeaza standardul OAuth2 (Open Authorization) pentru autentificare si 
autorizare

Pentru a obtine tokenul de acces, este necesara rularea fisierului
_run_create_token.py_ si urmarirea pasilor descrisi in el.

1. Se ruleaza comanda de mai jos, care returneaza un url ce trebuie accesat pentru a da
permisiunea aplicatiei sa realizeze actiunile cuprinse in SCOPE. Dupa accesarea link-ului,
se comenteaza la loc comanda.
```commandline
print(get_auth().url)
```

2. Se acceseaza url-ul obtinut ruland comanda de mai sus si se accepta termenii. Apoi, vei fi redirectionat
catre o pagina cu eroarea 404. Copiaza url-ul generat dupa redirectionare.

3. Se inlocuieste in variabila authorization_link url-ul copiat la pasul anterior

4. Se ruleaza comanda de mai jos, urmand a inlocui apoi constanta ACCESS_TOKEN din fisierul 
_constants.py_ cu noul cod de acces generat.
```commandline
pprint(request_access_token(authorization_code).json()['access_token'])
```

:bangbang: Token-ul generat este valabil pentru 60 de minute. Dupa expirarea timpului, este necesar sa
fie reluati pasii de la capitolul Autentificare.

Pentru mai multe informatii poti accesa link-urile urmatoare:

1. Ghidul de autorizare Spotify API: https://developer.spotify.com/documentation/web-api/concepts/authorization

2. Standardul de autorizare Google OAuth2: https://pkg.go.dev/golang.org/x/oauth2/google

## Pasul 4 Rularea testelor

Testele pot fi gasite in folderul _tests_.
Pentru rularea oricarui test, se poate rula fisierul corespunzator.

De exemplu, in fisierul _test_albums_api.py_ se pot rula toate testele apasand pe 
triunghiul verde din dreptul clasei _TestAlbumsAPI_.
Daca se doreste rularea unui singur test, se apasa triunghiul verde din dreptul functiei 
care descrie testul dorit, de exemplu functia _test_get_album()_

![test_albums_api](https://raw.githubusercontent.com/iuliantanaselea/API_TESTING_SPOTIFY/02d5e390184d3148c27e42f5c065f39696ff8ac2/assets/test_albums_api.png)

## Pasul 5 Realizarea raportului

Pentru realizarea raportului este necesara rularea din Terminal a comenzii:
```commandline
pytest --html=report.html
```
Astfel, va fi generat un fisier html in directorul principal al proiectului, care
poate fi deschis cu orice browser.
