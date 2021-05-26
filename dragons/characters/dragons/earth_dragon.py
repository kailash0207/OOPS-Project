from .dragon import Dragon

class EarthDragon(Dragon):
    name = 'Earth'
    implemented = True
    food_cost = 4

    def __init__(self,armor = 4):
        Dragon.__init__(self,armor)
    
    pass
