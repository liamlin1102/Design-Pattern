from abc import ABC,abstractmethod
from Sprite import Sprite
from CollisionHandler import CollisionHandler
from __future__ import annotations

class HeroFireCollision(CollisionHandler):
    def matchType(self,startType:str,endType:str):
        return
    
    def collisionEffect(self,startSprite:Sprite,endSprite:Sprite):
        return 