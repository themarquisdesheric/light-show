from blinkt import set_pixel, set_brightness, set_clear_on_exit, show, clear
from random import randint
from time import sleep

set_brightness(0.1)
set_clear_on_exit()


def loop(pixel_range, r, g, b):
  '''animates lighting up the specified pixels in the specified color'''
  for pixel in pixel_range:
    set_pixel(pixel, r, g, b)
    show()
    sleep(0.1)


def oscillate():
  '''animated oscillating pattern in a random color'''
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)

  while True:
    loop(range(7), r, g, b)
    clear()
    loop(reversed(range(1, 8)), r, g, b)
    clear()


oscillate()
