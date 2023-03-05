from FrontDoor import FrontDoor
from gpiozero import Button
import time

button = Button(24)
pair = 0

def capture():
    global pair
    time.sleep(.5)
    if button.value == 0:

        FrontDoor(pair)
        if pair == 0:
            pair = 1
        else:
            pair = 0
    

button.when_released = capture
