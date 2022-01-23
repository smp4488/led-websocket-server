import logging
import json

class Effect:
  running = False
  def __init__(self, options):
      self.name = options['name']
      self.description = options['description']
      self.title = options['title']
      self.logger = logging.getLogger()

  def start(self, options):
    self.running = True
    self.run(options)

  def stop(self):
    self.running = False

  def run(self, options):
    pass

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)