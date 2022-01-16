from rpi_ws281x import *

import led_accent_config as config

strip = Adafruit_NeoPixel(config.LED_COUNT,  config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS, config.LED_CHANNEL)
strip.begin()