from abc import ABC,abstractmethod
from Sprite import Sprite
from CollisionHandler import CollisionHandler
from __future__ import annotations
from World import World
from SameSpritCollision import SameSpritCollision
from HeroFireCollision import HeroFireCollision
from HeroWaterCollision import HeroWaterCollision
from WaterFireCollision import WaterFireCollision

class Main:
    world = World()
    world.makeSprite()
    
    SameSpritCollision(HeroFireCollision(HeroWaterCollision(WaterFireCollision(world),world),world),world).collisionEffect()
    