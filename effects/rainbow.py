
from led import LED_COLUMNS, LED_ROWS, strip_visualizer, strip_accent, led_martix
import asyncio
import effects.effect

class Rainbow(effects.effect.Effect):

  def __init__(self):
      options = { 'name': 'rainbow', 'description': 'Draw rainbow that fades across all pixels at once.', 'title': 'Rainbow' }
      super().__init__(options)

  def stop(self):
    self.running = False

  async def run(self, options):
    self.logger.info('running rainbow')

    while self.running:
      """Draw rainbow that fades across all pixels at once."""
      for j in range(256):

        for c in range(LED_COLUMNS):
            # need to offset i to correct number for strip
            for r in range(LED_ROWS):
              if (r == 2):
                strip = strip_visualizer
              else:
                strip = strip_accent
              
              strip.setPixelColor(led_martix[r][c], self.wheel((c+j) & 255))

        strip_accent.show()
        strip_visualizer.show()
        await asyncio.sleep