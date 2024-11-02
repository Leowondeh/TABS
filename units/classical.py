from .base import *
import logging

# +---------------------+
# |  ancient era units  |
# |  TODO: add all      |
# |  units info         |
# +---------------------+

class Spearman(BaseUnit):
    def __init__(self, id):
        self.unit_name = "Spearman"
        self.id = id
        self.armor = 0
        self.current_health = 70
        self.max_health = 70
        self.attack_damage = 35