from Sprite import Sprite
class Water(Sprite):

    def collision(self,target: Sprite,remove:bool):
        if target.type=="W":
            return False
        elif target.type=="H" :
            remove = True
            target.hp +=10
            return False
        elif target.type=="F":
            self.world.removeSprite(target)
            return False
        return True
        