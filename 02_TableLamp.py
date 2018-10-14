#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 13:05:53 2018

@author: kaniska
"""

import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12

ledState = GPIO.LOW

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

def buttonPress(pin):
    global ledState    
    ledState = not ledState
    
    if ledState:
        print('LED ON - pin {0}'.format(pin))
    else:
        print('LED OFF - pin {0}'.format(pin))
    GPIO.output(ledPin, ledState)
        
        
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()
    print('\nCleaned up resources. Board ready for reuse.')
        
    
def loop():
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, buttonPress, bouncetime=300)
    while True:
        pass
    
if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()