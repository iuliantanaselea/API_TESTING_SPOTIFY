"""
1. Run the command below, which returns a URL that needs to be accessed to grant the application the
permission to run the actions listed in the scope list
"""
from pprint import pprint

from api_requests.create_token import *

# print(get_auth().url)
"""
2. Access the URL obtained running the command above and accept the terms. From the URL address 
obtained, copy the generated code
"""

"""
3. Replace the value of the authorization_code variable with the code obtained above
"""
authorization_code = "AQBGvL2YLEkXA35jSE_g_OBlBuu4pzA50DNgWiQ_09_WHwXapHKKTZ4MSzYg6769M85YdEDmC2kn-hiZ35w-Ms3ENQ8FSxdH-Yi36IgqDb_oRzkkD6FdEKV_qDevnxY7-zhCkOqwdBwRC3w4DVE26OyZY-bUYhpVTn6p0RxW93fScoPiYWgPYunhHK9ukbqQ-xJxwhvlIBJaw4UD4Eu-dn_pJCZUscwF6UcemrbYcDxMrWbddAEYvWi6doL5mDwbYLIqn9XfnfG-zZUCs4mHNsEffmAjpb9r6UlTG5xRcgqcLyotmOLM8WOHvF878_GbL88l5v9t31TdbFoDVfZvGUOY5GeBLl7IY2oCkacLaYoW_qhexU_FOXhC58lNXMcwjgRKU-A"

"""
4. Run the command below and copy the generated code in the constant ACCESS_TOKEN from the "constants.py" file
"""
# pprint(request_access_token(authorization_code).json())
