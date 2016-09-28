import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
k=0

for i in range (32):
	        k = k+1
		print "step no."
		print k
		GPIO.output(8,1)
		GPIO.output(18,0)
		GPIO.output(22,0)
 		GPIO.output(23,0)
		time.sleep(0.006)

		GPIO.output(8,0)
		GPIO.output(18,1)
		GPIO.output(22,0)
		GPIO.output(23,0)
		time.sleep(0.006)

		GPIO.output(8,0)
		GPIO.output(18,0)
		GPIO.output(22,1)
		GPIO.output(23,0)
		time.sleep(0.006)

		GPIO.output(8,0)
		GPIO.output(18,0)
		GPIO.output(22,0)
		GPIO.output(23,1)
		time.sleep(0.006)
print "capturing image"
GPIO.cleanup()    
