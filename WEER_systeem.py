from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep

# motor HAT stack
kit1 = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)
#kit4 = MotorKit(address=0x63)

# Apache index.html op http://192.168.178.94/
apache_indexfile = "/var/www/html/index.html"
log_regel = open(apache_indexfile, "w")



log_regel.write("<p> Dit is de eerste regel </p>")
log_regel.write("<p> Dit is de tweede regel </p>")

