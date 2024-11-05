import logging
from random import randint

class BaseUnit():
    '''
    Base model for units, does not have stats.

    DO NOT modify it's stats or add new abilities, instead create a new unit inheriting from BaseUnit.
    '''
    def __init__(self, id):
        self.unit_name = "Base unit"
        self.id = id
        self.armor = 0
        self.current_health = 1
        self.max_health = 1
        self.attack_damage = 0

    def take_turn(self, enemies):
        '''
        Default AI

        Tries to use Defend (although randomly and rarely) if HP is lower than 50%, otherwise attacks lowest HP unit
        '''
        if self.current_health < self.max_health/2 and self.armor < 10 and randint(1, 10) <= 2:
            self.ability_defend()
            return
        
        # Target is the enemy with lowest HP. If there are 2+ units with the same HP, the lowest ID gets selected
        target = [enemy for enemy in enemies if enemy.current_health == min(enemy.current_health for enemy in enemies)][0]
        target.get_attacked(self.attack_damage)
        
        logging.debug(f"{self.unit_name} attacked unit ID {target.id} ({target.unit_name}), dealing {self.attack_damage} damage. (HP now {target.current_health})")

    def get_attacked(self, damage):
        '''
        Default course of action when getting attacked

        Tries to break armor, otherwise attacks
        '''
        if self.armor > 0:
            if self.armor - damage <= 0:
                self.armor = 0
                return
            self.armor -= damage
            return
        
        self.current_health -= damage

    def ability_defend(self):
        '''
        Default Defend

        Adds 30 armor to self, which tanks in place of HP on attack.
        '''
        self.armor += 30
        logging.debug(f'{self.unit_name} used Defend! (armor now {self.armor})')