# string van website genereren zodat alle mogelijke posities van een planeet getest kunnen worden
# positie loopt van 001 tot en met 360

# IP adres van de webserver is: hostname -I
# Apachewebserver heeft als file /var/www/html/positions.txt
# en is dan te benaderen via http://192.168.178.52/positions.txt

f = open("/var/www/html/positions.txt", "w")


for x in range(6):
 f.write(str(x))

f.close()
