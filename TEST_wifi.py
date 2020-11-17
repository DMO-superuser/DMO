import requests
from datetime import datetime

def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False

f= open("DMO.log","w+")    

for i in range(1000):    
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#sleep (10)    
    
  if checkInternetRequests():
     print (i,' ',dt_string, ' we hebben verbinding ')
     f.write(str(i) + dt_string + ' online  \r\n')
  else:
     print (i,' ',dt_string, ' off line ')
     f.write(str(i) + dt_string + ' off line  \r\n')

f.close()
