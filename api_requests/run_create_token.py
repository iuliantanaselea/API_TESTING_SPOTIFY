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
authorization_link = "http://localhost:8080/?code=AQDzDVzkJ8vuAYSA8UEsou2M741R5MqqS_aaP5VmCupLi9pgnuwMbvSWOmnIQf7l8jeFvu-reXz0i5lBQluJepg5WZgnkgLffER15qrKm-1sWFWZkSOjoRcxESw1cAG1O5Ys2oC2hpv00cy64V_AghiW_4H0jCWShi56cgRWmZCkh0EV3AMJFo2SL6hT3uENvHTi4psZJGp4v3LbR16N6U2GNcoAbQRCANRmIARqR421XYbTl8cuJoVWcCF_rS5xZky4BGntNpsTZOhUZqgeHL-SBzBjftWd-FMadu_RbM3qt4NS3nqUdvwMpXEqmHG9mdevnMQRHw9rooqhqntXDJiGBWACDH-OPByJMv10Yegevbw3fBtAHB_8LPG6MLmZiSsj6_Q"
authorization_code = authorization_link.split("=")[1]

"""
4. Se ruleaza comanda de mai jos, urmand a inlocui apoi constanta ACCESS_TOKEN din fisierul 
"constants.py"cu noul cod de acces generat.
"""
pprint(request_access_token(authorization_code).json()['access_token'])

