#elke planeet heeft 4 posities in de string
#mercurius
#venus
#aarde
#mars
#jupiter
#saturnus

import requests

url = 'http://planetarium.chrisdemoor.nl/positions.txt'
planeet = 'venus'
positiestring_oud = ""

while True:
 r = requests.get(url)
 positiestring = r.text
 
 if (positiestring_oud != positiestring):
  positiestring_oud = positiestring
  print (positiestring)
  print ("Mercurius " + positiestring[0:3])
  print ("Venus " + positiestring[3:6]) 
  print ("Aarde " + positiestring[6:9])
  print ("Mars " +  positiestring[9:12])
  print ("Jupiter " + positiestring[12:15])
  print ("Saturnus " + positiestring[15:18])
