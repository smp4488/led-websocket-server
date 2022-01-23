import logging

class Effect:
  running = False
  def __init__(self, options):
      self.id = options.id
      self.name = options.name
      self.description = options.description
      self.logger = logging.getLogger()

  def start(self, options):
    self.running = True
    self.run(options)

  def stop(self):
    self.running = False

  def run(self, options):
    pass