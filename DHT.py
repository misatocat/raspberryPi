import sys

import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
 
print temperature, humidity


