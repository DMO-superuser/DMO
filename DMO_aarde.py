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
  #print "Setup pins"
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
Seq = Seq2
StepCount = StepCount2
schakelaar = "open"


# spullen reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 26 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(26,io.INPUT)

# spullen curl
import requests
url = 'http://planetarium.chrisdemoor.nl/positions.txt'
positiestring     = ""
positiestring_oud = "leeg"

while True:
  r = requests.get(url)
  positiestring = r.text

  # bepalen aantal stappen
  aantal_graden_positiestring = 360 - int(positiestring[6:9])
  aantal_graden_nulpunt_aarde = 236 # begin magneet veld = 20 augustus
  aantal_graden_tot_23_dec = 360 - aantal_graden_nulpunt_aarde
  if (aantal_graden_positiestring > aantal_graden_nulpunt_aarde):
    # de datum ligt voor 23 december
    aantal_graden_te_lopen = aantal_graden_positiestring - aantal_graden_nulpunt_aarde   
  else:  
    aantal_graden_te_lopen = aantal_graden_tot_23_dec + aantal_graden_positiestring
  aantal_stappen_te_lopen = int(aantal_graden_te_lopen * 57.34)

  # als er een nieuwe positie is ingegeven op de website
  if (positiestring != positiestring_oud):
  
    # EERST RONDJE AFMAKEN EN NAAR HET BEGIN LOPEN
    teller = 1
    while (schakelaar == "open"):
      for pin in list(range(0, 4)):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          #print "Stap: %i GPIO Actief: %i" %(StepCounter,xpin
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
   
      #print (teller) 
      teller += 1  
      StepCounter += 1
  
      if (io.digitalRead(26)):
        #print ("open")
        schakelaar = "open"
      else:
        # onder de schakelaar
        #print ("dicht")
        #print (teller)
        if teller > 1500:
          schakelaar = "dicht"

      # Als we aan het einde van de stappenvolgorde zijn beland start dan opnieuw
      if (StepCounter==StepCount): StepCounter = 0
      if (StepCounter<0): StepCounter = StepCount

      # Wacht voor de volgende stap (lager = snellere draaisnelheid)
      sleep(.001)

    # DAARNA NAAR DE POSITIE LOPEN
    teller = 1
    while (teller < aantal_stappen_te_lopen):
      for pin in list(range(0, 4)):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          #print "Stap: %i GPIO Actief: %i" %(StepCounter,xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
        
      #print (teller) 
      teller += 1
      StepCounter += 1

      # Als we aan het einde van de stappenvolgorde zijn beland start dan opnieuw
      if (StepCounter==StepCount): StepCounter = 0
      if (StepCounter<0): StepCounter = StepCount
    
      # Wacht voor de volgende stap (lager = snellere draaisnelheid)
      sleep(.001)

    positiestring_oud = positiestring
