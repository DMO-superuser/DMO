# diversen
from time import sleep
import os

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # pin7  binnen temperatuur 

GPIO.setup(22, GPIO.IN)  # pin15 rode knop
GPIO.setup(20, GPIO.IN)  # pin38 reset 1
GPIO.setup(25, GPIO.IN)  # pin36 reset 2
GPIO.setup(16, GPIO.IN)  # pin32 reset 3
GPIO.setup(5, GPIO.IN)   # pin26 reset 4
GPIO.setup(12, GPIO.IN)  # pin24 reset 5
GPIO.setup(7, GPIO.IN)   # pin22 reset 6
GPIO.setup(11, GPIO.IN)  # pin22 reset 7
GPIO.setup(8, GPIO.IN)   # pin29 reset 8
GPIO.setup(23, GPIO.IN)  # pin16 windsnelheid
GPIO.setup(6, GPIO.IN)   # pin31 windrichting 1
GPIO.setup(13, GPIO.IN)  # pin33 windrichting 2
GPIO.setup(19, GPIO.IN)  # pin35 windrichting 3
GPIO.setup(26, GPIO.IN)  # pin37 windrichting 4
GPIO.setup(21, GPIO.IN)  # pin40 neerslag


GPIO.setwarnings(False)


# motor HAT stack
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit1 = MotorKit(address=0x60) # meter 3 en 4
kit2 = MotorKit(address=0x61) 
kit3 = MotorKit(address=0x62) # meter 5 en 6
kit4 = MotorKit(address=0x63) # meter 7 en 8

# Apache index.html op http://192.168.178.94/
apache_indexfile = "/var/www/html/index.html"
log_regel = open(apache_indexfile, "a+")

# binnentemperatuur meter
import time
from w1thermsensor import W1ThermSensor
sensor_binnentemp = W1ThermSensor()
binnen_temp = 0
binnen_temp_oud = -30

# luchtdruk meten
import Adafruit_BMP.BMP085 as BMP085
sensor_luchtdruk = BMP085.BMP085()
luchtdruk = 0
luchtdruk_oud = 950

# windsnelheid
km_per_uur = 0
km_per_uur_oud = 0
km_tijd = 1 # aantal seconden dat de wind gemeten wordt

# windrichting
positie = 0
positie_oud = 0

# neerslag
neerslag_wip = 0
neerslag_wip_oud = 1
neerslag_hoeveelheid = 0
neerslag_aantal = 0
neerslag_begin_tijd = time.time() # in seconden


