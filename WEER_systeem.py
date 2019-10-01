# diversen
from time import sleep

# GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) # pin7

# motor HAT stack
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit1 = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)
#kit4 = MotorKit(address=0x63)

# Apache index.html op http://192.168.178.94/
apache_indexfile = "/var/www/html/index.html"
log_regel = open(apache_indexfile, "w")


while True:

  ########################
  # BINNENTEMPERATUUR B0M1
  ########################
  # single coil steps, 500 stappen rond
  devicedir = glob.glob("/sys/bus/w1/devices/28-00000809ac91/")
  device = devicedir[0] + "w1_slave"
  # open up the file - temperatuur met DS18B20
  f = open (device, 'r')
  sensor = f.readlines()
  f.close()
  # parse results from file - temperatuur met DS18B20
  # temperatuur wordt op een 10e graad uitgelezen
  # single coil steps, 513 stappen rond
  # range = van -10 tot 40 graden, 500 stappen nodig. 100 stappen per 10 graden
  # ijkpunt = 0 + 6 voor de eerste, hij begint op -10 graden C (= 100 stappen) 
  crc = sensor[0].split()[-1]
  temp = float(sensor[1].split()[-1].strip('t='))
  temp_C = (temp/1000.000)
  temp_C = round(temp_C,1)
  log_regel.write("<p> Dit is de eerste regel </p>")
  log_regel.write(temp_C)

