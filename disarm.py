#!/usr/bin/env python3

"""
Lab security with pi zero 2W, noir camera and motion.
"""

import time
import datetime
import paho.mqtt.client as mqtt
import json

from subprocess import check_call

from configparser import ConfigParser
config = ConfigParser()
config.read('settings.ini')

client = mqtt.Client(config['device']['name'] + "_pub", False)

def main():

    check_call(["pkill", "-9", "-f", "masteralert.py"])
    print("disarmed!")

    mqtt_msg = {
        "msg": "disarmed",
        "alarm": False,
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



