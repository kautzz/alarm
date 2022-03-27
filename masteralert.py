#!/usr/bin/env python3

"""
Lab security with pi zero 2W, noir camera and motion.
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

    mqtt_msg = {
        "msg": "motion detected",
        "countdown": config['alarm']['countdown'],
        "strobe" : False,
        "horn" : False
    }

    client.connect("192.168.1.100",1883,60)
    client.publish(config['device']['name'], json.dumps(mqtt_msg))
    client.disconnect()


if __name__ == "__main__":
    main()

print('')
print('End of program')



