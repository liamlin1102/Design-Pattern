from CollisionDetection.World import World
from Sprite import Sprite
class Hero(Sprite):

    def __init__(self, type: str, position: int, world: World):
        super().__init__(type, position, world)
        self.hp = 30
        return 
    
    def collision(self,target: Sprite,remove:bool):
        if target.type=="W":
            self.hp+=10
            self.world.removeSprite(target)
        elif target.type=="H" :
            return False
        elif target.type=="F":
            self.hp-=10
            self.world.removeSprite(target)
            if self.hp==0 : remove=True
        return True
    

        
        

