

import requests

url = 'https://www.bdsmzaken.nl'


#while True:
r = requests.get(url)
positiestring = r.text
print (positiestring)
