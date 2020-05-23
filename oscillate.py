from blinkt import set_pixel, set_brightness, set_clear_on_exit, show, clear
from random import randint
from time import sleep

# OH GOD PLEASE HELP HANNAH WHY DOESN'T THIS SIMPLE THING WORK

set_brightness(0.1)
set_clear_on_exit()


def loop(pixel_range, r, g, b):
  for pixel in pixel_range:
    set_pixel(pixel, r, g, b)
    show()
    sleep(0.1)


def loop_range(pixel_range):
  def inner_loop(r, g, b):
    '''animates lighting up the specified pixels in the specified color'''
    for pixel in pixel_range:
      set_pixel(pixel, r, g, b)
      show()
      sleep(0.1)

  return inner_loop


loop_up = loop_range(range(7))
# BUT WHY MUST I RESORT TO THIS HANNAH? WHY WOULD I HAVE TO LIVE IN SUCH A WORLD?
loop_down = loop_range([7, 6, 5, 4, 3, 2, 1])

# if this worked... 
# loop(reversed(range(1, 8)), r, g, b)

# why doesn't this work?
# loop_down = loop_range(reversed(range(1, 8)))


def oscillate():
  '''animated oscillating pattern of a random color'''
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)

  while True:
    # loop(range(7), r, g, b)
    loop_up(r, g, b)
    clear()
    # loop(reversed(range(1, 8)), r, g, b)
    loop_down(r, g, b)
    clear()


oscillate()
