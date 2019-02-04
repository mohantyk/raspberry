#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:03:40 2019

@author: kaniska
"""

import MPU6050 
import time

mpu = MPU6050.MPU6050()
accel = [0]*3 # Store accelrator data
gyro = [0]*3 # Store gyroscope data

def setup():
    mpu.dmp_initialize() # Initialize 
    
def loop():
    while True:
        accel = mpu.get_acceleration()
        gyro = mpu.get_rotation()
        
        print('Acceleration: {}'.format(accel))
        print('Gyroscope: {}'.format(gyro))
        print(' ') 
        time.sleep(0.5)
        

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        pass

