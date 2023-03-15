from pygame import Rect

from settings import Player_settings as Pl_settings
from character import Character

class Player(Character):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, settings_class=Pl_settings)
        
        self.bullets_number = Pl_settings.bullets_number
        self.fire_delay = Pl_settings.fire_delay
        self.last_fire_time = 0
        
        self.weapon_width = Pl_settings.weapon_width
        self.weapon_height = Pl_settings.weapon_heigh
        self.weapon_color = Pl_settings.weapon_color
    
    
    def get_weapon_rect(self, p):
        return Rect(self.x + self.width / 2, self.y + self.height / 2,
                    self.weapon_width, self.weapon_height/2)