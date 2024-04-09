from abc import ABC,abstractmethod
from Sprite import Sprite
from CollisionHandler import CollisionHandler
from __future__ import annotations

class HeroFireCollision(CollisionHandler):

    def matchType(self,startType:str,endType:str):
        return (startType=="H" and endType=="F") or (startType=="F" and endType=="H") 
    
    def collisionEffect(self,startSprite:Sprite,endSprite:Sprite):
        self.hp-=10
        self.world.removeSprite(target)
        if self.hp==0 : remove=True
        return True