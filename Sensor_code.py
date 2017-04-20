import RPi.GPIO as GPIO
import time
from firebase import firebase
from datetime import datetime
from threading import Timer
import thread
import threading

time.sleep(15) #since we make the code run on startup, we need to give the R-Pi time to connect to the internet

GPIO.setmode(GPIO.BCM) #use BCM mode for the GPIO inputs
TRIG = 4 #defin trig and echo pins for the Ultrasound sensor
ECHO = 5
url = "https://iot-dw-1d-2017.firebaseio.com/"  # URL to Firebase database
token = "0lYSxo2k1Jrr3i3rxhyb3IFy3kTKEAsXP39n3mpV"  # unique token used for authentication
duration = 300 #run the code for 5 minutes (scaled down from the usual 3 hours)


# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)
List_Readings = {'Infrared':0, 'Methane':0,'Ultrasound':0} #dictionary to update firebase

def cleanup(): #code run after the script ends
    print 'Cleaning up'
    #firebase.put('/', 'Infrared', '')
    #firebase.put('/', 'Ultrasound', '')
    #firebase.put('/', 'Methane', '')
    List_Readings = {'Infrared':0, 'Methane':0, 'Ultrasound':0}


def infrared(arg1,stop_event):
    #print 'infrared'
    GPIO.setwarnings(False) #remove warning messages

    GPIO.setup(23, GPIO.IN) #Read output from infrared sensor
    #GPIO.setup(23, GPIO.OUT)#LED output pin
    count = 0
    output = []
    while ( not stop_event.is_set()):
       i=GPIO.input(23)
       if count >= 5:
              output.append('Infrared alert!') #if infrared sensor is blocked for 5 seconds or more, an alert will be sent to firebase
             # print output
              List_Readings['Infrared'] = output[-1]
              #print output[-1]
              firebase.put('/','BinA',List_Readings) #add the alert to firebase
              #break
       elif i==0:                 #When output from motion sensor is LOW
             #print "No motion"
 #            GPIO.output(23, 0)  #Turn OFF LED
             count+=1
            # print count
             time.sleep(1)
             output.append(count)
            # print output
             
       elif i==1:               #When output from motion sensor is HIGH
           #  print "Motion detected"
  #           GPIO.output(23, 1)  #Turn ON LED
             time.sleep(1)
             count = 0
             output.append(count)
             #print output

def ultrasound(arg1,stop_event):
    # print 'Distance measurement in progress'
    print 'ultrasound runs eh'
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    # print 'Waiting for sensor to settle'
    output = []
    count = 0
    while ( not stop_event.is_set()):
        time.sleep(1)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        pulse_start = time.time()

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = round(pulse_duration * 17150, 2)

        # if distance > 3000 or distance < 5:
        #     count += 1
        # else:
        #     count = 0
        # if count == 5:
        #     distance = 'Ultrasound TRIGGERED'
            # break
        output.append(distance)
        List_Readings['Ultrasound']=distance
        #print distance
        firebase.put('/', 'BinA', List_Readings) #consistently update ultrasound readings to Firebase

def methane(arg1,stop_event):
    #print 'methane runs eh'
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)  # Read output from PIR motion sensor
    # GPIO.setup(23, GPIO.OUT)       #LED output pin

    while ( not stop_event.is_set()):
        count = 0
        i = GPIO.input(16)
        if count >= 3:
            output.append('Methane detected')
            List_Readings['Methane'] = output[-1]
            firebase.put('/', 'BinA',List_Readings)
        if i == 0:  # When output from motion sensor is lower than 250ppm
            # print "No methane"
            output = i
            time.sleep(1)
            count = 0
        elif i == 1:  # When output from methane sensor is greater than 250ppm
            # print "Methane detected"
            output = i
            time.sleep(1)
            count += 1



def main(): #threading in order to run the 3 sensors at the same time

    t1_stop= threading.Event()
    t1 = threading.Thread(target=methane, args=(1, t1_stop))
    t1.start()
    t2_stop = threading.Event()
    t2 = threading.Thread(target=ultrasound,  args =(1, t2_stop))
    t2.start()
    t3_stop = threading.Event()
    t3 = threading.Thread(target=infrared, args=(1,t3_stop))
    t3.start()
    time.sleep(duration)
# stop the threads after 300 seconds

    t2_stop.set()
    t1_stop.set()
    t3_stop.set()


#Code to run the code every day at a certain timing. 
from datetime import datetime
from threading import Timer, Thread

x = datetime.today()
if x.second < 50:
    y = x.replace(day=x.day, hour=x.hour, minute=x.minute, second=x.second+10, microsecond=0)
else:
    hmm = 59 - x.second
    y = x.replace(day=x.day, hour=x.hour, minute=x.minute + 1, second=x.second + hmm, microsecond=0)

delta_t = y - x



# def u():
#     print ultrasound()


# def i():
#     print infrared()


# def m():
#     print methane()


# t = Timer(secs, u)
# s = Timer(secs, i)
# v = Timer(secs, m)

# if _name_ == '_main_':
#   Thread(target = t).start()
#  Thread(target = s).start()
# Thread(target = v).start()
# start = time.time()
# period = 300
main()
#AllSensors()
cleanup()
