from rpi_ws281x import Color
import logging
import json

class Effect:
  logger = logging.getLogger()
  running = False
  def __init__(self, options):
      self.name = options['name']
      self.description = options['description']
      self.title = options['title']
      self.running = False
      # self.logger = logging.getLogger()

      # self.options = options

  # async def start(self, options):
  #   self.running = True
  #   await self.run(options)

  def start(self, options):
    self.running = True
    self.run(options)

  def stop(self):
    self.running = False

  def run(self, options):
    pass

  def toJSON(self):
    return self.__dict__

  def wheel(self, pos):
      """Generate rainbow colors across 0-255 positions."""
      if pos < 85:
          return Color(pos * 3, 255 - pos * 3, 0)
      elif pos < 170:
          pos -= 85
          return Color(255 - pos * 3, 0, pos * 3)
      else:
          pos -= 170
          return Color(0, pos * 3, 255 - pos * 3)