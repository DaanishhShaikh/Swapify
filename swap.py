import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
client_id = 'f9e4dec8fe734648872cd4f2b1678de3'
client_secret = 'dd12ea188ce1487ba8880f198be49323'
redirect_uri = 'http://localhost:8888/callback'  # This should match the redirect URI you set in your Spotify Developer Dashboard
scope = 'playlist-modify-public'  # Adjust the scope as needed

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Get tracks from the old playlist
old_playlist_uri = 'https://open.spotify.com/playlist/1h40Sj5SIJ7TMrPFeWPpb5?si=2c16fab79cab4023'  # Replace with the correct playlist URI or ID

tracks = []
results = sp.playlist_tracks(old_playlist_uri)
tracks.extend(results['items'])

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Create a new playlist in the new account
new_playlist_name = 'Swweeettt'
new_playlist_description = 'Luvv is in the air!!!!'
new_playlist = sp.user_playlist_create('dabnishshaikhb', name=new_playlist_name, public=True, description=new_playlist_description)
new_playlist_id = new_playlist['id']

# Split the track URIs into batches of 100 and add them to the new playlist
track_uris = [track['track']['uri'] for track in tracks]
batch_size = 100
for i in range(0, len(track_uris), batch_size):
    sp.playlist_add_items(new_playlist_id, track_uris[i:i+batch_size])

print('Playlist transfer completed!')