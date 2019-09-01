import socket
planeet = socket.gethostname()
if (planeet == "DMO-Mars"):
   wachttijd = .001   # wachttijd per stap Venus
if (planeet == "DMO-Jupiter"):
   wachttijd = .0005   # wachttijd per stap planeet
if (planeet == "DMO-Saturnus"):
   wachttijd = .001   # wachttijd per stap planeet


"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  sleep (wachttijd)
