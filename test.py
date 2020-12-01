import socket
planeet = socket.gethostname()



richting = 'direction=stepper.BACKWARD'
stijl   = 'style=stepper.DOUBLE'

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
 if planeet != "DMO-Mars":
    kit.stepper1.onestep(richting, stijl) 
 else:
    kit.stepper1.onestep(richting, stijl) 
 #sleep (0.01)
