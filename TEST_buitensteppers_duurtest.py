from time import sleep

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit()

while True:
  
  teller = 1
  while (teller < 200) :
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    teller +=1

  kit.stepper1.release()

  sleep(10)

