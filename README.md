# Spotify Music Downloader

a python script that finds your saved songs on spotify and downloads them to your Home directory's Music Folder

## Dependecies
  * [ytmdl](https://github.com/deepjyoti30/ytmdl)
  * [python-dotenv](https://github.com/theskumar/python-dotenv)
  * [spotipy](https://github.com/plamere/spotipy) 

## Setup

you'll need to create a `.env` file with the following:

```
SPOTIPY_CLIENT_ID="your spotify app client id"
SPOTIPY_CLIENT_SECRET="your spotify app client secret"
SPOTIPY_REDIRECT_URI="a redirect uri that matches one in your spotify app"
```

run

```
python get-songs.py <SPOTIFY USERNAME>
```

to start downloading

## TODO
  * add a way to download playlists instead of your whole library
  * reformat search string so that it uses ytmdl --artist and --album arguments
  * check if song is already downloaded to your folder so that it skips duplicates e.g. if you need to start the script over again
  * add optional argument for specific folder
  * add way to make sure it only downloads songs without needing user input and not full ablums
