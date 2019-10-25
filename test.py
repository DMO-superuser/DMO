import time

import Adafruit_DHT

from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
    print (sensor)
    print (sensor.id)
    print (sensor.id, sensor.get_temperature())


