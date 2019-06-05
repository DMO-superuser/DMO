# spullen reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 26 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(26,io.INPUT)

schakelaar = "open"
teller = 1
    
"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while (schakelaar == "open"):
  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  if (io.digitalRead(26)):
    #print ("open")
    schakelaar = "open"
  else:
    # onder de schakelaar
    #print ("dicht")
    #print (teller)
    if teller > 1500:
      schakelaar = "dicht"

  print (teller)
  teller +=1
  sleep (0.01)

    
print (teller)
