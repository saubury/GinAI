import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from config_secrets import SPOTIFY



def play_song(searchString):
    username = SPOTIFY['username']
    token = get_token(username)
    spotifyObject = spotipy.Spotify(auth=token)

    track_id = spotifyObject.search(q=searchString, type='track', limit=1)
    trackResults = track_id['tracks']['items']
    trackSelectionList = []

    for trackItem in trackResults:
        # print("🔊 {} : Track 🎵 : {}  URI:{}".format(colored('Playing', 'red'), colored(trackItem['name'], 'green'), trackItem['uri']))
        print(f"🔊 Playing 🎵 : {trackItem['name']} ")
        trackSelectionList.append(trackItem['uri'])

    devices = spotifyObject.devices()
    deviceID = devices['devices'][0]['id']
    spotifyObject.start_playback(deviceID, None, trackSelectionList)


def get_token(username):
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'

    try:
        token = util.prompt_for_user_token(username=username, scope=scope, client_id=SPOTIFY['client_id'], client_secret=SPOTIFY['client_secret'], redirect_uri=SPOTIFY['redirect_uri'])
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
    return token


def findAndPlaySong(songRequest):
    splitRequest = songRequest.split(' by ')
    if (len(splitRequest)==1):
        # Title only serach
        searchString = 'track:{}'.format(splitRequest[0])
    else:
        # Title and Artist search
        searchString = 'artist:{} track:{}'.format(splitRequest[1], splitRequest[0])
    play_song(searchString)

if __name__ == '__main__':
    if len(sys.argv) == 2: 
        findAndPlaySong(sys.argv[1])
    else:
        print("Specify song to search for; eg \"Call Me by Carly Rae Jepsen\" or \"Don't Call Me Up\"")
        sys.exit(1)
