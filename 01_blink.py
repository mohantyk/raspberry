#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 08:55:04 2018

@author: kaniska
"""

import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print('Usig pin {0} to toggle led'.format(ledPin))
    
def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print('LED ON...')
        time.sleep(1)
        
        GPIO.output(ledPin, GPIO.LOW)
        print('...LED OFF')
        time.sleep(1)
        
        
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()
    print('Cleaned up resources. Board ready for reuse.')
    
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
