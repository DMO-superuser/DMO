# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 

GPIO.setup(22, GPIO.IN) # pin15 rode knop
GPIO.setup(20, GPIO.IN) # pin38 reset 1
GPIO.setup(25, GPIO.IN) # pin36 reset 2
GPIO.setup(16, GPIO.IN) # pin32 reset 3
GPIO.setup(5, GPIO.IN)  # pin26 reset 4
GPIO.setup(12, GPIO.IN)  # pin24 reset 5
GPIO.setup(7, GPIO.IN) # pin22 reset 6
GPIO.setup(11, GPIO.IN) # pin22 reset 7
GPIO.setup(8, GPIO.IN)  # pin29 reset 8
GPIO.setup(23, GPIO.IN) # pin16 windsnelheid

GPIO.setwarnings(False)


# motor HAT stack
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit1 = MotorKit(address=0x60) # meter 3 en 4
kit2 = MotorKit(address=0x61) 
kit3 = MotorKit(address=0x62)
kit4 = MotorKit(address=0x63)

# Apache index.html op http://192.168.178.94/
apache_indexfile = "/var/www/html/index.html"
log_regel = open(apache_indexfile, "a+")

# binnentemperatuur meter
import time
from w1thermsensor import W1ThermSensor
sensor_binnentemp = W1ThermSensor()
binnen_temp = 0
binnen_temp_oud = 0

# luchtdruk meten
import Adafruit_BMP.BMP085 as BMP085
sensor_luchtdruk = BMP085.BMP085()

while True:

  ########################
  # BINNENTEMPERATUUR meter 3
  ########################
  # schaal -30 tot 60 graden
  # 512 stappen in een rondje, 90 graden op de schaal worden gebruikt, 75% van de schaal, 4,27 stap per graad
  ########################
  # eerst wijzer ijken op 0 punt en dat is dan -30 graden Celsius
  ########################

  binnen_temp = sensor_binnentemp.get_temperature()
  # #log_regel.write("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
  print("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
  if (binnen_temp != binnen_temp_oud):
     verschil = binnen_temp - binnen_temp_oud 
     aantal_stappen = int(verschil * 4.27)
     if (verschil > 0):
        #het is warmer
        for x in range(0, aantal_stappen): kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
     else: 
        #het is kouder
        for x in range(0, aantal_stappen): kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
  binnen_temp_oud = binnen_temp
  
  # resetten van meter (zwarte knop bij desbetreffende meter)
  # zwarte knop ingedrukt houden, rode knop erbij om meter andere kant op te laten draaien
  while (GPIO.input(16) == 0):
        # rode knop voor heen en weer
        if (GPIO.input(22) == 1):
           kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        else:
           kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        binnen_temp_oud = -30

  ########################
  # LUCHTDRUK B0M2 meter 4
  ########################
  # schaal 
  # 512 stappen in een rondje
  # PSI
  ########################
  # eerst wijzer ijken 
  ########################
  
  pressure = sensor_luchtdruk.read_pressure()
  print("<p> De luchtdruk is " + str(pressure) + " </p>")
  
  # resetten van meter (zwarte knop bij desbetreffende meter)
  # zwarte knop ingedrukt houden, rode knop erbij om meter andere kant op te laten draaien
  while (GPIO.input(5) == 0):
        # rode knop voor heen en weer
        if (GPIO.input(22) == 1):
           kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        else:
           kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        binnen_temp_oud = -30
  
  
  
  
  ###################
  # WINDSNELHEID B2M1
  ###################
  # de switch is tijdens 1 rotatie op 2 tegenover elkaar liggende posities 
  # gedurende 1 a 2  cm 0. Verder is hij altijd 1
  # om de wind te meten gaan we de nullen tellen. 2 nullen geeft 1 omwenteling
  # de diameter van het schoepenrad is 50 cm
  # een windsnelheid van 150 km/u 
  # geeft  83,3 omwentelingen per seconde
  # geeft 166,6 keer een 0 
  # omtrek van het schoepenrad is 50 cm
  # er wordt 5 seconden gemeten elke keer
  # 
  # windkracht  benaming         km/h     m/sec       omwentelingen/sec  nullen/sec  per 5 sec
  #     0       stil             0  -1     0    - 0,2        0,2            0,4         2
  #     1       zwak             1  -5     0,3  - 1,5        1,8            3,6
  #     2       zwak             6  -11    1,6  - 3,3        4,9            9,8
  #     3       matig            12 -19    3,4  - 5,4        8,8           17,6
  #     4       matig            20 -28    5,5  - 7,9        13,4          26,8 
  #     5       vrij krachtig    29 -38    8,0  - 10,7       18,7          37,4 
  #     6       krachtig         39 -49    10,8 - 13,8       24,6          49,2 
  #     7       hard             50 -61    13,9 - 17,1       31            62,0
  #     8       stormachtig      62 -74    17,2 - 20,7       37,9          75,8
  #     9       storm            75 -88    20,8 - 24,4       45,2          90,4
  #     10      zware storm      89 -102   24,5 - 28,4       52,9          105,8        529
  #     11      zeer zware storm 103-117   28,5 - 32,6       61,1          122,2
  #     12      orkaan           >117      >32,6

  #  0,9 nul per seconde staat voor 1 kilometer per uur
  #  schaal = 50 stapjes per 10 km/h
 

  aantal_nullen = 0
  reed_switch = 0
  timeout = time.time() + 5
  while (time.time() < timeout) :
    if (GPIO.input(20) == 0):
        if (reed_switch == 0):
           aantal_nullen = aantal_nullen + 1
        reed_switch = 1
    else :
        if reed_switch == 1 :
           reed_switch = 0
  print("<p> De windsnelheid in aantal nullen is" + str(aantal_nullen) + " </p>")

