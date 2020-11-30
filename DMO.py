import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 350  # 14 december, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Jupiter"):
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 350  # 14 december, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Mars"):
   totaal_stappen = 2045 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 90  # 23 september, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Aarde"):
   totaal_stappen = 1107 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 20   # 1 december, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet 
if (planeet == "DMO-Venus"):
   totaal_stappen = 1019 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 101  # 10 september, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 3  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 6  # de eindpositie in de string bij de Curl van deze planeet 
if (planeet == "DMO-Mercurius"):
   totaal_stappen = 202 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 187   # 14 juni, positie in graden waar de magneet van de planeet ligt
   beginpos_string = 0  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 3  # de eindpositie in de string bij de Curl van deze planeet 

#controle WiFi
import requests
from datetime import datetime
from time import sleep
def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        print ('ONLINE')
        return True
    except requests.ConnectionError as ex:
        #print(ex)
        print ('OFFLINE')
        sleep(1)
        return False
    
# spullen reedswitch
import os
import wiringpi
os.system('gpio export 19 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(19,io.INPUT)

# spullen Adafruit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit()

# spullen om de string van de website in te lezen
url = 'http://planetarium.chrisdemoor.nl/positions.txt'

schakelaar = "open"
teller = 1
positiestring     = ""
positiestring_oud = "001001001001001001001001001"
totaalteller = 1

# bij de eerste keer opstarten wachten totdat alle processen in de Pi zijn opgestart (anders hapert de stepper tijdens het rijden)
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
    while (schakelaar == "open"):
      if planeet != "DMO-Mars":
         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      else:
         kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   
      if (io.digitalRead(19)):  
        schakelaar = "open"
      else:
        if teller > 200:
          schakelaar = "dicht"
      teller +=1
      
    sleep(1)  
   
    # BEREKENING AANTAL STAPPEN 
    nieuwe_positie_planeet = int(positiestring[beginpos_string:eindpos_string])
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
      if planeet != "DMO-Mars":
         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      else:
         kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   

      teller +=1

    
    sleep (1)
   
  # 10 seconden wachten omdat anders de GET teveel requests doet naar de server en ons weigert
  sleep (10)
  totaalteller +=1
  kit.stepper1.release() 
      
  positiestring_oud = positiestring
  schakelaar = "open"
  teller = 1

