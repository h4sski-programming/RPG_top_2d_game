import pygame
import time

from settings import Settings


class Main():
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((Settings.width, Settings.height))
        pygame.display.set_caption(Settings.game_title)
        self.running = True
        
        self.main_loop()
        
    
    def draw(self):
        pass
    
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
    
    
    
    def main_loop(self):
        while self.running:
            self.events()
            self.draw()
        
        pygame.quit()
    
    
    
if __name__ == '__main__':
    Main()