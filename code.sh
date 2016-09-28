#!/bin/bash

x=($(date +"%Y-%m-%d %H:%M:%S %s")) 

fswebcam -r 1280x720  --no-banner -S 15 --flip h --jpeg 95 --shadow --title "SLB Labs" --info "Monitor: Active @ 1 fpm" --save $x.jpg -q -l 60

