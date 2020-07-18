import requests
response = requests.get('http://planetarium.chrisdemoor.nl/positions.txt', timeout = 4)
print (response.status_code)
print (response.content)
print (response.headers)
