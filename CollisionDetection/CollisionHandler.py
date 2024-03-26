from abc import ABC,abstractmethod
from Sprite import Sprite
from __future__ import annotations
class CollisionHandler(ABC):
    
    def __init__(self,next:CollisionHandler):
        self.next = next
    
    def collision(self,startSprite:Sprite,endSprite:Sprite):
        if self.matchType(startSprite.type,endSprite.type):
            self.collisionEffect(startSprite,endSprite)
        else:
            self.next.collision(startSprite,endSprite)

    @abstractmethod   
    def matchType(self,startType:str,endType:str):
        return
    
    @abstractmethod
    def collisionEffect(self,startSprite:Sprite,endSprite:Sprite):
        return 