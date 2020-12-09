

import requests

url = 'https://fetlife.com/p/netherlands/zuid-holland/kinksters?page=2'


#while True:
r = requests.get(url)
positiestring = r.text
print (positiestring)
