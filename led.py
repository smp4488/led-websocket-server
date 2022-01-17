# combines two strips into one

from led_accent import strip as strip_accent
from led_visualizer import strip as strip_visualizer
from rpi_ws281x import Color

# import led_visualizer_config as config_visualizer
# import led_accent_config as config_accent

import time

# should be 90
# TOTAL_LED_COUNT = config_accent.LED_COUNT + config_visualizer.LED_COUNT
TOTAL_LED_COUNT = strip_visualizer.numPixels() + strip_accent.numPixels()
# 36 LEDs then the visualizer starts then the other 36 for the accent
LED_OFFSET = 36

global CURRENT_COLOR 
CURRENT_COLOR = (0,0,0) # off


# led matrix to turn to rows and visualizer strip into a matrix
LED_ROWS = 5
LED_COLUMNS = 18
# looking at it from the front, starts on the top left
led_martix = [ [71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54],
              [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53],
              [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17],
              [35, 34, 33. 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18],
              [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17] ]

def get_current_color():
  return CURRENT_COLOR

# set the color of both strips
def set_color(color):
  for i in range(TOTAL_LED_COUNT):
    get_strip_from_index(i).setPixelColor(get_corrected_led_index(i), color)

  strip_accent.show()
  strip_visualizer.show()

# set the color of both strips
def set_color_hex(hex):
  rgb = hexToRGB(hex)
  # global CURRENT_COLOR
  CURRENT_COLOR = rgb
  for i in range(TOTAL_LED_COUNT):
    get_strip_from_index(i).setPixelColor(get_corrected_led_index(i), Color(*(rgb)))

  strip_accent.show()
  strip_visualizer.show()

def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(TOTAL_LED_COUNT):
        # need to offset i to correct number for strip
        strip = get_strip_from_index(i)
        strip.setPixelColor(get_corrected_led_index(i), color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# get the strip based off the led index position
def get_strip_from_index(i):
  if (i >= LED_OFFSET and i < LED_OFFSET + strip_visualizer.numPixels()):
    return strip_visualizer
  else:
    return strip_accent

# get the corrected index for the approiate strip
def get_corrected_led_index(i):
  # need to offset i to correct number for strip
  # less than the off set return i
  if (i < LED_OFFSET):
    return i
  # at the second strip, pull the index back down to 0 until we get to the length of the second strip
  elif (i >= LED_OFFSET and i < LED_OFFSET + strip_visualizer.numPixels()):
    return i - LED_OFFSET
  # finally bring i back to where we left off
  else:
    return i - strip_visualizer.numPixels()

# https://stackoverflow.com/a/29643643
def hexToRGB(hex):
    h = hex.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# Execute this file to run a LED strand test
# If everything is working, you should see a red, green, and blue pixel scroll
# across the LED strip continuously
if __name__ == '__main__':
    try:

        # set a solid color not in a loop for testing
        # set_color(Color(255, 255, 255))

        while True:
            print ('Color wipe animations.')

            colorWipe(Color(255, 0, 0))  # Red wipe
            colorWipe(Color(0, 255, 0))  # Blue wipe
            colorWipe(Color(0, 0, 255))  # Green wipe
            # colorWipe(Color(0, 0, 0))  # Off wipe
            # print ('Theater chase animations.')
            # theaterChase(strip, Color(127, 127, 127))  # White theater chase
            # theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            # theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            # print ('Rainbow animations.')
            # rainbow(strip)
            # rainbowCycle(strip)
            # theaterChaseRainbow(strip)

    except KeyboardInterrupt:
      colorWipe(Color(0,0,0), 10)