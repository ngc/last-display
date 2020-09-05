#!/bin/bash
printf "Get your last.fm API key here https://www.last.fm/api/account/create..."
printf "Enter your last.fm API key: "
read API_KEY
clear
echo "export API_KEY='$API_KEY'" > lastfmwrapper/.env 
echo "Key loaded in lastfmwrapper/.env..."
echo "To run last.display, type ./run.sh USERNAME"
chmod +x run.sh