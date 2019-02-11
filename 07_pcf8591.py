#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 04:24:13 2019

@author: kaniska
"""

from smbus import SMBus
import time

address = 0x48 # Default address for PCF8591 
bus = SMBus(1) # use i2c channel 1 (SDA/SCL 1) - Rpi 3 uses channel 1
cmd = 0x40  # See Fig. 4 in https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf 
            # Bit 7 turns on the analog output flag
            # Input channels are LSBs 0 and 1 (see analogRead below)
            
def analogRead(channel):
    complete_cmd = cmd + channel # set LSBs 0 and 1 for input channels 0-3
    value = bus.read_byte_data(complete_cmd)
    return value

def analogWrite(value):
    bus.write_byte_data(address, cmd, value)
    
def loop():
    while True:
        value = analogRead(0) # Read input from ADC 0
        analogWrite(value)    # Write DAC value
        voltage = 3.3*value/255.0
        print('ADC value: {}, Voltage: {:.2f}'.format(value, voltage))
        time.sleep(0.01)
        
def destroy():
    bus.close()
    
if __name__=='__main__':
    print('Starting program...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()