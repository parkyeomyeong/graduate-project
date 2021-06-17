# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = ""
CLIENT_ID = "re-id"
PATH_TO_CERT = ""
PATH_TO_KEY = ""
PATH_TO_ROOT = "certification2/root.pem"
MESSAGE = "Hello World"
TOPIC = "$aws/things/project/shadow/update"
RANGE = 1

class AWSClient():

    def __init__(self):
        self.myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
        self.myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
        self.myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

        self.myAWSIoTMQTTClient.connect()

    def mqttpublising(self, data):
        
        message = {"state" : { "reported" : { "section" : "entrance", "table" : data }}}
        self.myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1)
        print("Published: '" + json.dumps(message) + "' to the topic: " + TOPIC)
        t.sleep(0.1)


# print('Begin Publish')
# for i in range (RANGE):
#     # data = "{} [{}]".format(MESSAGE, i+1)
#     message = {"state" : { "reported" : { "section" : "sangsang1", "persons": 1 }}}
#     myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
#     print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
#     t.sleep(0.1)
# print('Publish End')
# myAWSIoTMQTTClient.disconnect()