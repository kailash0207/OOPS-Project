from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    

    name = 'Laser'
    implemented = True
    food_cost = 10
    damage = 2

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
       current_place = self.place
       front_fighters = {}
       current_distance = 0
       while current_place is not skynet:
           if current_place is self.place:
               if self.place.dragon != self:
                   front_fighters.update({self.place.dragon : current_distance})
           else:
               dragon = current_place.dragon
               if dragon is not None:
                    front_fighters.update({dragon : current_distance})
                    if dragon.is_container:
                        if dragon.contained_dragon is not None:
                            front_fighters.update({dragon.contained_dragon : current_distance})
           terminators = { terminator: current_distance for terminator in current_place.terminators}
           front_fighters.update(terminators)
           current_place = current_place.entrance
           current_distance+=1
       return front_fighters





    def calculate_damage(self, distance):
        
        return max(0,self.damage - 0.2 * distance - 0.05 * self.fighters_shot)
        

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
