import socket
planeet = socket.gethostname()



richting = 'direction=stepper.BACKWARD'
stijl   = 'style=stepper.DOUBLE'
allebei = 'direction=stepper.BACKWARD, style=stepper.DOUBLE'
appel = 'appel'
peer = 'peer'

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

kit.stepper1.onestep(direction=appel,style=peer)

while True:
 if planeet != "DMO-Mars":
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
 else:
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
 #sleep (0.01)
