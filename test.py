import os
teller = 1
bestand = open("/home/pi/DMO/DMO.wifi","a")



while True:

  hostname = "google.com" #example
  response = os.system("ping -c 1 " + hostname)

  #and then check the response...
  if response == 0:
     bestand.write (str(teller)  + " up \n")
  else:
     bestand.write (str(teller)  + " down \n")
     bestand.close()
     os.system('sudo shutdown -r now')

  teller +=1
  
  
