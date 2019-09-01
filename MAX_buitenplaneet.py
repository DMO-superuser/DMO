import socket
planeet = socket.gethostname()
if (planeet == "DMO-Mars"):
   wachttijd = 0.0001   # wachttijd per stap 
if (planeet == "DMO-Jupiter"):
   wachttijd = 0.0005   # wachttijd per stap 
if (planeet == "DMO-Saturnus"):
   wachttijd = 0.001   # wachttijd per stap 


"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  sleep (wachttijd)
