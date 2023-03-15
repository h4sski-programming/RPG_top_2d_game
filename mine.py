import pygame
import time

from settings import Settings
from player import Player
from bullet import Bullet
from map import Map
from enemy import Enemy


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
        
        spawn_position = self.map.get_player_position() 
        self.player = Player(x=spawn_position[0], y=spawn_position[1])
        
        pygame.init()
        self.player_health_font = pygame.font.SysFont(name='Verdana', size=(self.player.height), bold=True)
        
        self.enemy_list = []
        while True:
            continue_loop, enemy_pos = self.map.get_enemy_position(30)
            if not continue_loop:
                break
            enemy = Enemy(x=enemy_pos[0], y=enemy_pos[1])
            self.enemy_list.append(enemy)
        
        self.main_loop()
        
    
    def draw(self):
        self.window.fill('black')
        
        # drawing the map
        self.map_surface.fill('black')
        self.map.draw_map(self.map_surface)
        self.window.blit(source=self.map_surface, dest=(0, 0))
        
        # draw player
        pygame.draw.rect(surface=self.window,
                         color=self.player.color,
                         rect=self.player.get_rect())
        
        # player health label
        player_health_label = self.player_health_font.render(f'Players health = {self.player.hp}', 1, self.player.color, 'black')
        self.window.blit(player_health_label, (30, 5))
        
        # draw enemys
        for enemy in self.enemy_list:
            pygame.draw.rect(surface=self.window,
                             color=enemy.color,
                             rect=enemy.get_rect())
        
            ### draw agro lines - for debuging
            # pygame.draw.line(self.window, 'white', enemy.get_center_position(), self.player.get_center_position())
        
        # draw player bullets
        for b in self.bullets_list:
            pygame.draw.rect(surface=self.window,
                             color=b.color,
                             rect=b.get_rect())
        
        pygame.display.update()
    
    
    def update(self):
        
        for b, bullet in enumerate(self.bullets_list):
            bullet.increment_position()
            
            # removing bullets from bullet_list if hit wall (or out of the window)
            if not self.window_rect.colliderect(bullet.get_rect()) \
                or \
                not self.map.collidete_with_object(object=bullet, move_direction=(bullet.delta_x, bullet.delta_y)):
                self.bullets_list.pop(b)
            
            # remove bullet if hit enemy
            for e, enemy in enumerate(self.enemy_list):
                if bullet.get_rect().colliderect(enemy.get_rect()):
                    self.bullets_list.pop(b)
                    enemy.hitted()
                    enemy.agro_on_player = True
                    if enemy.hp == 0:
                        self.enemy_list.pop(e)
                        if len(self.enemy_list) == 0:
                            self.quit_main()
        
        # checking agro on all enemys
        # for en, enemy in enumerate(self.enemy_list):
        
        # move enemys
        for enemy in self.enemy_list:
            ### check agro based on distance and start moving
            enemy.check_agro_distance(self.player.get_center_position())
            enemy.move_to_player(self.player.get_center_position())
            
            ### check colision with player
            if enemy.get_rect().colliderect(self.player.get_rect()):
                self.quit_main()
            
    
    
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
        if keys[pygame.K_a] and self.player.x >= 0 and \
            self.map.collidete_with_object(object=self.player, move_direction=(-self.player.velocity, 0)):
            self.player.x -= self.player.velocity
        if keys[pygame.K_d] and self.player.x + self.player.width <= Settings.width and \
            self.map.collidete_with_object(object=self.player, move_direction=(self.player.velocity, 0)):
            self.player.x += self.player.velocity
        # vertical
        if keys[pygame.K_w] and self.player.y >= 0 and \
            self.map.collidete_with_object(object=self.player, move_direction=(0, -self.player.velocity)):
            self.player.y -= self.player.velocity
        if keys[pygame.K_s] and self.player.y + self.player.height <= Settings.height and \
            self.map.collidete_with_object(object=self.player, move_direction=(0, self.player.velocity)):
            self.player.y += self.player.velocity
        
        m_btn = pygame.mouse.get_pressed(num_buttons=3)
        if m_btn[0] and pygame.time.get_ticks() >= self.player.last_fire_time + self.player.fire_delay:
            self.create_bullet()
    
    def quit_main(self):
        self.running = False
    
    def main_loop(self):
        self.bullets_list = []
        
        while self.running:
            self.clock.tick(Settings.fps)
            self.mouse = pygame.mouse.get_pos()
            self.events()
            self.update()
            self.draw()
        
        quit_font = pygame.font.SysFont(name='verdana', size=100, bold=True)
        quit_string = 'GAME OVER'
        quit_label = quit_font.render(quit_string, 1, self.player.color, 'black')
        quit_label_size = quit_font.size(quit_string)
        self.window.blit(source=quit_label, 
                         dest=((Settings.width - quit_label_size[0]) / 2,
                               (Settings.height - quit_label_size[1]) / 2))
        pygame.display.update()
        
        pygame.time.delay(2000)
        pygame.quit()
    
    
    
if __name__ == '__main__':
    Main()