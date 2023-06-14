# Swapify
Swapify is a Python script that allows you to transfer playlists from one Spotify account to another. It utilizes the Spotipy library for interacting with the Spotify Web API and provides a convenient way to transfer your favorite playlists between accounts.



## Features
- Authenticate with Spotify using the SpotifyOAuth flow.
- Retrieve tracks from a source playlist.
- Create a new playlist in the target Spotify account.
- Add tracks from the source playlist to the new playlist.



## Prerequisites
- Python 3.6 or above
- Spotipy library



## Installation
1. Clone the repository:
   ```
   git clone https://github.com/DaanishhShaikh/Swapify.git
   ```

2. Install the required dependencies:
   ```
   pip install spotipy
   ```


## Usage
Swapify can be used either via the command line interface (CLI) OR the graphical user interface (GUI).


### Command Line Interface (CLI)
1. Replace the following placeholders in the script with your Spotify Developer credentials:
   - `YOUR_CLIENT_ID`
   - `YOUR_CLIENT_SECRET`
   - `YOUR_REDIRECT_URI`

2. Update the `old_playlist_uri` variable with the correct source playlist URI or ID.
3. Run the script:
   ```
   python swapify.py
   ```
4. Follow the authentication flow in the console to authorize the script to access your Spotify account.
5. Once authenticated, the script will transfer the playlist to your desired account. Progress will be displayed in the console.
6. Enjoy your transferred playlist in the target Spotify account!



### Graphical User Interface (GUI)
1. Launch the GUI application by running the following command:
   ```
   python swapifyGUI.py
   ```
3. The GUI will prompt you to enter your Spotify Developer credentials:
   - Client ID
   - Client Secret
   - Redirect URI
4. Enter the required information:
   - Source playlist URI or ID
   - Target Spotify username
   - New playlist name and description
5. Click the "Transfer Playlists" button to initiate the playlist transfer process.
6. The GUI will display the progress of the transfer and provide a success message upon completion.
7. Access your transferred playlists in the target Spotify account.


## License
This project is licensed under the [MIT License](LICENSE).


## Acknowledgments
Spotipy - A lightweight Python library for the Spotify Web API.


## Contributing
Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Support
If you benefit from this please star the repository

Note: The CLI and GUI interfaces provide the same functionality. Choose the interface that best suits your preference and needs.
If you encounter any issues or have further questions, please refer to the documentation or reach out to the script's developer. Enjoy swapping your playlists with Swapify!
