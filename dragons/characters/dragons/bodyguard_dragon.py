from .dragon import Dragon


class BodyguardDragon(Dragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    food_cost = 4
    implemented = True  
    is_container = True
    def __init__(self, armor=2):
        Dragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard

    def can_contain(self, other):
        return self.contained_dragon is None and other.is_container == False
        

    def contain_dragon(self, dragon):
        self.contained_dragon = dragon
        

    def action(self, colony):
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
        
