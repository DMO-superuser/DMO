import socket
planeet = socket.gethostname()



richting = 'stepper.BACKWARD'
stijl   = 'stepper.DOUBLE'
allebei = 'direction=stepper.BACKWARD, style=stepper.DOUBLE'
appel = 'stepper.BACKWARD'
peer = 'stepper.DOUBLE'

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()


while True:
 if planeet != "DMO-Mars":
    kit.stepper1.onestep(direction=richting, style=stijl) 
 else:
    kit.stepper1.onestep(direction=richting, style=stijl) 
 #sleep (0.01)
