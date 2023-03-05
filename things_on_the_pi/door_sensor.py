import pygame
pygame.init()

bell1 = pygame.mixer.Sound("/home/pi/Downloads/ES_PREL Glitch 11 - SFX Producer-1.wav")

def bells():
    print('bells n stuff ;)')
    bell1.play()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) # set up pin ?? (one of the above listed pins) as an input with a pull-up resistor

while True:
    if GPIO.input(18) == GPIO.HIGH:
        bells()
    if GPIO.input(18) == GPIO.LOW:
        print('CLOSED')