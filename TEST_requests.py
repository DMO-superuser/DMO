import requests
response = requests.get('http://planetarium.chrisdemoor.nl/positions.txt')
print (response.status_code)
print (response.content)
print (response.headers)
