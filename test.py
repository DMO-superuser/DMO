import socket
planeet = socket.gethostname()



richting = 'stepper.BACKWARD'
stijl   = 'stepper.DOUBLE'
allebei = 'direction=stepper.BACKWARD, style=stepper.DOUBLE'


"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
 kit.stepper1.onestep(allebei) 

 #sleep (0.01)
