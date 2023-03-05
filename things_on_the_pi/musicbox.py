from gpiozero import MotionSensor
from signal import pause
import pygame
import curses
pygame.init()




bell1 = pygame.mixer.Sound('/home/pi/Downloads/ES_PREL Glitch 11 - SFX Producer-1.wav')
actions = {
    curses.KEY_UP:    bell1.play(),
    #curses.KEY_DOWN:  robot.backward,
    #curses.KEY_LEFT:  robot.left,
    #curses.KEY_RIGHT: robot.right,
}




def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            robot.stop()

curses.wrapper(main)


def bells():
    pring('bells n stuff ;)')
    bell1.play()

# pir = MotionSensor(4)
# pir.when_motion =
# pir.when_no_motion =

# pause()