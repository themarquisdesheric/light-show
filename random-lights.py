from blinkt import set_pixel, set_brightness, set_clear_on_exit, show, clear
from random import randint
from time import sleep

set_brightness(0.05)
set_clear_on_exit()

def light_up():
  '''lights up in random colors for a second'''
  for pixel in range(8):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    set_pixel(pixel, r, g, b)
    show()
    sleep(0.1)
  sleep(1)

light_up()
