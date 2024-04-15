from Sprite import Sprite
from World import World
class Fire(Sprite):
    
    def __init__(self, type: str, position: int, world: World):
        super().__init__(type, position, world)
        return 