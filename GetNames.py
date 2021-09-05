import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd
import json

with open('SpotPD/spotifyClientID.json') as file:
    data = json.load(file)

ClientID = data['ClientID']
ClientSecret = data['ClientSecret']

client_credentials_manager = SpotifyClientCredentials(ClientID,
        ClientSecret)

sp = \
    spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def call_playlist(creator, playlist_id):

    playlist_features_list = ['track_name']
    playlist_df = pd.DataFrame(columns=playlist_features_list)

    playlist = sp.user_playlist_tracks(creator, playlist_id)['items']
    playlist_features = []
    for track in playlist:

        playlist_features.append(track['track']['name'] + ' '
                                 + track['track']['artists'][0]['name'])

    return playlist_features
