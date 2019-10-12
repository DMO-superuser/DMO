"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep


kit1 = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)
kit4 = MotorKit(address=0x63)

#while True:
#  kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit2.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit2.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit3.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit3.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit4.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#  kit4.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
 
