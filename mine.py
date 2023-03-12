import pygame
import time

from settings import Settings
from player import Player
from bullet import Bullet


class Main():
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((Settings.width, Settings.height))
        pygame.display.set_caption(Settings.game_title)
        self.running = True
        self.clock = pygame.time.Clock()
        
        self.player = Player(x=200, y=300, hp = 10)
        
        
        self.main_loop()
        
    
    def draw(self):
        self.window.fill('black')
        
        # draw player
        pygame.draw.rect(surface=self.window,
                         color=self.player.color,
                         rect=self.player.get_rect())
        
        # draw bullets
        for b in self.bullets_list:
            pygame.draw.rect(surface=self.window,
                             color=b.color,
                             rect=b.get_rect())
        
        # # draw player weapon
        # r = pygame.Surface(size=(100, 10))
        # r.fill('green')
        # # self.player.get_weapon_rect(self.mouse))
        # r_rotated = pygame.transform.rotate(r, self.angle)
        # pygame.draw.rect(surface=self.window,
        #                  color=self.player.weapon_color,
        #                  rect=r_rotated.get_rect())
        #                 #  rect=self.player.get_weapon_rect(self.mouse))
        
        pygame.display.update()
    
    
    def update(self):
        for i, bullet in enumerate(self.bullets_list):
            bullet.increment_position()
            if bullet.x >= Settings.width:
                self.bullets_list.pop(i)
    
    
    def create_bullet(self):
        if len(self.bullets_list) <= self.player.bullets_number:
            b = Bullet(x = self.player.x + self.player.width / 2,
                       y = self.player.y + self.player.height / 2,
                       self.mouse)
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
        
        self.angle = 0
        self.bullets_list = []
        
        while self.running:
            self.clock.tick(Settings.fps)
            
            self.mouse = pygame.mouse.get_pos()
            
            self.events()
            self.update()
            self.draw()
            self.angle += 1
            
        pygame.quit()
    
    
    
if __name__ == '__main__':
    Main()