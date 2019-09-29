# WEER_test_steppers.py
# 29 sep 2019, python3

# spullen van de buitenstepper
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit(address=0x61)


while True: 

  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

