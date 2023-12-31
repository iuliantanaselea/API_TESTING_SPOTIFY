"""
1. Se ruleaza comanda de mai jos, care returneaza un url ce trebuie accesat pentru a da
permisiunea aplicatiei sa realizeze actiunile cuprinse in SCOPE
"""
from pprint import pprint

from api_requests.create_token import *

# print(get_auth().url)
"""
2. Se acceseaza url-ul obtinut ruland comanda de mai sus si se accepta termenii, 
urmand ca din url-ul generat dupa redirectionare sa copiem codul generat
"""

"""
3. Se inlocuieste in variabila authorization_code valoarea obtinuta la pasul 2
"""
authorization_code = "AQBGvL2YLEkXA35jSE_g_OBlBuu4pzA50DNgWiQ_09_WHwXapHKKTZ4MSzYg6769M85YdEDmC2kn-hiZ35w-Ms3ENQ8FSxdH-Yi36IgqDb_oRzkkD6FdEKV_qDevnxY7-zhCkOqwdBwRC3w4DVE26OyZY-bUYhpVTn6p0RxW93fScoPiYWgPYunhHK9ukbqQ-xJxwhvlIBJaw4UD4Eu-dn_pJCZUscwF6UcemrbYcDxMrWbddAEYvWi6doL5mDwbYLIqn9XfnfG-zZUCs4mHNsEffmAjpb9r6UlTG5xRcgqcLyotmOLM8WOHvF878_GbL88l5v9t31TdbFoDVfZvGUOY5GeBLl7IY2oCkacLaYoW_qhexU_FOXhC58lNXMcwjgRKU-A"

"""
4. Se ruleaza comanda de mai jos, urmand a inlocui apoi constanta ACCESS_TOKEN din fisierul "constants.py"
cu noul cod de acces generat.
"""
# pprint(request_access_token(authorization_code).json())
