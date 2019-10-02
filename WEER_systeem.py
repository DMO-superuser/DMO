# diversen
from time import sleep

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) # pin7

# motor HAT stack
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit1 = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)
#kit4 = MotorKit(address=0x63)

# Apache index.html op http://192.168.178.94/
apache_indexfile = "/var/www/html/index.html"
log_regel = open(apache_indexfile, "a+")

# binnentemperatuur meter
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()


while True:
  ########################
  # CONFIG FILE INLEZEN
  ########################
  
  ########################
  # BINNENTEMPERATUUR B0M1
  ########################
  # schaal -10 tot 50 graden
  # stepper: 512 stappen in het rond
    binnen_temp = sensor.get_temperature()
    log_regel.write("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
    binnen_temp = int(binnen_temp)
    
    
    time.sleep(1)
