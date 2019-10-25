import time

import Adafruit_DHT

from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

print("Sensor1 has temperature %.2f" % (1, sensor.get_temperature()))
print("Sensor2 has temperature %.2f" % (2, sensor.get_temperature()))
