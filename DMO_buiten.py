import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   steppersoort = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = 154   # het magneetje ligt op een willekeurige plek in het planetarium, dat is niet noodzakelijkerwijs het begin van de graden-berekening
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
if (planeet == "DMO-Jupiter"):
   steppersoort = "buiten"    # er bestaan binnen- en buitensteppers 
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   begin_stappen = totaal_stappen - 3438   # aantal stappen van 20 augustus (nulpunt Aarde) naar magneet planeet
   stappen_per_graad = totaal_stappen / 360
   # Mercurius 0 en 3, Venus 3 en 6, Aarde 6 en 9, Mars 9 en 12, Jupiter 12 en 15, Saturnus 15 en 18
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

while (positiestring_oud != positiestring):
  r = requests.get(url)
  positiestring = r.text
   
  # EERST NAAR SCHAKELAAR RIJDEN 
  while (schakelaar == "open"):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    if (io.digitalRead(26)):
      #print ("open")
      schakelaar = "open"
    else:
      # onder de schakelaar
      #print ("dicht")
      #print (teller)
      if teller > 1500:
        schakelaar = "dicht"
    teller +=1

  # BEREKENING AANTAL STAPPEN VANAF MAGNEET
  # procentueel verschil met de aarde 
  aantal_graden_planeet = 360 - int(positiestring[beginpos_string:eindpos_string])
  aantal_graden_aarde = 360 - int(positiestring[6:9])
  verhouding_tot_aarde = aantal_graden_planeet / aantal_graden_aarde

  print (positiestring)
  print ("verhouding tot aarde")
  print (verhouding_tot_aarde)   

  # bepaal aantal graden dat de Aarde te lopen heeft vanaf nulpunt Aarde (20 augustus)
  aantal_graden_positiestring = 360 - int(positiestring[6:9])
  aantal_graden_nulpunt_aarde = 236 # begin magneet veld = 20 augustus
  aantal_graden_tot_23_dec = 360 - aantal_graden_nulpunt_aarde
  if (aantal_graden_positiestring > aantal_graden_nulpunt_aarde):
    # de datum ligt voor 23 december
    aantal_graden_te_lopen = aantal_graden_positiestring - aantal_graden_nulpunt_aarde   
  else:  
    aantal_graden_te_lopen = aantal_graden_tot_23_dec + aantal_graden_positiestring   
  # voeg verhouding toe
  aantal_graden_te_lopen = aantal_graden_te_lopen * verhouding_tot_aarde
  # bereken aantal stappen
  aantal_stappen_te_lopen = int(aantal_graden_te_lopen * stappen_per_graad) - begin_stappen

  print ("aantal graden te lopen")
  print (aantal_graden_te_lopen)
  print ("aantal stappen te lopen")
  print (aantal_stappen_te_lopen)
   
   
  # NU NAAR POSITIE RIJDEN 
  teller = 1
  while (teller < aantal_stappen_te_lopen):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    teller +=1
   
  positiestring_oud = positiestring

    
