import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Jupiter"):
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Mars"):
   totaal_stappen = 2776 # aantal stappen om een rondje te maken, 1% afwijking per keer
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
 
stappen_per_graad = int(totaal_stappen / 360)   

# spullen reedswitch
import os
import wiringpi
from time import sleep
os.system('gpio export 26 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(26,io.INPUT)

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

testteller = 1

while True:
  r = requests.get(url, timeout=4)
  positiestring = r.text
  #print ("Aarde " + positiestring[6:9])
  #print ("Mars " +  positiestring[9:12])
  #print ("Jupiter " + positiestring[12:15])
  #print ("Saturnus " + positiestring[15:18])
  #print ("positiestring     " + positiestring)
  #print ("positiestring_oud " + positiestring_oud)

 # als er een nieuwe positie is ingegeven op de website
  if (positiestring != positiestring_oud) and (r.status_code == 200):   
      
    # EERST NAAR MAGNEET RIJDEN, die ligt op 001
    #while (schakelaar == "open"):
    #  kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    #  if (io.digitalRead(26)):  
    #    schakelaar = "open"
    #  else:
    #    if teller > 500:
    #      schakelaar = "dicht"
    #  teller +=1

   
    # BEREKENING AANTAL STAPPEN 
    aantal_graden_planeet = 360 - int(positiestring[beginpos_string:eindpos_string])
    aantal_stappen_te_lopen =  int(aantal_graden_planeet * stappen_per_graad)
    # VOOR TESTDOELEINDEN om sneller te testen
    aantal_stappen_te_lopen = 300
   
   
    # NU NAAR POSITIE RIJDEN 
    teller = 1
    while (teller < aantal_stappen_te_lopen):
      kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      teller +=1
    
    # motoren loslaten
    kit.stepper1.release()
   
  # 10 seconden wachten omdat anders de GET teveel requests doet naar de server en ons weigert
  sleep (10)
  print (testteller)
  testteller +=1
   
   
  positiestring_oud = positiestring
  schakelaar = "open"
  teller = 1

    

