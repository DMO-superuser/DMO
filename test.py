import socket
planeet = socket.gethostname()

def rijden (richting, stijl):
   print (richting)
   print (stijl)
   #kit.stepper1.onestep(richting, stijl)  

richting = 'direction=stepper.BACKWARD'
stijl   = 'style=stepper.DOUBLE'

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
 if planeet != "DMO-Mars":
    rijden (richting, stijl)
 else:
    rijden (richting, stijl)
 #sleep (0.01)
