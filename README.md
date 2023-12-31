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

 I. Viziteaza site-ul [Spotify for developers](https://developer.spotify.com/). 
 Acceseaza sectiunea "Log in". Daca ai un cont, introdu datele de autentificare. 
 Daca nu, acceseaza sectiunea "Inregistreaza-te la Spotify" si urmeaza pasii necesari
 pentru a crea un cont. Dupa logare sau inregistrare, acceseaza [panoul
 de comanda al contului](https://developer.spotify.com/dashboard).

II. Apasa pe butonul "Create App". Seteaza numele si descrierea noii aplicatii, 
completeaza campul "REDIRECT URIs" cu valoarea "http://localhost:8080", accepta
Termenii si Conditiile si apasa butonul "Save"

III. Apasa pe butonul "Settings". Sub campul Client ID, va fi afisat un link cu textul 
"View client secret". Apasa pe acesta pentru a afisa campul Client Secret. Copiaza 
informatiile din campurile Client ID si Client Secret in calculator, deoarece va fi nevoie
de ele la initializarea aplicatiei.

## Pasul 2 Instalarea si initializarea aplicatiei 

I. Creaza un folder in calculator, unde doresti sa salvezi codul pentru rularea aplicatiei.

II. Instaleaza pachetele Python necesare ruland in Terminal comanda: 
```commandline
pip install -r requirements.txt
```
III. In fisierul _constants.py_, inlocuieste 