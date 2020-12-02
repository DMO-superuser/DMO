import socket
import requests
from datetime import datetime
from time import sleep
import os
import wiringpi
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

# string van de website in te lezen
url = 'http://planetarium.chrisdemoor.nl/positions.txt'

# indien test_modus is TRUE dan wordt niet de websitestring gebruikt maar de 
# simulator op TEST_website_string.py die op een aparte RPI draait
# als planeet_motor is TRUE dan kan er ook gereden worden in test_modus, anders niet
# en is het uitsluitend om de software te testen
test_modus = False
planeet_motor = True
if test_modus:
   url = 'http://192.168.178.52/positions.txt'

#welke planeet zijn we?
planeet = socket.gethostname()

if (planeet == "DMO-Saturnus"):
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 350  # 14 december, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
   richting = stepper.BACKWARD
   stijl = stepper.DOUBLE
if (planeet == "DMO-Jupiter"):
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 350  # 14 december, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
   richting = stepper.BACKWARD
   stijl = stepper.DOUBLE
if (planeet == "DMO-Mars"):
   totaal_stappen = 2045 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 90  # 23 september, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
   richting = stepper.FORWARD
   stijl = stepper.DOUBLE
if (planeet == "DMO-Aarde"):
   totaal_stappen = 1107 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 20   # 1 december, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet 
   richting = stepper.BACKWARD
   stijl = stepper.DOUBLE
if (planeet == "DMO-Venus"):
   totaal_stappen = 1019 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 101  # 10 september, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 3  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 6  # de eindpositie in de string bij de Curl van deze planeet 
   richting = stepper.BACKWARD
   stijl = stepper.DOUBLE
if (planeet == "DMO-Mercurius"):
   totaal_stappen = 202 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 187   # 14 juni, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 0  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 3  # de eindpositie in de string bij de Curl van deze planeet 
   richting = stepper.BACKWARD
   stijl = stepper.DOUBLE

#controle WiFi
def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=3)
        print ('ONLINE')
        return True
    except requests.ConnectionError as ex:
        #print(ex)
        print ('OFFLINE')
        offline_teller +=1
        if offline_teller > 10:
           os.system('sudo shutdown -r now')
        sleep(1)
        return False
    
# spullen reedswitch
os.system('gpio export 19 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(19,io.INPUT)

# spullen Adafruit
kit = MotorKit()

schakelaar = "open"
teller = 1
positiestring     = ""
positiestring_oud = "001001001001001001001001001"
totaalteller = 1
offline_teller = 1


# bij de eerste keer opstarten wachten totdat alle processen in de Pi zijn opgestart (anders hapert de stepper in het begin tijdens het rijden)
sleep (30)



while True:

  #timestamp voor DMO.log
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  print ('-------------------------------')
  print (totaalteller , ' ' + dt_string + ' ' + planeet)
  
  if checkInternetRequests():
     try:
       r = requests.get(url, timeout=4)
       positiestring = r.text
     except requests.exceptions.ConnectionError:
       positiestring = positiestring_oud

  print ('Mer ',positiestring[0:3],' Ven ',positiestring[3:6],' Aar ',positiestring[6:9],' Mar ',positiestring[9:12],' Jup ',positiestring[12:15],' Sat ',positiestring[15:18])

 # als er een nieuwe positie is ingegeven op de website en er is een internetverbinding
  if (str(positiestring) != str(positiestring_oud)):   
      
    # EERST NAAR MAGNEET RIJDEN, die ligt op 001
    while (schakelaar == "open") and (not test_modus):
      kit.stepper1.onestep(direction=richting, style= stijl)
      if (io.digitalRead(19)):  
        schakelaar = "open"
      else:
        if teller > 200:
          schakelaar = "dicht"
      teller +=1
    sleep(1)  
   
    # BEREKENING AANTAL STAPPEN 
    try:
       nieuwe_positie_planeet = int(positiestring[beginpos_string:eindpos_string])
    except:
       print ('FOUT in conversie van: ',  positiestring[beginpos_string:eindpos_string])
       nieuwe_positie_planeet = 1
    stappen_per_graad = totaal_stappen/360
    if (nieuwe_positie_planeet < magneet_positie) and (nieuwe_positie_planeet > 0):
       aantal_stappen_te_lopen = (magneet_positie - nieuwe_positie_planeet) * stappen_per_graad
    else:
       aantal_stappen_te_lopen =  ((360- nieuwe_positie_planeet)+ magneet_positie) * stappen_per_graad 
    
    print ('nieuwe_positie_planeet ' , nieuwe_positie_planeet)
    print ('stappen_per_graad ' , stappen_per_graad)
    print ('magneet_positie ' , magneet_positie)
    print ('aantal_stappen_te_lopen ' , aantal_stappen_te_lopen)      
   
    # NU NAAR POSITIE RIJDEN 
    teller = 1
    while (teller < aantal_stappen_te_lopen):
       if planeet_motor:
          kit.stepper1.onestep(direction=richting, style= stijl) 
       teller +=1    
    sleep (1)
   
  # 10 seconden wachten omdat anders de GET teveel requests doet naar de server en ons weigert
  sleep (10)
  totaalteller +=1
  if planeet_motor:
     kit.stepper1.release() 
      
  positiestring_oud = positiestring
  schakelaar = "open"
  teller = 1

