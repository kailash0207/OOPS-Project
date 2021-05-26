from .thrower_dragon import ThrowerDragon
from utils import make_scare, apply_effect

class ScaryThrower(ThrowerDragon):
    """ThrowerDragon that intimidates Terminators, making them back away instead of advancing."""

    name = 'Scary'
    food_cost = 6
    implemented = True

    

    def throw_at(self, target):
       if target:
            apply_effect(make_scare, target, 2)
            

       
