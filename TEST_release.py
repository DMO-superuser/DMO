
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep
kit = MotorKit()


teller = 1
while (teller < 50):
  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  teller +=1

kit.stepper1.release()
   
