# Import eBot and time module
from eBot import eBot
from time import sleep

def forward(speed, duration):
    ebot.wheels(speed,speed)
    sleep(duration)
    pass
def celcius_to_farenheit(c):
    c = ebot.temperature()
    f = (c*9/5)+32
    return format(f, '.3f') 

def epic():
    speed = float(raw_input("Input speed (max 1): "))
    duration = float(raw_input("Input duration: "))    
    forward(speed, duration)
    ebot.imperial_march()
    return 
    
ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

############### Start writing your code here ################ 
def go_go_power_rangers():
    x = format(ebot.temperature(), '.3f')
    epic()
    print "The temperature in Celcius is", x, "and Farenheit is", celcius_to_farenheit(x)
    return

go_go_power_rangers()
########################## end ############################## 

ebot.disconnect() # disconnect the Bluetooth communication
