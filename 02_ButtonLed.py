#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 12:38:11 2018

@author: kaniska
"""

import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(ledPin, GPIO.HIGH)
            print('LED ON')
        else: 
            GPIO.output(ledPin, GPIO.LOW)
            print('LED OFF')
            
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()
    print('\nCleaned up resources. Board ready for reuse')
    

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()