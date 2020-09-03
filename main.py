import json
import requests
import argparse
import os
from time import sleep
from lastfmwrapper import lastfm

"""Generates HTML as specified to be rendered by w3m in the terminal"""
def generate_html(user):
    src = lastfm.get_recent_track(user)
    track_name = src['name']
    track_artist = src['artist']['#text']
    image_src = src['image'][3]['#text']

    raw_html = """
    <html>
    <head>
    </head>
    <body>
    <br>
    <img src="{0}">
    <br>
    Now Playing: {2} | {1}
    </body>
    </html>
    """.format(image_src, track_name, track_artist, os.getcwd() + "/__display__.html")
    f = open("__display__.html", "w")
    f.write(raw_html)
    f.close()

"""Argument Parsing"""
parser = argparse.ArgumentParser(description="""Display information for a user's last.fm profile in the terminal""")
parser.add_argument('--user', metavar='username', type=str, nargs='?',
                help='specified last.fm user to get information from')
args = parser.parse_args()

while True:
    sleep(5)
    generate_html(args.user)