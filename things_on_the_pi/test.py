from signal import pause
import pygame
pygame.init()

bell1 = pygame.mixer.Sound("/home/pi/Downloads/ES_PREL Glitch 11 - SFX Producer-1.wav")

def bells():
    print('bells n stuff ;)')
    bell1.play()
bells()
    
