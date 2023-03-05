from FrontDoor import FrontDoor
from gpiozero import Button
import time
import requests
import json
import pygame
pygame.init()

bell1 = pygame.mixer.Sound("/home/pi/Downloads/ES_Time Melody Clock - 10db.wav")
button = Button(24)
pair = 0

def capture():
    global pair
    time.sleep(.5)
    if button.value == 0:
        webhook_url = 'https://hook.us1.make.com/v9gjorbj4s2wqr1fq1u6nch5katfmn9u'
        data = { 'stuff': 'THIS IS Eds',
             'lala': 'Dinger'
             }
        r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    
        webhook_url = 'https://hook.us1.make.com/iw73i9w2pmizs5wuye7msjfusv1jm11u'
        data = { 'stuff': 'THIS IS Bens',
             'lala': 'Dinger'
             }
        r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    
    
        bell1.play()
        FrontDoor(pair)
        if pair == 0:
            pair = 1
        else:
            pair = 0
    

button.when_released = capture
