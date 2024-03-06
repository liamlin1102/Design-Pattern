from __future__ import annotations
from Coord import Coord
from typing import Set,List
class Imdividual():
    def __init__(self,id:int,gender:str,age:int,intro:str,habbits:Set[str],coord:Coord)->None:
        self.id = id
        self.gender = gender
        self.age =age
        self.intro = intro
        self.habbits = habbits
        self.coord = coord 
        return 