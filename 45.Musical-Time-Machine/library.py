import re

import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.util import prompt_for_user_token
from bs4 import BeautifulSoup

# Client ID and secret obtained from Spotify Developer Dashboard

# Spotify username and scope


# Obtain user token for authentication
username = '***'
scope = 'playlist-modify-private playlist-modify-public'

CLIENT_ID = "***"
CLIENT_SECRET = "***"
token = prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                              redirect_uri='http://localhost:8000/callback')
# Create Spotify object with user token
sp = spotipy.Spotify(auth=token)


def get_top100(date):
    titles = []
    link = "https://www.billboard.com/charts/hot-100/"
    data_at_date = requests.get(f"{link}{date}")
    data_at_date = data_at_date.text
    soup = BeautifulSoup(data_at_date, "html.parser")
    result = soup.findAll('h3', class_='a-no-trucate')

    for i in result:
        titles.append(i.getText(strip=True))
    titles = [title.replace('\n', '').replace('\t', '') for title in titles]
    return titles
def check_playlist(playlist_name):
    id = None
    playlists = sp.current_user_playlists(limit=50)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            id = playlist['id']
            break
    return id

def add_element_playlist(playlist_name, songs):
    id = None
    # Get list of user's playlists
    playlists = sp.current_user_playlists(limit=50)
    # Find the playlist with the desired name and return its ID
    id = check_playlist(playlist_name)
    if id is not None:
        # Add track to playlist
        playlist_id = id
        for song in songs:
            results = sp.search(song, limit=1)
            if results and results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=[track_uri])
                print(f"Added track :{song}\n")
            else:
                print(f"No track found for '{song}'")
    else:
        print(f"No playlist found with name '{playlist_name}'")


def create_playlist(name):
    playlist_name = name
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)
    return playlist_name
