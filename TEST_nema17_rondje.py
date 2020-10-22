import socket
planeet = socket.gethostname()


"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
 if planeet != "DMO-Mars":
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
 else:
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)   
 sleep (0.01)
