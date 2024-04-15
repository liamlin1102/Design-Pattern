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
    def Main(self):
        world = World()
        world.makeSprite()
        while(True):
            positionList = self.movingTime()
            handler = SameSpritCollision(HeroFireCollision(HeroWaterCollision(WaterFireCollision(world),world),world),world)
            world.moveSprite(positionList[0],positionList[1],handler)

        
    def movingTime(self):
        positionList = []
        positionList = input("輸入兩個數字（以空白隔開）,數值範圍 0~29").split(" ")
        if len(positionList)<=1: 
            print("請輸入兩個數字，數值範圍 0~29並且使用空白符號隔開")
            positionList = self.movingTime()
        return positionList