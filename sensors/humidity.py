#!/usr/bin/python3

"""
Measure humidity with the DHT11 sensor
https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
"""

import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 21)
result = instance.read()

if result.is_valid():
  print("Temperature: %-3.1f C" % result.temperature)
  print("Humidity: %-3.1f %%" % result.humidity)
else:
  print("Error: %d" % result.error_code)

