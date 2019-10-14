# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 


GPIO.setup(21, GPIO.IN) # neerslag

GPIO.setwarnings(False)



while True:


      
  if (GPIO.input(21) == 0):
     print ("21, neerslag = 0")
  else:
     print ("21, neerslag = 1")
