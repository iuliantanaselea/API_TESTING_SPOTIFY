from pprint import pprint
from api_requests.create_token import *
"""
1. Run the command below, which returns a URL that needs to be accessed to grant the application the permission 
to run the actions listed in SCOPE. After accessing the link, comment back the command.
"""

# print(get_auth().url)
"""
2. Access the URL obtained running the command above and accept the terms.
You will be redirected to a URL which you need to copy
"""

"""
3. Replace the value in the _authorization_code_ variable with the code obtained above
"""
authorization_link = "http://localhost:8080/?code=AQDzDVzkJ8vuAYSA8UEsou2M741R5MqqS_aaP5VmCupLi9pgnuwMbvSWOmnIQf7l8jeFvu-reXz0i5lBQluJepg5WZgnkgLffER15qrKm-1sWFWZkSOjoRcxESw1cAG1O5Ys2oC2hpv00cy64V_AghiW_4H0jCWShi56cgRWmZCkh0EV3AMJFo2SL6hT3uENvHTi4psZJGp4v3LbR16N6U2GNcoAbQRCANRmIARqR421XYbTl8cuJoVWcCF_rS5xZky4BGntNpsTZOhUZqgeHL-SBzBjftWd-FMadu_RbM3qt4NS3nqUdvwMpXEqmHG9mdevnMQRHw9rooqhqntXDJiGBWACDH-OPByJMv10Yegevbw3fBtAHB_8LPG6MLmZiSsj6_Q"
authorization_code = authorization_link.split("=")[1]

"""
4. Run the command below and copy the generated code in the constant ACCESS_TOKEN from the "constants.py" file.

"""
pprint(request_access_token(authorization_code).json()['access_token'])

