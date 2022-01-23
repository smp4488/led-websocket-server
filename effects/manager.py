import logging

import effects.solid

class EffectsManager:
  effects = list()

  def __init__(self):
    self.logger = logging.getLogger()
    

    # adding each effect
    self.effects.append(effects.solid.Solid())

    # set solid as currnet
    self.current_effect = self.effects[0] 

  def get_effects(self):
    return self.effects
    # return [effect.toJSON() for effect in self.effects]

  def get_effect_by_name(self, name):
    return filter(lambda effect: effect.name == name, self.effects)

  def set_effect(self, name, options):
    self.current_effect.stop()
    effect = self.get_effect_by_name(name)
    effect.start(options)