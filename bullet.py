from pygame import Rect
from math import asin, sin, cos, radians, sqrt
import math

from settings import Bullet_settings
from sprite import Sprite


class Bullet(Sprite):
    def __init__(self, x, y, mouse_position=(0, 0)) -> None:
        super().__init__(x - Bullet_settings.width / 2, y - Bullet_settings.height / 2,
                         Bullet_settings.width, Bullet_settings.height)
        
        self.velocity = Bullet_settings.velocity
        self.color = Bullet_settings.color
        
        self.delta_x = self.velocity
        self.delta_y = 0
        
        # self.calculate_delta(mouse_position=mouse_position)
    
    def calculate_delta(self, mouse_position):
        d_x = mouse_position[0] - self.x
        d_y = mouse_position[1] - self.y
        
        # c^2 = a^2 + b^2  => c = sqrt(a^2 + b^2)
        c = sqrt(d_x * d_x + d_y * d_y)
        ratio = c / self.velocity
        
        self.delta_x = d_x / ratio
        self.delta_y = d_y / ratio
        # print(f'delta_x: {self.delta_x}, delta_y: {self.delta_y}')
    
    
    def increment_position(self):
        self.x += self.delta_x
        self.y += self.delta_y
    
        
    def get_rect(self):
        return Rect(self.x, self.y, self.width, self.height)