from pprint import pprint
from api_requests.create_token import *
"""
1. Se ruleaza comanda de mai jos, care returneaza un url ce trebuie accesat pentru a da
permisiunea aplicatiei sa realizeze actiunile cuprinse in SCOPE. Dupa accesarea link-ului,
se comenteaza la loc comanda.
"""

# print(get_auth().url)
"""
2. Se acceseaza url-ul obtinut ruland comanda de mai sus si se accepta termenii. Apoi, vei fi redirectionat
catre o pagina cu eroarea 404. Copiaza url-ul generat dupa redirectionare.
"""

"""
3. Se inlocuieste in variabila authorization_link url-ul copiat la pasul anterior
"""
authorization_link = "http://localhost:8080/?code=AQCgvupIutnYwLSNn39b1P7LI6F6WDv14LJ7y9uL_aeNny7EUGdR8KnDbBwW3u_Bg6YZxfeSUKFDO5OcpDsy2P1SXP4tKEg9bYU_X2kS5Yj5rFu6DwdhtSvaN-qDnLmy8_7NewAVLBcdNJGKd67-T0pskrjBSIVx9ozaHeNUoMtNrn1Dg7is0b6w1cNVEqdD9KUc1KWZKRTrxonSpLlbvLHM_-OfeGhOG1fgmMrPuUqTmrm6lCjd74r6npRT9YRbuePdRao8q1ve_ZQ08EB-rlC-n3dIJt1aWiQxDouNp3GjA5LHKLS75EQBLpjTnN7pJh5hOMttHc6rO4GVHhQ2Y_9TeG511wtFNLT_mGg_5Eztp3aJkpPTfc8SzusdEfXhkqzKurs"

authorization_code = authorization_link.split("=")[1]

"""
4. Se ruleaza comanda de mai jos, urmand a inlocui apoi constanta ACCESS_TOKEN din fisierul 
"constants.py"cu noul cod de acces generat.
"""
pprint(request_access_token(authorization_code).json()['access_token'])

