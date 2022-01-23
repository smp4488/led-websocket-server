# from effect import Effect
from led import set_color_hex, colorWipe
import effects.effect

class Solid(effects.effect.Effect):

  def __init__(self):
      options = { 'name': 'solid', 'description': 'A solid color', 'title': 'Solid' }
      super().__init__(options)

  def stop(self):
    self.running = False
    set_color_hex('#000000')

  def run(self, options):
    if options.color:
      set_color_hex(options.color)