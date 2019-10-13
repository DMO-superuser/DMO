# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 


GPIO.setup(23, GPIO.IN) # pin16 windsnelheid

GPIO.setwarnings(False)



while True:


      
  if (GPIO.input(23) == 0):
     print ("23, windsnelheid = 0")
  else:
     print ("23, windsnelheid = 1")
