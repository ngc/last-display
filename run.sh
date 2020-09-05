#!/bin/bash
nohup python3 main.py --user $1 > /dev/null &
chromium-browser --app="http://0.0.0.0:8099/__display__.html" > /dev/null &
