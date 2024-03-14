from abc import ABC,abstractmethod
from __future__ import annotations

class Sprite(ABC):
    def __init__(self,type:str):
        self.type = type
        return 
    @abstractmethod
    def collision(self,target:Sprite):
        return 