#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:08:28 2018

@author: kaniska
"""

import RPi.GPIO as GPIO
import time

ledPin = 12
sleepTime = 0.01
freq = 1000

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    p = GPIO.PWM(ledPin, freq)
    p.start(0)
    
def loop():
    while True:
        print('Increasing duty cycle')
        for duty_cycle in range(0,101,1):
            p.ChangeDutyCycle(duty_cycle)
            time.sleep(sleepTime)
        time.sleep(0.5)
        
        print('Decreasing duty cycle')
        for duty_cycle in range(100,-1,-1):
            p.ChangeDutyCycle(duty_cycle)
            time.sleep(sleepTime)
        time.sleep(0.5)
    
    
def destroy():
    p.stop()
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()
    


if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
