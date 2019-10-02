# diversen
from time import sleep

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) # pin7  binnen temperatuur 
GPIO.setup(22, GPIO.IN) # pin15 rode knop

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
binnen_temp = 0
binnen_temp_oud = 0


while True:

  ########################
  # BINNENTEMPERATUUR B0M1
  ########################
  # schaal -10 tot 60 graden
  # 512 stappen in een rondje, 225 graden op de schaal worden gebruikt, 2,28 stap per graad op wijzerplaat
  # graden Celsius op 2 decimalen
  ########################
  # eerst wijzer ijken op 0 punt en dat is dan -30 graden Celsius
  ########################

    binnen_temp = round(sensor.get_temperature(),2)
    #log_regel.write("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
    print("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
    if (binnen_temp != binnen_temp_oud):
       verschil = binnen_temp - binnen_temp_oud 
       if (verschil > 0):
          #het is warmer
          for x in range(0, 50): kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
       else: 
          #het is kouder
          for x in range(0, 50): kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
    binnen_temp_oud = binnen_temp
    
  #############################
  # RESETTEN van meters
  #############################
  # RODE KNOP = GPIO 22 
    if GPIO.input(22):
      # Schakelaar is AAN.
      print "Schakelaar AAN, GPIO status:", GPIO.input(22)
    else:
      # Schakelaar is UIT.
      print "Schakelaar UIT, GPIO status:", GPIO.input(22)
 
    
