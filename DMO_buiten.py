import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   steppersoort = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   planeet_magneet = 346 # begin van het magneetveld van de planeet
   stappen_per_graad = totaal_stappen / 360
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Jupiter"):
   steppersoort = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   planeet_magneet = 321 # begin van het magneetveld van de planeet
   stappen_per_graad = totaal_stappen / 360
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Mars"):
   steppersoort = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 2596 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Aarde"):
   steppersoort = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 2000 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Venus"):
   steppersoort = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 20778 # aantal stappen om een rondje te maken, 1% afwijking per keer, bij Seq2 en Stepcount2
   #totaal_stappen = 10591 # aantal stappen om een rondje te maken, 1% afwijking per keer, bij Seq1 en Stepcount1
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet      
if (planeet == "DMO-Mercurius"):
   steppersoort = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 4099 # aantal stappen om een rondje te maken, 1% afwijking per keer, bij Seq2 en Stepcount2
   #totaal_stappen = 2067 # aantal stappen om een rondje te maken, 1% afwijking per keer, bij Seq1 en Stepcount1
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Aarde"):
   steppersoort = "binnen"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 20645 # aantal stappen om een rondje te maken, 1% afwijking per keer, bij Seq2 en Stepcount2
   #totaal_stappen = 10335 # aantal stappen om een rondje te maken, 1% afwijking per keer, bij Seq1 en Stepcount1
   begin_stappen = 14   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet      

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

while True:
  r = requests.get(url)
  positiestring = r.text
  #print ("Aarde " + positiestring[6:9])
  #print ("Mars " +  positiestring[9:12])
  #print ("Jupiter " + positiestring[12:15])
  #print ("Saturnus " + positiestring[15:18])

 # als er een nieuwe positie is ingegeven op de website
  if (positiestring != positiestring_oud):   
      
    # EERST NAAR SCHAKELAAR RIJDEN 
    while (schakelaar == "open"):
      kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      if (io.digitalRead(26)):  
        schakelaar = "open"
      else:
        if teller > 500:
          schakelaar = "dicht"
      teller +=1

    # BEREKENING AANTAL STAPPEN 
    aantal_graden_planeet = 360 - int(positiestring[beginpos_string:eindpos_string])
    if (aantal_graden_planeet > planeet_magneet):
      aantal_graden_planeet = aantal_graden_planeet - planeet_magneet
    else:
      aantal_graden_planeet = (360 - planeet_magneet) + aantal_graden_planeet
    aantal_stappen_te_lopen =  int(aantal_graden_planeet * stappen_per_graad)

    # NU NAAR POSITIE RIJDEN 
    teller = 1
    while (teller < aantal_stappen_te_lopen):
      kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
      teller +=1
   
    positiestring_oud = positiestring
    schakelaar = "open"
    teller = 1

    

