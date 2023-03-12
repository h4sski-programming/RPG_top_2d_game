import pygame
import time

from settings import Settings
from player import Player
from bullet import Bullet
from map import Map


class Main():
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((Settings.width, Settings.height))
        pygame.display.set_caption(Settings.game_title)
        self.running = True
        self.clock = pygame.time.Clock()
        self.window_rect = pygame.Rect(0, 0, Settings.width, Settings.height)
        
        self.map = Map()
        self.map_surface = pygame.Surface((Settings.width, Settings.height))
        self.map.draw_map(self.map_surface)
        
        self.player = Player(x=200, y=300, hp = 10)
        
        
        self.main_loop()
        
    
    def draw(self):
        self.window.fill('black')
        self.map_surface.fill('black')
        self.window.blit(source=self.map_surface, dest=(0, 0))
        
        # draw player
        pygame.draw.rect(surface=self.window,
                         color=self.player.color,
                         rect=self.player.get_rect())
        
        # draw bullets
        for b in self.bullets_list:
            pygame.draw.rect(surface=self.window,
                             color=b.color,
                             rect=b.get_rect())
        
        pygame.display.update()
    
    
    def update(self):
        for i, bullet in enumerate(self.bullets_list):
            bullet.increment_position()
            if not self.window_rect.colliderect(bullet.get_rect()):
                self.bullets_list.pop(i)
    
    
    def create_bullet(self):
        if len(self.bullets_list) <= self.player.bullets_number:
            b = Bullet(x = self.player.x + self.player.width / 2,
                       y = self.player.y + self.player.height / 2)
            b.calculate_delta(self.mouse)
            self.bullets_list.append(b)
            self.player.last_fire_time = pygame.time.get_ticks()
        
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
        
        
        keys = pygame.key.get_pressed()
        
        # player movement
        # horizontal
        if keys[pygame.K_a] and self.player.x >= 0:
            self.player.x -= self.player.velocity
        if keys[pygame.K_d] and self.player.x + self.player.width <= Settings.width:
            self.player.x += self.player.velocity
        # vertical
        if keys[pygame.K_w] and self.player.y >= 0:
            self.player.y -= self.player.velocity
        if keys[pygame.K_s] and self.player.y + self.player.height <= Settings.height:
            self.player.y += self.player.velocity
        
        m_btn = pygame.mouse.get_pressed(num_buttons=3)
        if m_btn[0] and pygame.time.get_ticks() >= self.player.last_fire_time + self.player.fire_delay:
            self.create_bullet()
    
    
    
    def main_loop(self):
        
        self.bullets_list = []
        
        while self.running:
            self.clock.tick(Settings.fps)
            self.mouse = pygame.mouse.get_pos()
            self.events()
            self.update()
            self.draw()
            
        pygame.quit()
    
    
    
if __name__ == '__main__':
    Main()