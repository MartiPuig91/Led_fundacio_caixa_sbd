#!/usr/bin/env python3


import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
maxTMP = 50 # The maximum temperature in Celsius after which we trigger the fan
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    #print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp

def Led1():
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.LOW)
    sleep(1)
def Led2():
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    sleep(1)

def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        Led1()
    else:
        Led2()
    return()

try:
    setup()
    while True:
        getTEMP()
    sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this program
