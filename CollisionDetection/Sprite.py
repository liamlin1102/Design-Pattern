from abc import ABC,abstractmethod
from World import World
from __future__ import annotations

class Sprite(ABC):
    def __init__(self,type:str,position:int,world:World):
        self.type = type
        self.positon = position
        self.world = world
        return
        