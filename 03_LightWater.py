#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:03:21 2018

@author: kaniska
"""

import RPi.GPIO as GPIO
import time

pins = [11,13,15,12,16]

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        
def loop():
    while True:
        for pin in pins:
            print('Turning pin {} on.'.format(pin))
            GPIO.setup(pin, GPIO.LOW)
            time.sleep(0.1)
            print('Turning pin {} off.'.format(pin))
            GPIO.setup(pin, GPIO.HIGH)
            
        for pin in pins[::-1]:
            print('Turning pin {} on.'.format(pin))
            GPIO.setup(pin, GPIO.LOW)
            time.sleep(0.1)
            print('Turning pin {} off.'.format(pin))
            GPIO.setup(pin, GPIO.HIGH)
            
def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()
    print('\nCleaned up resources. Board ready for reuse.')
        


if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
