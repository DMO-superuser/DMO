

import requests

url = 'https://www.estdigital.nl'


#while True:
r = requests.get(url)
positiestring = r.text
print (positiestring)
