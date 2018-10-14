#elke planeet heeft 4 posities in de string
#mercurius
#venus
#aarde
#mars
#jupiter
#saturnus

import requests

url = 'http://planetarium.chrisdemoor.nl'
planeet = 'venus'

r = requests.get(url)
positiestring = r.text.decode("utf8")


print (positiestring)
print positiestring[2:5]
plaats =  int(positiestring[2:5]) + 1
print plaats
