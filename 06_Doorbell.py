#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:09:28 2019

@author: kaniska
"""

import RPi.GPIO as GPIO

buzzerPin = 11 # GPIO17
buttonPin = 12 # GPIO18

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(buzzerPin, GPIO.HIGH)
            print('buzzer on')
        else:
            GPIO.output(buzzerPin, GPIO.LOW)
            print('buzzer off')
            
def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)
    GPIO.cleanup()
    
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()