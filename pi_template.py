from RPi import GPIO
from firebase import firebase

token=None
url=None

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':20, 'red':21}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def setLED(ledno):
	if ledno = 'yellow':
		GPIO.output(20, GPIO.HIGH) # turn on the LED
    	GPIO.output(21, GPIO.LOW)
    elif ledno = 'red':
    	GPIO.output(21, GPIO.HIGH) # turn on the LED
    	GPIO.output(20, GPIO.LOW)
    else:
    	GPIO.output(21, GPIO.LOW) # turn on the LED
    	GPIO.output(20, GPIO.LOW)

	# you can use this to set the LED on or off
	pass

while True:
	ledno = firebase.get('/state')
	setLED(ledno)

