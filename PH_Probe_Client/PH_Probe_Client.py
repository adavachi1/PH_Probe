import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import configparser
import requests
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

while True:

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get the URI from the configuration file
    uri = config['URI']['url']

    # Get the PH sensor details from the configuration file
    i2c_bus = int(config['PH_SENSOR']['i2c_bus'])
    i2c_address = int(config['PH_SENSOR']['i2c_address'], 0)
    adc_channel = int(config['PH_SENSOR']['adc_channel'])

    # Get the POST request details from the configuration file
    headers = dict(header.split(': ') for header in config['POST_REQUEST']['headers'].splitlines())
    payload_template = config['POST_REQUEST']['payload_template']

    # Initialize the I2C bus and ADC channel
    # (Assuming you have already installed the necessary libraries and imported them in your code)
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c, address=i2c_address)
    chan = AnalogIn(ads, adc_channel)

    # Read the PH value from the sensor
    ph_value = chan.voltage

    # Create the payload by formatting the PH value into the payload template
    payload = payload_template % ph_value

    # Send the POST request to the URI with the payload and headers
    response = requests.post(uri, data=payload, headers=headers)
    time.sleep(1)
