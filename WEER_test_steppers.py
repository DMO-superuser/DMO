# WEER_test_steppers.py
# 29 sep 2019, python3


from adafruit_motorkit import MotorKit

kit = MotorKit()

for i in range(100):
    kit.stepper1.onestep()
