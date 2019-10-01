"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep


kit1 = MotorKit(address=0x60)
# Initialise the second hat on a different address
# kit2 = MotorKit(address=0x61)

while True:
  kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
