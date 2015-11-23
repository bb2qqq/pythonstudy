""" This file is using to generate all kinds of cards for play   """
from attrs import ATTR_DICT
ABILITY_COST_DICT = {
'Fast_attack': 'attack_related',
'Multiple_attack': 'attack_related',
'Damage_absorb': 'attack_related',
'Force_attack': 1,
}


def cost_caulculator(atttak, defend, abilities=[]):
    abilities = set(abilities)




class Card(object):
    def __init__(self, attr_list):
        over_all_cost = 0
        for attr in attr_list:
            cost = ATTR_DICT[attr]['cost']
            effects = ATTR_DICT[attr]['effect']
