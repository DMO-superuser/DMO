import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 1  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Jupiter"):
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 1  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Mars"):
   totaal_stappen = 2776 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 1   # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Aarde"):
   totaal_stappen = 1107 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 16   # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet 
if (planeet == "DMO-Venus"):
   totaal_stappen = 1019 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 98  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 3  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 6  # de eindpositie in de string bij de Curl van deze planeet 
if (planeet == "DMO-Mercurius"):
   totaal_stappen = 202 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 191   # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 0  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 3  # de eindpositie in de string bij de Curl van deze planeet 
   
   
stappen_per_graad = int(totaal_stappen / 360)   

# spullen reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 19 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(19,io.INPUT)

# spullen Adafruit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep
kit = MotorKit()

# spullen op de string van de website in te lezen
import requests
url = 'http://planetarium.chrisdemoor.nl/positions.txt'

schakelaar = "open"
teller = 1
positiestring     = ""
positiestring_oud = "leeg"

while True:

  try:
    r = requests.get(url, timeout=4)
  except requests.exceptions.ConnectionError:
    positiestring = positiestring_oud

  positiestring = r.text

  #print ("Mercurius " + positiestring[0:3])
  print ("Venus " + positiestring[3:6])
  print ("Aarde " + positiestring[6:9])
  #print ("Mars " +  positiestring[9:12])
  #print ("Jupiter " + positiestring[12:15])
  #print ("Saturnus " + positiestring[15:18])
  #print ("positiestring     " + positiestring)
  #print ("positiestring_oud " + positiestring_oud)

 # als er een nieuwe positie is ingegeven op de website
  if (positiestring != positiestring_oud):   
      
    # EERST NAAR MAGNEET RIJDEN, die ligt op 001
    while (schakelaar == "open"):
      if planeet != "DMO-Mars":
         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      else:
         kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   
      if (io.digitalRead(19)):  
        schakelaar = "open"
      else:
        if teller > 100:
          schakelaar = "dicht"
      teller +=1

   
    # BEREKENING AANTAL STAPPEN 
    nieuwe_positie_planeet = int(positiestring[beginpos_string:eindpos_string])
    stappen_per_graad = int(totaal_stappen/360)
    if (nieuwe_positie_planeet < magneet_positie) and (nieuwe_positie_planeet > 0):
       aantal_stappen_te_lopen = (magneet_positie - nieuwe_positie_planeet) * stappen_per_graad
    else:
       aantal_stappen_te_lopen =  ((360- nieuwe_positie_planeet)+ magneet_positie) * stappen_per_graad 
   
    print ("---------------------------------------------")
    print ("nieuwe_positie_planeet " + str(nieuwe_positie_planeet))
    print ("stappen_per_graad " + str(stappen_per_graad))
    print ("magneet_positie " + str(magneet_positie))
    print ("aantal_stappen_te_lopen " + str(aantal_stappen_te_lopen))      
    print ("---------------------einde-------------------------")      
   
    # NU NAAR POSITIE RIJDEN 
    teller = 1
    while (teller < aantal_stappen_te_lopen):
      if planeet != "DMO-Mars":
         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      else:
         kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   

      teller +=1
    
  
   
  # 10 seconden wachten omdat anders de GET teveel requests doet naar de server en ons weigert
  sleep (10)
   
  kit.stepper1.release() 
      
  positiestring_oud = positiestring
  schakelaar = "open"
  teller = 1

    

