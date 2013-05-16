#!/bin/bash
#script to download today's NASA Astronomy Picture of the Day and set it as the wallpaper

cd ~/nasapics;
wget -N http://apod.nasa.gov/apod/astropix.html;
wget -N -O todaysImage.jpg http://apod.nasa.gov/apod/$(grep -o "image.*\.jpg" astropix.html | head -n1);
osascript -e 'tell application "Finder" to set desktop picture to "Hard Drive:Users:Charles:nasapics:todaysImage.jpg" as alias';
killall Dock;