# diversen
from time import sleep

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) # pin7  binnen temperatuur 
GPIO.setup(22, GPIO.IN) # pin15 rode knop
GPIO.setup(20, GPIO.IN) # pin38 reset 1
GPIO.setup(16, GPIO.IN) # pin36 reset 2
GPIO.setup(12, GPIO.IN) # pin32 reset 3
GPIO.setup(7, GPIO.IN) # pin26 reset 4
GPIO.setup(8, GPIO.IN) # pin24 reset 5
GPIO.setup(25, GPIO.IN) # pin22 reset 6
GPIO.setup(5, GPIO.IN) # pin29 reset 8



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
#import time
#from w1thermsensor import W1ThermSensor
#sensor = W1ThermSensor()
#binnen_temp = 0
#binnen_temp_oud = 0


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

  #  binnen_temp = sensor.get_temperature()
  # #log_regel.write("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
  #  print("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
  #  if (binnen_temp != binnen_temp_oud):
  #     verschil = binnen_temp - binnen_temp_oud 
  #     if (verschil > 0):
  #        #het is warmer
  #        for x in range(0, 50): kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
  #     else: 
  #        #het is kouder
  #        for x in range(0, 50): kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
  #  binnen_temp_oud = binnen_temp
    
  #############################
  # RESETTEN van meters
  #############################
  if GPIO.input(22):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, rood")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, rood")

  if GPIO.input(20):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset1")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset1")
 
  if GPIO.input(16):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset2")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset2")
      
  if GPIO.input(16):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset2")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset2")
      
  if GPIO.input(12):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset3")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset3")
 
  if GPIO.input(7):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset4")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset4")
 
  if GPIO.input(8):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset5")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset5")
 
  if GPIO.input(25):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset6")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset6")
 
  if GPIO.input(11):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset7")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset7")
 
  if GPIO.input(5):
      # Schakelaar is AAN.
      print ("Schakelaar AAN, reset8")
  else:
      # Schakelaar is UIT.
      print ("Schakelaar UIT, reset8")
 




      
 

    
