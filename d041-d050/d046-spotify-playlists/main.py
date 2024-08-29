# Spotify Playlist Creator

# Choose a date, get the top 100 billboard songs of that day, then
# create a playlist on Spotify with those songs.
#
# More practices about web scrapping, using APIs, and a new library
# (spotipy).

from etc.helpers import ask_input
import datetime as dt
import os
import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_REDIRECT_URL = 'http://example.com'
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_SCOPE = 'playlist-modify-private'

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/{date}/'


def valid_date(string: str) -> bool:
    try:
        dt.datetime.strptime(string, '%Y-%m-%d')

        return True
    except ValueError:
        return False


def get_list_of_songs(selected_date: str) -> list[str]:
    print(f'Finding top 100 songs of {selected_date}')
    url = BILLBOARD_URL.replace('{date}', selected_date)
    response = requests.get(url=url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    elements = soup.select(
        'div.chart-results-list div.o-chart-results-list-row-container '
        'ul.o-chart-results-list-row '
        'h3')

    return [element.get_text(strip=True) for element in elements]


def connect_spotify() -> spotipy.Spotify:
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        SPOTIFY_CLIENT_ID,
        SPOTIFY_CLIENT_SECRET,
        scope=SPOTIFY_SCOPE,
        redirect_uri=SPOTIFY_REDIRECT_URL))


def get_user_id(sp: spotipy.Spotify) -> str:
    return sp.current_user()['id']


def create_playlist(sp: spotipy.Spotify, selected_date: str) -> (str, str):
    playlist = sp.user_playlist_create(
        get_user_id(sp),
        name=f'TOP 100 songs of {selected_date}',
        public=False,
        description=f'The top 100 songs of {selected_date} according to Billboard.')

    return playlist['external_urls']['spotify'], playlist['id']


def find_song(sp: spotipy.Spotify, selected_song: str, selected_year: str) -> str | None:
    print(f'Looking info about {selected_song}')
    response = sp.search(
        f'track: {selected_song} year: {selected_year}',
        limit=10,
        offset=0,
        type='track',
        market=None)
    tracks = response['tracks']

    if tracks['total'] == 0:
        return None

    return tracks['items'][0]['uri']


def add_song_to_playlist(sp: spotipy.Spotify, playlist: str, selected_songs: list[str]) -> None:
    print('Creating playlist')
    sp.playlist_add_items(playlist, selected_songs)


sp_client = connect_spotify()
date = ask_input('Tell me an important date for you. [yyyy-mm-dd] ', valid_date)
year = date[:4]
songs = get_list_of_songs(date)

(playlist_url, playlist_id) = create_playlist(sp_client, date)
all_songs = []

for song in songs:
    song_uri = find_song(sp_client, song, year)

    if song_uri is not None:
        all_songs.append(song_uri)

if len(all_songs) > 0:
    add_song_to_playlist(sp_client, playlist_id, all_songs)

print(f'Complete, listen to the new playlist here: {playlist_url}')
