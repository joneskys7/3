#!/bin/bash

DATE=($(date +" %H:%M:%S"))

fswebcam -r 1280x720  --no-banner /home/pi/Desktop/3dscanner/$DATE.jpg
