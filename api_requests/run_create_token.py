from create_token import *
from constants import *

"""
1. Se ruleaza functia de mai jos, care returneaza un url ce trebuie accesat pentru a da 
permisiunea aplicatiei sa realizeze actiunile cuprinse in SCOPE
"""

# print(get_auth().url)
"""
2. Se acceseaza url-ul obtinut ruland functia de mai sus si se accepta termenii, urmand ca din url-ul generat dupa redirectionare sa copiem codul generat
"""

"""
3. Se inlocuieste in variabila authorization_code valoarea obtinuta urmand pasii de mai sus
"""
authorization_code = "AQAnP4QMHAoYfu9pZUQBHgMuGhVrdQ9S0W6ugtAe9fKBHIc4Vhgug_hLHhnzHA7Dv8xO3uFGYKCTgTQwZOk2k16iFPU5I_ueWmVAs3QjJs26cr5mLl57Yy8tc2m5_wnExLKt_AjYfw6cNhV4CJdfKWMnOuaNI0dzGL25nghPx4GZ5moh3RCj7BW7_F0lWvvottbd8ygh94-Xh-Nc3DPtDdooKlUUJu7U8jT_POUK2bKbcVyy0jVFAsQuZU1jBixqZuyrmCsPkiSiyxUr1naAJ-vZ_ZVio2XCATbrlD6imVNRlB52gKhsLB84eTBX2HxVBXQGvO1v18fsdUo1JrYgf0WNnP1wl6feUJ-5wBUnD8q8lCkwBoYItvG1Ire_0m4VLPc_GvY"

"""
4. Se ruleaza functia de mai jos, urmand a inlocui apoi constanta ACCESS_TOKEN din fisierul "constants.py"
cu noul cod de acces generat. 
"""
# pprint(request_access_token(authorization_code).json())
