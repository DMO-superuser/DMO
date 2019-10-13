# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 


GPIO.setup(6, GPIO.IN) # windrichting 1
GPIO.setup(13, GPIO.IN) # windrichting 2
GPIO.setup(19, GPIO.IN) # windrichting 3
GPIO.setup(26, GPIO.IN) # windrichting 4

GPIO.setwarnings(False)



while True:


      
  if (GPIO.input(6) == 0):
     print ("6, windrichting 1 = 0")
  else:
     print ("6, windrichting 1 = 1")
     
  if (GPIO.input(13) == 0):
     print ("13, windrichting 2 = 0")
  else:
     print ("13, windrichting 2 = 1")   
          
  if (GPIO.input(19) == 0):
     print ("19, windrichting 3 = 0")
  else:
     print ("19, windrichting 3 = 1")     

          
  if (GPIO.input(26) == 0):
     print ("26, windrichting 4 = 0")
  else:
     print ("26, windrichting 4 = 1")     

  sleep (1)
