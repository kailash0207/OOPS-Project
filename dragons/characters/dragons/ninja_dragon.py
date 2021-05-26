from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    implemented = True  
    food_cost = 5
    blocks_path = False
    

    def action(self, colony):
       
        terminators = self.place.terminators.copy()
        for terminator in terminators:
            terminator.reduce_armor(self.damage)
