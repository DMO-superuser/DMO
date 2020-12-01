import socket
planeet = socket.gethostname()




allebei = 'direction=stepper.BACKWARD, style=stepper.DOUBLE'
rich = 'BACKWARD'
stij = 'DOUBLE'

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()
richting = stepper.BACKWARD
stijl   = stepper.DOUBLE

while True:
 kit.stepper1.onestep(direction=richting, style= stijl)

 #sleep (0.01)
