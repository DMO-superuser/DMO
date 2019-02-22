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
  print (positiestring[0:3])
