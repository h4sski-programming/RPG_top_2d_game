from pygame import Rect

from settings import Player_settings as Pl_settings
from sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y, hp) -> None:
        super().__init__(x + Pl_settings.width/2, y + Pl_settings.height/2,
                         Pl_settings.width, Pl_settings.height)
        
        self.hp = hp
        self.velocity = Pl_settings.velocit
        self.color = Pl_settings.color
        self.bullets_number = Pl_settings.bullets_number
        self.fire_delay = Pl_settings.fire_delay
        self.last_fire_time = 0
        
        self.weapon_width = Pl_settings.weapon_width
        self.weapon_height = Pl_settings.weapon_heigh
        self.weapon_color = Pl_settings.weapon_color
    
    def get_rect(self):
        return Rect(self.x, self.y, self.width, self.height)
    
    def get_weapon_rect(self, p):
        return Rect(self.x + self.width / 2, self.y + self.height / 2,
                    self.weapon_width, self.weapon_height/2)