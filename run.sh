#!/bin/bash

while true
do
    ( cmdpid=$BASHPID; (sleep 60; kill $cmdpid) & exec w3m __display__.html )
done

