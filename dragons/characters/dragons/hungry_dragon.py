from .dragon import Dragon
from utils import random_or_none

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    implemented = True
    food_cost = 4
    time_to_digest = 3
   

    def __init__(self, armor=1, digesting=0):
        
        Dragon.__init__(self,armor)
        self.digesting = digesting
       

    def eat_terminator(self, terminator):
       
         terminator.reduce_armor(terminator.armor)
         self.digesting = self.time_to_digest
       

    def action(self, colony):
        
        if self.digesting>0:
            self.digesting-=1
        else:
            terminator_to_eat = random_or_none(self.place.terminators)
            if terminator_to_eat is not None:
                self.eat_terminator(terminator_to_eat)
               

