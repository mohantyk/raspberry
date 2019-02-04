#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 07:57:08 2019

@author: kaniska
"""

import RPi.GPIO as GPIO
import time

trig_pin = 16
echo_pin = 18
MAX_DISTANCE = 220 # cms
timeout = MAX_DISTANCE * 60 # usecs

def setup():
    print('Program is starting')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    

def loop():
    while True:
        distance = get_sonar()
        print('The distance is {:.2f} cms'.format(distance))
        time.sleep(1)
        

def destroy():
    GPIO.output(trig_pin, GPIO.LOW)
    GPIO.cleanup()
    
    
def get_sonar():
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001) # 10 us pulse
    GPIO.output(trig_pin, GPIO.LOW)
    ping_time = pulse_in(echo_pin, GPIO.HIGH, timeout) # usecs
    distance = ping_time * 340.0 / 2.0 / 10000.0 # sound of speed is 340 m/s
    return distance
    
    
def pulse_in(pin, pulse_level, max_wait):
    ''' 
    Returns pulse duration in usecs 
    inputs:
        pin: GPIO pin
        pulse_level: level of the pulse (high/low)
        max_wait: maximum waiting time (in usecs)
    '''
    t0 = time.time()
    while GPIO.input(pin) != pulse_level: # No pulse yet
        if (time.time() - t0 > max_wait * 0.000001) :
            print('No pulse found')
            return 0
    
    t0 = time.time()
    while GPIO.input(pin) == pulse_level: # Pulse detected
        if (time.time() - t0 > max_wait * 0.000001) :
            print('Pulse found but waited too long')
            return 0
    pulse_time = (time.time() - t0)*(10**6) #usecs
    return pulse_time
    
        
        
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()