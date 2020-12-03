import system
import requests
from datetime import datetime
from time import sleep

def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        #print(ex)
        sleep(1)
        return False

f= open("DMO.wifi","a")    

for i in range(100000):    
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

  sleep (1)    
    
  if checkInternetRequests():
     print (i,'',dt_string, ' we hebben verbinding ')
     f.write(str(i) + ' ' + dt_string + ' online  \r\n')
  else:
     print (i,' ',dt_string, ' off line ')
     f.write(str(i) + ' ' + dt_string + ' off line en REBOOT \r\n')
     f.close()
     os.system('sudo shutdown -r now')

f.close()
