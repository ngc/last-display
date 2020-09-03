import os 
import json

payload = {
    'api_key': os.getenv("API_KEY"),
    'format': 'json',
    'method': 'user.getRecentTracks',
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
jprint(r.json())