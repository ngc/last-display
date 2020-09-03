import json
import requests
import argparse
import os
from time import sleep
from lastfmwrapper import lastfm
import sys
import urllib.request
from PIL import Image, ImageFilter
rounds = 0
"""Generates HTML as specified to be rendered by w3m in the terminal"""
def generate_html(user):
    global rounds
    rounds += 1

    src = lastfm.get_recent_track(user)
    image_src = src['image'][3]['#text']
    urllib.request.urlretrieve(image_src, "__coverimg__.png")
    cover_img = Image.open("__coverimg__.png")
    background_img = cover_img.resize((1000, 1000), Image.ANTIALIAS)
    background_img = background_img.filter(ImageFilter.GaussianBlur(10))
    background_img.save("__background_img__.png")

    track_name = src['name']
    track_artist = src['artist']['#text']
    image_src = src['image'][3]['#text']

    with open('template.html', 'r') as file:
        raw_html = file.read().format(image_src, track_name, track_artist, (os.getcwd() + "/__display__.html"), rounds)

    f = open("__display__.html", "w")
    f.write(raw_html)
    f.close()

"""Argument Parsing"""
parser = argparse.ArgumentParser(description="""Display information for a user's last.fm profile in the terminal""")
parser.add_argument('--user', metavar='username', type=str, nargs='?',
                help='specified last.fm user to get information from')
parser.add_argument('--feh', metavar='username', type=bool, nargs='?',
                help='Whether the image will be displayed by feh or not', 
                default=False)
args = parser.parse_args()

while True:
    sleep(5)
    if('--feh' in sys.argv):
        generate_feh(args.user)
    else:
        generate_html(args.user)