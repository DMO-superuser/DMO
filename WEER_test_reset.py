# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 

GPIO.setup(22, GPIO.IN) # pin15 rode knop
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

