# Continuous MQ-2 Gas Sensor Read
# Author: Grecia Francisco and Michelle Tran
 
# Libraries needed
import time
import board 
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import logging
from ovos_bus_client import MessageBusClient, Message
import RPi.GPIO as GPIO

# Set up Indicator LEDs
GPIO.setmode(GPIO.BCM)
greenLed = 16
redLed = 20
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)
GPIO.output(greenLed, GPIO.LOW)
GPIO.output(redLed, GPIO.LOW)
GPIO.output(greenLed, GPIO.HIGH) # initial state

# Setting up client to connect to a local mycroft instance
client = MessageBusClient()
client.run_in_thread()
# Sending speak message
client.emit(Message('speak', data={'utterance': 'Reading MQ-2 Sensor'}))

#Create log file
logging.basicConfig(filename='MQ-2.log', format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

# Create the I2C bus 
i2c = busio.I2C(board.SCL, board.SDA)

#Create the ADS object using the I2C bus
ads = ADS.ADS1015(i2c)

#Create single-ended input on channel 0 (Analog Pin 0)
channelA0 = AnalogIn(ads, ADS.P0)

logging.info("MQ2 Warming Up!")
time.sleep(5) # Give 5 seconds to warm up

try:
	while True:
		formatted_output = f"raw value: {channelA0.value}     voltage: {channelA0.voltage:.3f} volts"
		time.sleep(0.5) # allow delay between every read of about .5 sec
		logging.info(formatted_output)
		if channelA0.value >= 10000:
			GPIO.output(greenLed, GPIO.LOW)
			GPIO.output(redLed, GPIO.HIGH)
		else:
			GPIO.output(greenLed, GPIO.HIGH)
			GPIO.output(redLed, GPIO.LOW)	
		# client.emit(Message('speak', data={'utterance': str(channelA0.value)}))
except Exception:
	GPIO.cleanup()
