from math import sin, cos, sqrt
from pygame import draw, time
import random

from settings import Enemy_settings
from character import Character

class Enemy(Character):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, settings_class=Enemy_settings)
        
        self.agro_on_player = False
        # self.velocity_standby = Enemy_settings.velocit_standby
        # self.move_tick = 0
        # self.movement_delay = Enemy_settings.movement_delay
        
        # self.move_direction = 0
        # self.turning_raio = Enemy_settings.turning_ratio
    
    
    def check_agro_distance(self, player_position):
        enemy_position = self.get_center_position()
        dx = player_position[0] - enemy_position[0]
        dy = player_position[1] - enemy_position[1]
        real_distance = sqrt(dx*dx + dy*dy)
        if real_distance <= Enemy_settings.agro_distance:
            self.agro_on_player = True
    
    
    def move_to_player(self, player_position):
        if self.agro_on_player:
            enemy_position = self.get_center_position()
            dx = player_position[0] - enemy_position[0]
            dy = player_position[1] - enemy_position[1]
            real_distance = sqrt(dx*dx + dy*dy)
            ratio = real_distance / self.velocity
            self.x += dx / ratio
            self.y += dy / ratio
    
    
    
    ### to be removed
    
    def get_agro_line(self, player):
        enemy_position = self.get_center_position()
        player_position = player.get_center_position()
        draw.line()
        
    
    def generate_move_direction(self):
        x = random.random() * random.choice([-1, 1])
        y = (1 - x) * random.choice([-1, 1])
        return (x, y)
    
    def move(self):
        cur_time = time.get_ticks()
        # if True:
        if cur_time > self.move_tick + self.movement_delay:
            self.move_tick = cur_time
            
            self.move_direction += (random.random() * 2 - 1) * self.turning_raio
            print(self.move_direction)
            self.x += sin(self.move_direction) * self.velocity
            self.y += cos(self.move_direction) * self.velocity
            
            # old thinking
            # move_directions = self.generate_move_direction()
            # self.x += self.velocity * move_directions[0]
            # self.y += self.velocity * move_directions[1]