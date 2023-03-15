
class Settings():
    width = 1000
    height = 800
    game_title = 'RPG top 2D'
    fps = 60
    
class Player_settings():
    width = 30
    height = width
    velocit = 3
    hp = 10
    color = 'orange'
    bullets_number = 2      # including 0, e.g. if 3 then 4 bullets
    fire_delay = 200         # miliseconds
    weapon_width = 70
    weapon_heigh = 8
    weapon_color = 'white'
    
class Bullet_settings():
    width = 7
    height = width
    velocity = 6
    color = 'red'

class Enemy_settings():
    width = 20
    height = width
    velocit = 4
    hp = 3
    color = 'blue'