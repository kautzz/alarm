#!/usr/bin/env python3

"""
Lab security with pi zero 2W ,noir camera and motion.
"""

import time
import datetime
import paho.mqtt.client as mqtt
import json

from configparser import ConfigParser
config = ConfigParser()
config.read('settings.ini')

client = mqtt.Client(config['device']['name'] + "_pub", False)

def main():
    print("master alarm!")
