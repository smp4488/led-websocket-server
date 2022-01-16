# combines two stips into one

from led_accent import strip as strip_accent
from led_visualizer import strip as strip_visualizer

# import led_visualizer_config as config_visualizer
# import led_accent_config as config_accent

import time

# should be 90
# TOTAL_LED_COUNT = config_accent.LED_COUNT + config_visualizer.LED_COUNT
TOTAL_LED_COUNT = strip_visualizer.numPixels() + strip_accent.numPixels()
# 36 LEDs then the visualizer starts then the other 36 for the accent
LED_OFFSET = 36

# set the color of both strips
def set_color(color):
  for i in range(TOTAL_LED_COUNT):
    get_strip_from_indes(i).setPixelColor(i, color)

  strip_accent.show()
  strip_visualizer.show()

# get the strip based off the led index position
def get_strip_from_indes(i):
  if (i >= LED_OFFSET and i < LED_OFFSET + strip_visualizer.numPixels()):
    return strip_visualizer
  else:
    return strip_accent

def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(TOTAL_LED_COUNT):
        get_strip_from_indes(i).setPixelColor(i, color)
        get_strip_from_indes(i).show()
        time.sleep(wait_ms/1000.0)

# Execute this file to run a LED strand test
# If everything is working, you should see a red, green, and blue pixel scroll
# across the LED strip continuously
if __name__ == '__main__':
    try:

        while True:
            print ('Color wipe animations.')
            colorWipe(Color(255, 0, 0))  # Red wipe
            colorWipe(Color(0, 255, 0))  # Blue wipe
            colorWipe(Color(0, 0, 255))  # Green wipe
            # print ('Theater chase animations.')
            # theaterChase(strip, Color(127, 127, 127))  # White theater chase
            # theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            # theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            # print ('Rainbow animations.')
            # rainbow(strip)
            # rainbowCycle(strip)
            # theaterChaseRainbow(strip)

    except KeyboardInterrupt:
      colorWipe(strip, Color(0,0,0), 10)