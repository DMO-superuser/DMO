# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 

GPIO.setup(22, GPIO.IN) # pin15 rode knop
GPIO.setup(27, GPIO.IN) # pin13 24 uur
GPIO.setup(20, GPIO.IN) # pin38 reset 1
GPIO.setup(16, GPIO.IN) # pin36 reset 2
GPIO.setup(12, GPIO.IN) # pin32 reset 3
GPIO.setup(7, GPIO.IN)  # pin26 reset 4
GPIO.setup(8, GPIO.IN)  # pin24 reset 5
GPIO.setup(25, GPIO.IN) # pin22 reset 6
GPIO.setup(11, GPIO.IN) # pin22 reset 7
GPIO.setup(5, GPIO.IN)  # pin29 reset 8
GPIO.setup(23, GPIO.IN) # pin16 windsnelheid

GPIO.setwarnings(False)



while True:

  if (GPIO.input(20) == 0):
     print ("reset 1 = 0")
  else:
     print ("reset 1 = 1")
      
  if (GPIO.input(16) == 0):
     print ("reset 2 = 0")
  else:
     print ("reset 2 = 1")

  if (GPIO.input(12) == 0):
     print ("reset 3 = 0")
  else:
     print ("reset 3 = 1")

  if (GPIO.input(7) == 0):
     print ("reset 4 = 0")
  else:
     print ("reset 4 = 1")

  if (GPIO.input(8 == 0):
     print ("reset 5 = 0")
  else:
     print ("reset 5 = 1")

  if (GPIO.input(25) == 0):
     print ("reset 6 = 0")
  else:
     print ("reset 6 = 1")

  if (GPIO.input(11) == 0):
     print ("reset 7 = 0")
  else:
     print ("reset 7 = 1")

  if (GPIO.input(5) == 0):
     print ("reset 8 = 0")
  else:
     print ("reset 8 = 1")

  if (GPIO.input(22) == 0):
     print ("rood = 0")
  else:
     print ("rood = 1")

  if (GPIO.input(27) == 0):
     print ("24 hour = 0")
  else:
     print ("24 hour = 1")

      
