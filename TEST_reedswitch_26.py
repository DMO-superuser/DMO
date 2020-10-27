import os
import wiringpi
from time import sleep

os.system('gpio export 26 in')
sleep(0.5)
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
io.pinMode(26,io.INPUT)

while True:
 if (io.digitalRead(26)):
     print ("open")
 else:
     # onder de schakelaar
     print ("dicht")
 sleep(0.05)
