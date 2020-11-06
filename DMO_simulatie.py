import socket
planeet = socket.gethostname()
if (planeet == "DMO-Saturnus"):
   totaal_stappen = 6683 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 350  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 15  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 18  # de eindpositie in de string bij de Curl van deze planeet
   wachttijd_simulatie = 0.0748 # de wachtijd als DMO in simulatie gaat   
if (planeet == "DMO-Jupiter"):
   totaal_stappen = 4326 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 350  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 12  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 15  # de eindpositie in de string bij de Curl van deze planeet
   wachttijd_simulatie = 0.0434 # de wachtijd als DMO in simulatie gaat   
if (planeet == "DMO-Mars"):
   totaal_stappen = 2776 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 77  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 9  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 12  # de eindpositie in de string bij de Curl van deze planeet
   wachttijd_simulatie = 0.0157 # de wachtijd als DMO in simulatie gaat   
if (planeet == "DMO-Aarde"):
   totaal_stappen = 1107 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 24   # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 6  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 9  # de eindpositie in de string bij de Curl van deze planeet 
   wachttijd_simulatie = 0.015 # de wachtijd als DMO in simulatie gaat
if (planeet == "DMO-Venus"):
   totaal_stappen = 1019 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 112  # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 3  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 6  # de eindpositie in de string bij de Curl van deze planeet 
   wachttijd_simulatie = 0.01 # de wachtijd als DMO in simulatie gaat
if (planeet == "DMO-Mercurius"):
   totaal_stappen = 202 # aantal stappen om een rondje te maken, 1% afwijking per keer
   magneet_positie = 175   # positie in graden waar de magneet van de planeet ligt
   beginpos_string = 0  # de beginpositie in de string bij de Curl van deze planeet
   eindpos_string  = 3  # de eindpositie in de string bij de Curl van deze planeet 
   wachttijd_simulatie = 0.0198 # de wachtijd als DMO in simulatie gaat   

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

kit = MotorKit()

while True:
 if planeet != "DMO-Mars":
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
 else:
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)   
 sleep (wachttijd_simulatie)