while True:

  ########################
  # BINNENTEMPERATUUR meter 3
  ########################
  # schaal -30 tot 60 graden
  # 512 stappen in een rondje, 90 graden Celcius op de schaal worden gebruikt, 75% van de schaal, 4,27 stap per graad
  ########################
  # eerst wijzer ijken op 0 punt en dat is dan -30 graden Celsius
  ########################
  binnen_temp = sensor_binnentemp.get_temperature()
  #print("<p> De binnentemperatuur is " + str(binnen_temp) + " </p>")
  if (binnen_temp != binnen_temp_oud):
     verschil = binnen_temp - binnen_temp_oud 
     aantal_stappen = int(verschil * 4.27)
     if (verschil > 0):
        #het is warmer
        for x in range(0, abs(aantal_stappen)): kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
     else: 
        #het is kouder
        for x in range(0, abs(aantal_stappen)): kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
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
  # schaal 950 tot 1050
  # 512 stappen in een rondje, 100 hPa op de schaal wordt gebruikt, 75% van de schaal, 3,84 stap per graad
  ########################
  # eerst wijzer ijken op 0 punt en dat is dan 950
  ########################
  luchtdruk = (sensor_luchtdruk.read_pressure() / 100)
  #print("<p> De luchtdruk is " + str(luchtdruk) + " </p>")
  if (luchtdruk != luchtdruk_oud):
     verschil = luchtdruk - luchtdruk_oud 
     aantal_stappen = int(verschil * 3.84)
     if (verschil > 0):
        #het is meer
        for x in range(0, abs(aantal_stappen)): kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
     else: 
        #het is minder
        for x in range(0, abs(aantal_stappen)): kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
  luchtdruk_oud = luchtdruk
  
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
        luchtdruk_oud = 950
  
  ###################
  # WINDSNELHEID B2M1 meter 5
  ###################
  # de switch is tijdens 1 rotatie op 2 tegenover elkaar liggende posities 
  # gedurende 1 a 2  cm 0. Verder is hij altijd 1
  # om de wind te meten gaan we de nullen tellen. 2 nullen geeft 1 omwenteling
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
  #
  # schaal 0 tot 120 km/h
  # 512 stappen in een rondje, 120 km/h op de schaal wordt gebruikt, 75% van de schaal, 3,2 stap per km/h
  ########################
  # eerst wijzer ijken op 0 punt en dat is dan 0

  aantal_nullen = 0
  reed_switch = 0
  timeout = time.time() + km_tijd
  while (time.time() < timeout) :
    if (GPIO.input(23) == 0):
        if (reed_switch == 0):
           aantal_nullen = aantal_nullen + 1
        reed_switch = 1
    else :
        if reed_switch == 1 :
           reed_switch = 0
  km_per_uur = int(0.9 * aantal_nullen)
  
  # print("<p> De windsnelheid in km/h is " + str(km_per_uur) + " </p>")

  if (km_per_uur != km_per_uur_oud):
     verschil = km_per_uur - km_per_uur_oud 
     aantal_stappen = int(verschil * 3.2)
     if (verschil > 0):
        #het waait harder
        for x in range(0, abs(aantal_stappen)): kit3.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
     else: 
        #het waait minder hard
        for x in range(0, abs(aantal_stappen)): kit3.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
  km_per_uur_oud = km_per_uur
  
  # resetten van meter (zwarte knop bij desbetreffende meter)
  # zwarte knop ingedrukt houden, rode knop erbij om meter andere kant op te laten draaien
  while (GPIO.input(12) == 0):
        # rode knop voor heen en weer
        if (GPIO.input(22) == 1):
           kit3.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        else:
           kit3.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        km_per_uur_oud = 0
        
  ###################
  # WINDRICHTING B2M1 meter 6
  ###################
  #
  # windrichting, Oost is rechts
  # ijkpunt is op het Zuiden, positie = 0
  # wordt alleen uitgevoerd als windsnelheid groter of gelijk aan 12 km/h is 
  #
  #  26 19 13 6  R   
  #  1  0  0  0  N   256
  #  0  0  0  1  w   128
  #  0  0  1  0  Z   0
  #  0  1  0  0  O   384
  #  1  1  0  0  NO  320
  #  0  1  1  0  ZO  448
  #  1  0  0  1  NW  192
  #  0  0  1  1  ZW  64       

  if (km_per_uur >= 12):
    if ((GPIO.input(26) == 1) and (GPIO.input(19) == 0) and (GPIO.input(13) == 0) and (GPIO.input(6) == 0)): 
      positie = 256
      print("<p> De wind komt uit het Noorden </p>")    
    if ((GPIO.input(26) == 0) and (GPIO.input(19) == 0) and (GPIO.input(13) == 0) and (GPIO.input(6) == 1)): 
      positie = 128
      print("<p> De wind komt uit het Westen </p>")    
    if ((GPIO.input(26) == 0) and (GPIO.input(19) == 0) and (GPIO.input(13) == 1) and (GPIO.input(6) == 0)):
      positie = 0
      print("<p> De wind komt uit het Zuiden </p>")    
    if ((GPIO.input(26) == 0) and (GPIO.input(19) == 2) and (GPIO.input(13) == 0) and (GPIO.input(6) == 0)): 
      positie = 384      
      print("<p> De wind komt uit het Oosten </p>")    
    if ((GPIO.input(26) == 1) and (GPIO.input(19) == 1) and (GPIO.input(13) == 0) and (GPIO.input(6) == 0)):
      positie = 320
      print("<p> De wind komt uit het Noordoosten </p>")       
    if ((GPIO.input(26) == 0) and (GPIO.input(19) == 1) and (GPIO.input(13) == 1) and (GPIO.input(6) == 0)): 
      positie = 448
      print("<p> De wind komt uit het Zuidoosten </p>")     
    if ((GPIO.input(26) == 1) and (GPIO.input(19) == 0) and (GPIO.input(13) == 0) and (GPIO.input(6) == 1)): 
      positie = 192
      print("<p> De wind komt uit het Noordwesten </p>")     
    if ((GPIO.input(26) == 0) and (GPIO.input(19) == 0) and (GPIO.input(13) == 1) and (GPIO.input(6) == 1)): 
      positie = 64
      print("<p> De wind komt uit het Zuidwesten </p>")  
    if (positie != positie_oud):
      aantal_stappen = positie - positie_oud 
      if (verschil > 0):
        #naar rechts
        for x in range(0, abs(aantal_stappen)): kit3.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
      else: 
        #naar links
        for x in range(0, abs(aantal_stappen)): kit3.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
      positie_oud = positie
  else:  
      print("<p> Wind te zwak om richting te bepalen </p>") 
    
  # resetten van meter (zwarte knop bij desbetreffende meter)
  # zwarte knop ingedrukt houden, rode knop erbij om meter andere kant op te laten draaien
  while (GPIO.input(7) == 0):
        # rode knop voor heen en weer
        if (GPIO.input(22) == 1):
           kit3.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        else:
           kit3.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE) 
           sleep (0.02)
        positie_oud = 0    
    
  ##############################################
  # NEERLSLAG MM per uur meter 7 en per etmaal meter 8
  ##############################################
  # gevallen regen in mm = aantal ml afgetapte neerslag x 10 gedeeld door de oppervlakte in cm2
  # oppervlakte trechter = 1/2 diameter * 1/2 diameter * Pi = 5 * 5 * Pi = 79,82 cm2
  # het wipje slaat om per 2,3 ml
  # als wipje 12 x omslaat in een uur dan is het:
  # 12 * 2,3 * 10 = 3,45 mm per uur 
  # in 1 uur zitten 3600 seconden, er zijn 6 containers van 10 minuten om het voortschrijdend gemiddelde we   
  # max per uur is 90 mm (record is 79)
  
  neerslag_wip = GPIO.input(21)
  if (neerslag_wip != neerslag_wip_oud):
     neerslag_wip_oud = neerslag_wip     
     print("<p> de tijd is  " + str(time.time()) + " </p>")
     print("<p> Aantal keer wipje omgegaan " + str(neerslag_wip) + " </p>")  
     print("<p> -------------- </p>") 
