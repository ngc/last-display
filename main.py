import json
import requests
import argparse
import os
from time import sleep
from lastfmwrapper import lastfm
import sys
import urllib.request
from PIL import Image, ImageFilter
from stackblur import StackBlur

track_name = "Y*7i7"
track_artist = "Y*7i7"
album_name = "Y*7i7"

def generate_html(user):
    """Generates HTML as specified to be rendered"""

    global album_name
    global track_name
    global track_artist

    src = lastfm.get_recent_track(user)

    if(src['name'] != track_name or src['artist']['#text'] != track_artist):
        track_name = src['name']
        track_artist = src['artist']['#text']
        image_src = src['image'][3]['#text']
        image_src = src['image'][3]['#text']
        
        if(album_name != src['album']['#text']):
            """Updates album art if new album is detected"""
            urllib.request.urlretrieve(image_src, "__coverimg__.png")
            cover_img = Image.open("__coverimg__.png")
            background_img = cover_img.resize((1000, 1000), Image.ANTIALIAS)
            background_img = background_img.filter(StackBlur(20))
            background_img.save("__background_img__.png")
        album_name = src['album']['#text']

        with open('template.html', 'r') as file:
            raw_html = file.read().format(image_src, track_name, track_artist, (os.getcwd() + "/__display__.html"))

        f = open("__display__.html", "w")
        f.write(raw_html)
        f.close()

        return "NEW TRACK: {0} by {1}".format(track_name, track_artist)
    
    track_name = src['name']
    track_artist = src['artist']['#text']
    image_src = src['image'][3]['#text']

    return "CONTINUED PLAYING OF: {0} by {1}".format(track_name, track_artist)


"""Argument Parsing"""
parser = argparse.ArgumentParser(description="""Display information for a user's last.fm profile in the terminal""")
parser.add_argument('--user', metavar='username', type=str, nargs='?',
                help='specified last.fm user to get information from')
parser.add_argument('--feh', metavar='username', type=bool, nargs='?',
                help='Whether the image will be displayed by feh or not', 
                default=False)
args = parser.parse_args()

while True:
    try:
        if('--feh' in sys.argv):
            print(generate_feh(args.user))
        else:
            print(generate_html(args.user))
        sleep(2)
    except ValueError:
        print("ERROR: Track fetch Error, retrying...")