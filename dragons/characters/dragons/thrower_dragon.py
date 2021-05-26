from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost = 3
    min_range = 0
    max_range = float('inf')
    

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        
        search_place = self.place
        place_position = 0
        while(search_place != skynet):
            if place_position<self.min_range:
                search_place = search_place.entrance;
                place_position+=1
            elif place_position>=self.min_range and place_position<=self.max_range:
                if search_place.terminators==[]:
                    search_place = search_place.entrance
                    place_position+=1
                else:
                    return random_or_none(search_place.terminators)
            else:
                break
        

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))


