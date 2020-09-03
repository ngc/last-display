import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_current_track(user):
    """Queries last.fm for the most recently played track by a user,
       returns json object for track if it's playing. 
       returns None type if nothing is playing. """

    payload = {
        'api_key': os.environ.get("API_KEY"),
        'format': 'json',
        'method': 'user.getRecentTracks',
        'user': user,
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
    content = r.json()
    if(content["recenttracks"]['track'][0]['@attr']['nowplaying'] == 'true'):
        return content["recenttracks"]['track'][0]
    else:
        return None

def get_recent_track(user):
    """Queries last.fm for the most recent track played by a user and returns json object for track"""
    payload = {
        'api_key': os.environ.get("API_KEY"),
        'format': 'json',
        'method': 'user.getRecentTracks',
        'user': user,
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
    content = r.json()
    return content["recenttracks"]['track'][0]