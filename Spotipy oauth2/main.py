import requests

from flask import Flask
app = Flask(__name__)
app.secret_key = 'fa9a2bdf463fcb30e49dfbe9a0d382f3'

CLIENT_ID = '7a805b18766647f8809cd01d57acff26'
CLIENT_SECRET = '7c470252e9004e03b0782b976b77df2f'
REDIRECT_URI = 'http://google.com/callback/'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return "Welcome to my Spotify App <a href='/login'>Login with Spotify</a>"

