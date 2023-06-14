import tkinter as tk
from tkinter import messagebox
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

def open_github_profile():
    webbrowser.open_new_tab('https://github.com/DaanishhShaikh')

def set_placeholder(entry, placeholder_text):
    # Set the placeholder text and color
    entry.insert(0, placeholder_text)
    entry.config(bg='light grey')

    # Bind the Entry widget to handle focus events
    entry.bind('<FocusIn>', lambda event: handle_focus_in(entry, placeholder_text))
    entry.bind('<FocusOut>', lambda event: handle_focus_out(entry, placeholder_text))

def handle_focus_in(entry, placeholder_text):
    # Clear the entry and set the text color to black
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def handle_focus_out(entry, placeholder_text):
    # Restore the placeholder text and color if the entry is empty
    if entry.get() == '':
        entry.insert(0, placeholder_text)
        entry.config(fg='black')

def transfer_playlists():
    # Retrieve user inputs
    client_id = client_id_entry.get()
    client_secret = client_secret_entry.get()
    redirect_uri = redirect_uri_entry.get()
    old_playlist_id = old_playlist_id_entry.get()
    new_playlist_name = new_playlist_name_entry.get()
    new_playlist_description = new_playlist_description_entry.get()
    user_id = user_id_entry.get()

    # Set up authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri))

    # Retrieve tracks from the old playlist
    tracks = []
    results = sp.playlist_tracks(old_playlist_id)
    tracks.extend(results['items'])

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # Create a new playlist in the user's account
    new_playlist = sp.user_playlist_create(user_id, name=new_playlist_name,
                                           public=True, description=new_playlist_description)
    new_playlist_id = new_playlist['id']

    # Add tracks to the new playlist in batches
    track_uris = [track['track']['uri'] for track in tracks]
    batch_size = 100
    for i in range(0, len(track_uris), batch_size):
        sp.playlist_add_items(new_playlist_id, track_uris[i:i+batch_size])

    messagebox.showinfo('Playlist Transfer', 'Playlist transfer completed!')

# Create the main window
window = tk.Tk()
window.title('Playlist Transfer')
window.geometry('400x450')
window.resizable(False, False)

# Set the background color to black
window.configure(bg='black')

# Create labels and entry fields for user input
tk.Label(window, text='Spotify Credentials', font=('Arial', 14, 'bold'), bg='black', fg='green', anchor='w').grid(row=0, columnspan=2, pady=10, padx=10, sticky='w')

client_id_label = tk.Label(window, text='Client ID:', bg='black', fg='white', anchor='w')
client_id_label.grid(row=1, column=0, pady=5, padx=10, sticky='w')
client_id_entry = tk.Entry(window, width=30)
client_id_entry.grid(row=1, column=1, pady=5, padx=10, sticky='w')
set_placeholder(client_id_entry, 'Enter Client ID')

client_secret_label = tk.Label(window, text='Client Secret:', bg='black', fg='white', anchor='w')
client_secret_label.grid(row=2, column=0, pady=5, padx=10, sticky='w')
client_secret_entry = tk.Entry(window, width=30)
client_secret_entry.grid(row=2, column=1, pady=5, padx=10, sticky='w')
set_placeholder(client_secret_entry, 'Enter Client Secret')

redirect_uri_label = tk.Label(window, text='Redirect URI:', bg='black', fg='white', anchor='w')
redirect_uri_label.grid(row=3, column=0, pady=5, padx=10, sticky='w')
redirect_uri_entry = tk.Entry(window, width=30)
redirect_uri_entry.grid(row=3, column=1, pady=5, padx=10, sticky='w')
set_placeholder(redirect_uri_entry, 'Enter Redirect URI')

tk.Label(window, text='Playlist Details', font=('Arial', 14, 'bold'), bg='black', fg='green', anchor='w').grid(row=4, columnspan=2, pady=10, padx=10, sticky='w')

old_playlist_id_label = tk.Label(window, text='Old Playlist ID:', bg='black', fg='white', anchor='w')
old_playlist_id_label.grid(row=5, column=0, pady=5, padx=10, sticky='w')
old_playlist_id_entry = tk.Entry(window, width=30)
old_playlist_id_entry.grid(row=5, column=1, pady=5, padx=10, sticky='w')
set_placeholder(old_playlist_id_entry, 'Enter Old Playlist ID')

new_playlist_name_label = tk.Label(window, text='New Playlist Name:', bg='black', fg='white', anchor='w')
new_playlist_name_label.grid(row=6, column=0, pady=5, padx=10, sticky='w')
new_playlist_name_entry = tk.Entry(window, width=30)
new_playlist_name_entry.grid(row=6, column=1, pady=5, padx=10, sticky='w')
set_placeholder(new_playlist_name_entry, 'Enter New Playlist Name')

new_playlist_description_label = tk.Label(window, text='New Playlist Description:', bg='black', fg='white', anchor='w')
new_playlist_description_label.grid(row=7, column=0, pady=5, padx=10, sticky='w')
new_playlist_description_entry = tk.Entry(window, width=30)
new_playlist_description_entry.grid(row=7, column=1, pady=5, padx=10, sticky='w')
set_placeholder(new_playlist_description_entry, 'Enter New Playlist Description')

user_id_label = tk.Label(window, text='Username:', bg='black', fg='white', anchor='w')
user_id_label.grid(row=8, column=0, pady=5, padx=10, sticky='w')
user_id_entry = tk.Entry(window, width=30)
user_id_entry.grid(row=8, column=1, pady=5, padx=10, sticky='w')
set_placeholder(user_id_entry, 'Enter Username')

# Create the transfer button with green background
transfer_button = tk.Button(window, text='Transfer Playlists', command=transfer_playlists, bg='green', fg='white', width=25)
transfer_button.grid(row=9, columnspan=2, pady=20, padx=10, sticky='n')

made_with_love_button = tk.Button(window, text='Made with ❤', command=open_github_profile, bg= 'green', fg= 'white')
made_with_love_button.grid(row=10, columnspan=2, pady=10, padx=10, sticky='n')

# Run the GUI
window.mainloop()

