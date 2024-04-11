# Continuous MQ-2 Gas Sensor Read
# Author: Grecia Francisco and Michelle Tran
 
# Libraries needed
import time
import board 
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus 
i2c = busio.I2C(board.SCL, board.SDA)

#Create the ADS object using the I2C bus
ads = ADS.ADS1015(i2c)
ads.gain = 8

#Create single-ended input on channel 0 (Analog Pin 0)
chan = AnalogIn(ads, ADS.P0)

#Create differential input between channel 0 and 1 
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("MQ2 Warming Up!")
time.sleep(5) # Give 5 seconds to warm up

while True:
	print(f"raw value: {chan.value}     voltage: {chan.voltage:.3f} volts")
	time.sleep(0.5) # allow delay between every read of about .5 sec
