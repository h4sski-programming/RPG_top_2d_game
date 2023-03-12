import pygame
import time

from settings import Settings
from player import Player


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
        
        pygame.draw.rect(surface=self.window,
                         color=Settings.Player.color,
                         rect=self.player.get_rect())
        
        pygame.display.update()
    
    
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
    
    
    
    def main_loop(self):
        while self.running:
            self.clock.tick(Settings.fps)
            self.events()
            self.draw()
        
        pygame.quit()
    
    
    
if __name__ == '__main__':
    Main()