from abc import ABC,abstractmethod
from Sprite import Sprite
from CollisionHandler import CollisionHandler
from __future__ import annotations

class HeroWaterCollision(CollisionHandler):
    def matchType(self,startType:str,endType:str):
        return (startType=="H" and endType=="W") or (startType=="W" and endType=="H") 
    
    def collisionEffect(self,startSprite:Sprite,endSprite:Sprite):
        return True