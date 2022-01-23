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

  def start(self, options):
    self.running = True
    self.run(options)

  def stop(self):
    self.running = False

  def run(self, options):
    pass

  def toJSON(self):
    return json.dumps(self.__dict__)