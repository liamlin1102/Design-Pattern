from abc import ABC,abstractmethod
from Sprite import Sprite
from CollisionHandler import CollisionHandler
from __future__ import annotations

class WaterFireCollision(CollisionHandler):
    
    def matchType(self,startType:str,endType:str):
        return (startType=="W" and endType=="F") or (startType=="F" and endType=="W") 
    
    def collisionEffect(self,startSprite:Sprite,endSprite:Sprite):
        self.world.removeSprite(startSprite.positon)
        self.world.removeSprite(endSprite.positon)
        return False