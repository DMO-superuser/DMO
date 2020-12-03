import system
dt_string = "12:00"
bestand = open("/home/pi/DMO/DMO.wifi","a")
bestand.write (dt_string + " WiFi verbroken \n")
bestand.close()
os.system('sudo shutdown -r now')
