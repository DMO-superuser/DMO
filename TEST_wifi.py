import requests

def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False
        
if checkInternetRequests():
   print (' we hebben verbinding ')
else:
   print (' off line ')
