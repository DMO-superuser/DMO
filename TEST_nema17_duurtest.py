from time import sleep

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit()

import socket
planeet = socket.gethostname()


while True:
  
  teller = 1
  while (teller < 200) :
    if planeet != "DMO-Mars":
       kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    else:
       kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   
    
    teller +=1

  #kit.stepper1.release()

  sleep(10)

