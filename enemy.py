from pygame import Rect

from settings import Enemy_settings
from character import Character

class Enemy(Character):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, settings_class=Enemy_settings)
        
        self.agro_on_player = False
    