# string van website genereren zodat alle mogelijke posities van een planeet getest kunnen worden
# positie loopt van 001 tot en met 360

# IP adres van de webserver is: hostname -I
# Apachewebserver heeft als file /var/www/html/positions.txt
# en is dan te benaderen via http://192.168.178.52/positions.txt




for x in range(19):
 f = open("/var/www/html/positions.txt", "w")
 afdruk = ""
 teller = x + 1
 if teller < 100:
    afdruk = "0" + str(teller)
    if teller < 10:
       afdruk = "0" + afdruk
 else:
    afdruk = str(teller)
 afdruk = afdruk + "001001001001001"     
 f.write(afdruk)
 f.close()
