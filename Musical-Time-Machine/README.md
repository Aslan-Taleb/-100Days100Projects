# Billboard Top 100 Playlist Generator

This Python script creates a Spotify playlist based on Billboard's Top 100 songs for a specific date. It uses the Spotify API and BeautifulSoup to retrieve song data and add it to a playlist.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your machine.
- Spotipy library installed (`pip install spotipy`).
- BeautifulSoup library installed (`pip install beautifulsoup4`).
- A Spotify Developer account with a client ID and secret.

## Usage Notes
The script will check if a playlist with the same name already exists in your Spotify account. If it does, it will skip playlist creation and offer options to continue with a new date or quit.

If a playlist with the specified name does not exist, the script will create a new playlist and add the top 100 songs for the chosen date.

## Acknowledgments

This script is for educational and informational purposes only.

Make sure to follow Spotify's terms of service and developer guidelines.

Use the script responsibly and at your own risk.