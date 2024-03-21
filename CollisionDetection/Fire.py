from Sprite import Sprite
class Fire(Sprite):
    
    def collision(self,target: Sprite,remove:bool):
        if target.type=="W":
            remove = True
            self.world.removeSprite(target)
        elif target.type=="H" :
            target.hp -=10
            if target.hp==0:self.world.removeSprite(target)
            remove=True
            return False
        elif target.type=="F":
            return False
        return True
    