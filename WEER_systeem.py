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
log_regel = open(apache_indexfile, "w")

# binnentemperatuur meter
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()


while True:
  ########################
  # BINNENTEMPERATUUR B0M1
  ########################
  # schaal -10 tot 50 graden
  # stepper: 512 stappen in het rond
    temperature = sensor.get_temperature()
    #print("The temperature is %s celsius" % temperature)
    log_regel.write("<p> De binnentemperatuur is ",temperature," </p>")

    
    
    time.sleep(1)
