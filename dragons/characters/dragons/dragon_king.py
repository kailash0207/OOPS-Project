from characters.dragons.scuba_thrower import ScubaThrower
from utils import terminators_win
class DragonKing(ScubaThrower):  
   
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    food_cost = 7
    implemented = True  
    instantiated = False
    buffed_dragons =[]
    

    def __init__(self, armor=1):
        ScubaThrower.__init__(self,armor)
        if not self.instantiated:
            DragonKing.instantiated = True
            self.is_true_king = True
        else:
            self.is_true_king = False
        

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        
        if not self.is_true_king:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            check_place = self.place.exit
            while check_place is not None:
                dragon = check_place.dragon
                if dragon is not None and dragon not in self.buffed_dragons:
                    check_place.dragon.damage *=2
                    self.buffed_dragons.append(check_place.dragon)
                if dragon is not None and dragon.is_container:
                    contained_dragon = dragon.contained_dragon
                    if contained_dragon is not None and contained_dragon not in self.buffed_dragons:
                        check_place.dragon.contained_dragon.damage *=2
                        self.buffed_dragons.append(check_place.dragon.contained_dragon)
                check_place = check_place.exit

        

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        super().reduce_armor(amount)
        if self.armor <=0 and self.is_true_king:
            terminators_win()

