from Sprite import Sprite
class Hero(Sprite):

    def __init__(self, type: str):
        super().__init__(type)
        self.hp = 30
    
    def collision(self,target: Sprite):
        if(target.type=="W"):
            self.hp+=10
        if(target==None):
            return True
