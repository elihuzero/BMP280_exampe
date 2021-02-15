#!/usr/bin/python

import Adafruit_BMP.BMP280 as BMP280
sensor= BMP280.BMP280(address=0x76)

temp = int(sensor.read_temperature())
press = int(sensor.read_pressure()/100)

print (temp)
print (press)
