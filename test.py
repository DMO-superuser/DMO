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
 print (temp_C)
