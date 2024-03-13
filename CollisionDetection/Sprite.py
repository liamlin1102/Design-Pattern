from abc import ABC,abstractmethod
from __future__ import annotations

class Sprite(ABC):
    def __init__(self,position:int):
        self.position= position
    @abstractmethod
    def collision(self,target:Sprite):
        return 