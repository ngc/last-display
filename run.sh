#!/bin/bash
python3 -m http.server 8099 > /dev/null &
python3 main.py --user > /dev/null &
#chromium-browser --app="http://0.0.0.0:8989/__display__.html" &
