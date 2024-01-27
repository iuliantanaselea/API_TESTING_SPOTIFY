The scope of this application is to test the functionalities of Spotify API.
[Spotify Web API](https://developer.spotify.com/documentation/web-api)

### Prerequisites
To run the application, you need python 3.11, venv and pip to be installed.
1. python 3.11

You need to have Python installed, at least the version 3.11 . Check if you already have Python installed
running the Terminal command: ```python --version```. If the result shows a version number, Python is already
installed. If not, you can download it here: https://www.python.org/downloads/

2. pip

pip is the package manager for Python. It is used to install and update packages in a virtual environment.
Check if you have already pip installed running the Terminal command: ```pip --version```.
If the result shows a version number, pip is installed and there is no need for further actions. If not,
instructions for downloading the latest version of pip can be found here: https://pip.pypa.io/en/stable/cli/pip_download/

3. venv (Virtual Environment)

You need to create a virtual environment (venv) before running the application. For more information on
how you create one, follow this link:  https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

## Step 1 Create a Spotify account

This app relies on Spotify API. In order to use the app, you need to create
a Spotify developer account.
 
1. Visit the [Spotify for developers portal](https://developer.spotify.com/). 
 Access the "Log in" section. If you already have an account, enter your authentication credentials.
 If not, click "Sign up for Spotify" and follow the steps to create an account. After you've logged in or
 signed up, access the [account dashboard](https://developer.spotify.com/dashboard).

2. Click the "Create App" button. Enter your new app name and description, 
fill the "REDIRECT URIs" field with "http://localhost:8080", accept the Terms and Conditions and click "Save".

3. Click the "Settings" button. Underneath the Client ID field, you'll see a "View client secret" link.
Click that link to reveal your Client Secret. Copy both Client ID and Client Secret values in your computer.
because you will need them later when initializing the application.

4. Access the [Edit profile](https://www.spotify.com/ro-ro/account/profile/) section on [Spotify](https://www.spotify.com/ro-ro/account/overview/) and 
copy the _Username_ 

## Step 2 Installation and Setup

I. Create a folder in your computer where you'd like to store the code to run the app.

II. The libraries used are requests (version 2.31), pytest (version 7.4.3), pytest-html (version 4.1.1). 
To install them, run the Terminal command:
```commandline
pip install -r requirements.txt
```
III. In _constants.py_ file, replace your _CLIENT_ID, CLIENT_SECRET_ values with the ones obtained in step 1.3 .
Replace the _USER_ID_ value with the one copied at step 1.4 :

```
# SCOPE determines what  permisions the user has
SCOPE = "user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position"

# CLIENT_ID = 'YOUR CLIENT ID' # You can find it in the application dashboard

# CLIENT_SECRET = 'YOUR CLIENT SECRET' # You can find it in the application dashboard

REDIRECT_URI = 'http://localhost:8080'
API = "https://api.spotify.com/v1"

# USER_ID = "YOUR USER ID"


# Will be modified manually with the code obtained running the "run_create_token.py" file
ACCESS_TOKEN = "YOUR_GENERATED_ACCESS_TOKEN
```


## Step 3 Authentication

Spotify relies on OAuth2 (Open Authorization) standard for authentication and authorization.

To obtain the access token, you need to run the _run_create_token.py_ file and follow the steps described.

1. Run the command below, which returns a URL that needs to be accessed to grant the application the
permission to run the actions listed in SCOPE. After accessing the link, comment back the command.
```commandline
print(get_auth().url)
```

2. Access the URL obtained running the command above and accept the terms. You will be redirected to a URL which you
need to copy

3. Replace the value in the _authorization_code_ variable with the code obtained above

4. Run the command below and copy the generated code in the constant ACCESS_TOKEN from the "constants.py" file

```commandline
pprint(request_access_token(authorization_code).json()['access_token'])
```

:bangbang: **The generated token is available for 60 minutes. After the time expires, you need to 
follow again the steps from Authentication chapter**

For more information you can follow the following URLs:

1. Spotify API authorization guide: https://developer.spotify.com/documentation/web-api/concepts/authorization

2. Google OAuth2 authorization standard: https://pkg.go.dev/golang.org/x/oauth2/google

## Step 4 Running the tests

The tests can be found in the _tests_ folder.
To run any test, you can run the corresponding file.

For example, in the _test_albums_api.py_ file, you can run the tests suite pressing the green triangle
found to the left of the _TestAlbumsAPI_ class. 
If you want to run only one test, press the green triangle found to the left of the function which 
describes the desired test, for example the function _test_get_album()_

![test_albums_api](https://raw.githubusercontent.com/iuliantanaselea/API_TESTING_SPOTIFY/02d5e390184d3148c27e42f5c065f39696ff8ac2/assets/test_albums_api.png)

## Step 5 Generating the report

To generate the report, run the Terminal command:
```commandline
pytest --html=report.html
```
An HTML file will be created in the project main directory, which can be opened with any browser.
