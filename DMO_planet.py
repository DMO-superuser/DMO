# DMO_planet.py
# 20 feb 2019, python3

# initele variabelen

stepper    = "buiten"  # er zijn binnen en buitensteppers
schakelaar = "open"    # de positie van de magneetschakelaar
teller = 1             # stappenteller van de planeet

# welke planeet is dit?
import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   stepper = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 154   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Jupiter"):
   stepper = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 144   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Mars"):
   stepper = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 2596 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Aarde"):
   stepper = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 2000 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Venus"):
   stepper = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 2000 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet      
if (planeet == "DMO-Mercurius"):
   stepper = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 2000 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet
   
# spullen van de buitenstepper
if stepper == "buiten":
 from adafruit_motorkit import MotorKit
 from adafruit_motor import stepper
 kit = MotorKit()

#spullen van de binnenstepper
if stepper == "binnen":
 # importeer de GPIO bibliotheek.
 import RPi.GPIO as GPIO
 # Importeer de time biblotheek voor tijdfuncties.
 from time import sleep

 # Zet de pinmode op Broadcom SOC.
 GPIO.setmode(GPIO.BCM)
 # Zet waarschuwingen uit.
 GPIO.setwarnings(False)
 # Stel de GPIO pinnen in voor de stappenmotor:
 StepPins = [4,17,27,22]

 # Set alle pinnen als uitgang.
 for pin in StepPins:
   # print "Setup pins"
   GPIO.setup(pin,GPIO.OUT)
   GPIO.output(pin, False)

 # Definieer variabelen.
 StepCounter = 0

 # Definieer simpele volgorde
 StepCount1 = 4
 Seq1 = []
 Seq1 = list(range(0, StepCount1))
 Seq1[0] = [1,0,0,0]
 Seq1[1] = [0,1,0,0]
 Seq1[2] = [0,0,1,0]
 Seq1[3] = [0,0,0,1]

 # Definieer geadvanceerde volgorde (volgens de datasheet)
 StepCount2 = 8
 Seq2 = []
 Seq2 = list(range(0, StepCount2))
 Seq2[0] = [1,0,0,0]
 Seq2[1] = [1,1,0,0]
 Seq2[2] = [0,1,0,0]
 Seq2[3] = [0,1,1,0]
 Seq2[4] = [0,0,1,0]
 Seq2[5] = [0,0,1,1]
 Seq2[6] = [0,0,0,1]
 Seq2[7] = [1,0,0,1]

 # Welke stappenvolgorde gaan we hanteren?
 Seq = Seq1
 StepCount = StepCount1

# spullen van de reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 26 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(26,io.INPUT)

# spullen op de string van de website in te lezen
# elke planeet heeft 3 posities in de string, de telling gaat van binnen naar buiten. Dus Mercurius eerst en  Uranus en Neptunus als laatste (met de laatste 2 gebeurt niets)
import requests
url = 'http://planetarium.chrisdemoor.nl/positions.txt'


while True: 

 teller = 1

 # naar het begin rijden, gebeurt elke keer bij een nieuwe positie
 while schakelaar == "open":
  if stepper == "buiten":
    # buitenstepper in actie
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
  else:
    # binnenstepper in actie
    while True:
      for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          # print "Stap: %i GPIO Actief: %i" %(StepCounter,xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepCounter += 1
      # Als we aan het einde van de stappenvolgorde zijn beland start dan opnieuw
      if (StepCounter==StepCount): StepCounter = 0
      if (StepCounter<0): StepCounter = StepCount
      # Wacht voor de volgende stap (lager = snellere draaisnelheid)
      sleep(.001)
      
   if (io.digitalRead(26)):
      schakelaar = "open"
  else:
      # onder de schakelaar
      if (teller > 100):
       schakelaar = "dicht"
       print ("op het begin!")
  teller += 1

 teller = 1
 positiestring_oud = ""
 r = requests.get(url)
 positiestring = r.text
 schakelaar = "open"

 if (positiestring_oud != positiestring):
  # er is een nieuwe positie en daar gaan we nu bepalen
  positiestring_oud = positiestring
  print (positiestring)
  print (positiestring[beginpos_string:eindpos_string])
  stappen_per_graad = totaal_stappen / 360
  nieuwe_positie = int(positiestring[beginpos_string:eindpos_string]) * int(stappen_per_graad)

  # en naar de nieuwe positie toe rijden.
  while (teller <  nieuwe_positie):
    if stepper == "buiten":
       # buitensteppers in actie
       kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    else:
       # binnenstepper in actie
       while True:
        for pin in range(0, 4):
          xpin = StepPins[pin]
          if Seq[StepCounter][pin]!=0:
            # print "Stap: %i GPIO Actief: %i" %(StepCounter,xpin)
            GPIO.output(xpin, True)
          else:
            GPIO.output(xpin, False)
        StepCounter += 1
        # Als we aan het einde van de stappenvolgorde zijn beland start dan opnieuw
        if (StepCounter==StepCount): StepCounter = 0
        if (StepCounter<0): StepCounter = StepCount
        # Wacht voor de volgende stap (lager = snellere draaisnelheid)
        sleep(.001)         

         teller += 1
  
  # telkens de string opvragen en zolang er geen nieuwe string is hier blijven
  while positiestring == positiestring_oud:
    r = requests.get(url)
    positiestring = r.text

