#!/bin/bash
: ${1?"Usage: USERNAME Needed"}
nohup python3.8 main.py --user $1 > /dev/null &
if chromium-browser --help > /dev/null; then
    chromium-browser --app="http://0.0.0.0:8099/__display__.html" > /dev/null &
else
    chromium --app="http://0.0.0.0:8099/__display__.html" > /dev/null &
fi

