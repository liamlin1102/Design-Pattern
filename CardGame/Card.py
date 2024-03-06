from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from Deck  import Deck

class Card(ABC):
    @abstractmethod 
    def __init__(self):
        return
    
    @abstractmethod 
    def MakeDeck(self)->Deck:
        return 


        
