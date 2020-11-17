import requests

def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False

f= open("DMO.log","w+")    

for i in range(10):    
  if checkInternetRequests():
     print (' we hebben verbinding ')
     f.write( ' online ')
  else:
     print (' off line ')
     f.write( ' off line ')

f.close()
