from CollisionDetection.World import World
from Sprite import Sprite
class Hero(Sprite):

    def __init__(self, type: str, position: int, world: World):
        super().__init__(type, position, world)
        self.hp = 30
        return 
    

    

        
        

