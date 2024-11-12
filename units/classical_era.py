from .base import *
import logging

# +---------------------+
# |  classic era units  |
# +---------------------+

class spearman(base_unit):
    def __init__(self, id):
        self.unit_name = 'Spearman'
        self.id = id
        self.current_health = 70
        self.max_health = 70
        self.armor = 0
        self.attack_damage = 35