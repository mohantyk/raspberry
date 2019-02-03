#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:09:28 2019

@author: kaniska
"""

import RPi.GPIO as GPIO
import time 
import math

buzzerPin = 11 # GPIO17
buttonPin = 12 # GPIO18

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    p = GPIO.PWM(buzzerPin, 1)
    p.start(0)
    
    
def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            print('buzzer on')
            alertor()
        else:
            print('buzzer off')
            stop_alertor()
            
def alertor():
    p.start(50) # Set Duty Cycle to 50
    for x in range(360):
        sinVal = math.sin(math.pi * x / 180)
        toneVal = 2000 + 500*sinVal
        p.ChangeFrequency(toneVal)  # Change the freq (duty cycle remains at 50)
        time.sleep(0.001)

def stop_alertor():
    p.stop()
            
            
def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)
    GPIO.cleanup()
    
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()