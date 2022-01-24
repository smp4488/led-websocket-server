from led import set_color_hex, colorWipe
import asyncio
import effects.effect

class Solid(effects.effect.Effect):

  def __init__(self):
      options = { 'name': 'solid', 'description': 'A solid color', 'title': 'Solid' }
      super().__init__(options)

  def stop(self):
    self.running = False
    set_color_hex('#000000')

  # async def run(self, options):
  #   self.logger.info('running solid ' + options['color'])
  #   if options['color']:
  #     set_color_hex(options['color'])
  #   await asyncio.sleep(1)

  def run(self, options):
    self.logger.info('running solid ' + options['color'])
    if options['color']:
      set_color_hex(options['color'])