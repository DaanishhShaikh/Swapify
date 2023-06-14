# Swapify - Playlist Transfer Script
# Created by Mohammed Danish Shaikh
# GitHub: https://github.com/DaanishhShaikh
# Date: 13/06/2023
# Feel free to reach out to me if you have any questions or suggestions!

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Obtaining Spotify Credentials:
#    - Visit the Spotify Developer Dashboard at [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) and log in with your Spotify account.
#    - Create a new application by clicking on the "Create an App" button.
#    - Provide a name and description for your app, you can enter any site as the website it can even be one of you social media, and agree to the terms of service.
#    - Once the app is created, you'll see your app's dashboard. Note down the **Client ID** and **Client Secret**.
#    - In the app's settings, add a redirect URI. This can be any valid URL (Use this if you dont know the technical aspects `http://localhost:8888/callback`).

# Set up authentication
client_id = ''
client_secret = ''
redirect_uri = 'http://localhost:8888/callback'  # This should match the redirect URI you set in your Spotify Developer Dashboard
scope = 'playlist-modify-public'  # Adjust the scope as needed public(RECOMMENDED)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Get tracks from the old playlist
old_playlist_uri = 'https://open.spotify.com/playlist/5ex7tZSAaqHCtDA79Qw9QW' # Replace with the correct playlist URI or ID

tracks = []
results = sp.playlist_tracks(old_playlist_uri)
tracks.extend(results['items'])

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Create a new playlist in the new account
new_playlist_name = 'Swapped Playlist'
new_playlist_description = 'Generated Using Swapify'
new_playlist = sp.user_playlist_create('YOUR_USERNAME', name=new_playlist_name, public=True, description=new_playlist_description) # make sure to replace it with your username
new_playlist_id = new_playlist['id']

# Split the track URIs into batches of 100 and add them to the new playlist
track_uris = [track['track']['uri'] for track in tracks]
batch_size = 100
for i in range(0, len(track_uris), batch_size):
    sp.playlist_add_items(new_playlist_id, track_uris[i:i+batch_size])

print('Playlist transfer completed!')
