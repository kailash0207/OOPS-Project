from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    
    implemented = True  
    food_cost = 5
   

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
       
        
        terminators = self.place.terminators.copy()
        net_damage = amount
        super().reduce_armor(amount)
        if self.armor<=0:
            net_damage+=self.damage
        for terminator in terminators:
            terminator.reduce_armor(net_damage)
        
       
        
      
        