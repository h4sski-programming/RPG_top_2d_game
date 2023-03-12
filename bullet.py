import pygame

from settings import Bullet_settings
from sprite import Sprite


class Bullet(Sprite):
    def __init__(self, x, y, mouse_position) -> None:
        super().__init__(x - Bullet_settings.width / 2, y - Bullet_settings.height / 2,
                         Bullet_settings.width, Bullet_settings.height)
        
        self.velocity = Bullet_settings.velocity
        self.color = Bullet_settings.color
        
        self.delta_x = self.velocity
        self.delta_y = 0
        
        self.calculate_delta(mouse_position=mouse_position)
    
    def calculate_delta(self, mouse_position):
        pass
    
    def increment_position(self):
        self.x += self.delta_x
        self.y += self.delta_y
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)