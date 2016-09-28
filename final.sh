DATE=($(date +" %H:%M:%S"))

for i in range {0..31}:
do
	cd /
	cd home/pi/Desktop
	sudo python stepper.py
	fswebcam -r 1280x720  --no-banner -S 15 --flip h --jpeg 95 --shadow --title "SLB Labs" --info "Monitor: Active @ 1 fpm" /home/pi/Desktop/$DATE.jpg -q -l 60
done
