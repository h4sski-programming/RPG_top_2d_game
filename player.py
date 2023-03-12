import pygame

from settings import Settings
from sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y, hp) -> None:
        super().__init__(x, y, Settings.Player.width, Settings.Player.height)
        
        self.hp = hp
        self.velocity = Settings.Player.velocit
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)