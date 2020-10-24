# spullen reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 19 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(19,io.INPUT)


import socket
planeet = socket.gethostname()


"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

schakelaar = "open"
teller = 1

while (schakelaar == "open"):
  if planeet != "DMO-Mars":
     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  else:
     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   
  if (io.digitalRead(19)):
    #print ("open")
    schakelaar = "open"
  else:
    # onder de schakelaar
    #print ("dicht")
    #print (teller)
    if teller > 100:
      schakelaar = "dicht"

  print (teller)
  teller +=1
  sleep (0.001)

    
print (teller)
