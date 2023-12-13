from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Player import Player


class ExchangePlayer:
    def __init__(self,round:int,player:Player) -> None:
        self.round = round
        self.player= player