while [ true ]
do
   sleep 4
    xdotool search --class xterm windowactivate --sync %1 key R windowactivate $(xdotool getactivewindow)
done
