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

#Create single-ended input on channel 0 (Analog Pin 0)
channelA0 = AnalogIn(ads, ADS.P0)

print("MQ2 Warming Up!")
time.sleep(5) # Give 5 seconds to warm up

while True:
	print(f"raw value: {channelA0.value}     voltage: {channelA0.voltage:.3f} volts")
	time.sleep(0.5) # allow delay between every read of about .5 sec
