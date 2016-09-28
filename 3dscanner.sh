

for i in range {0..31}:
do
	cd /
	cd home/pi/Desktop
	sudo python stepper.py
	./camera.sh
done
