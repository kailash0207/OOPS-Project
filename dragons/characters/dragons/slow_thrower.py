from .thrower_dragon import ThrowerDragon
from utils import apply_effect, make_slow


class SlowThrower(ThrowerDragon):
    """ThrowerDragon that causes Slow on Terminators."""

    name = 'Slow'
    food_cost = 4
    implemented = True

   

    def throw_at(self, target):
        if target:
            apply_effect(make_slow, target, 3)
