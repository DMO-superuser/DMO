

# spullen reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 26 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(26,io.INPUT)

# spullen Adafruit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep
kit = MotorKit()

# spullen op de string van de website in te lezen
import requests
url = 'http://planetarium.chrisdemoor.nl/positions.txt'

schakelaar = "open"
teller = 1
positiestring     = ""
positiestring_oud = "leeg"

aantal_stappen_te_lopen =  50
   
# 50 teststappen
teller = 1
while (teller < aantal_stappen_te_lopen):
  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  teller +=1

kit.stepper1.release()
   
