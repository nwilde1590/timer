#!/bin/sh
#launcher.sh
sleep 2
/home/pi/Documents/timer.py &
sleep 45
/root/Dropbox-Uploader/dropbox_uploader.sh delete /timer.csv
/root/Dropbox-Uploader/dropbox_uploader.sh upload /root/timer.csv /
