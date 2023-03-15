from pygame import Rect

from sprite import Sprite

class Character(Sprite):
    def __init__(self, x, y, settings_class) -> None:
        super().__init__(x + settings_class.width/2, y + settings_class.height/2,
                         settings_class.width, settings_class.height)
        
        if settings_class.hp:
            self.hp = settings_class.hp
        self.velocity = settings_class.velocity
        self.color = settings_class.color
        

    def get_rect(self):
        return Rect(self.x, self.y, self.width, self.height)
    
    
    def get_center_position(self):
        return (self.x + self.width / 2, self.y + self.height / 2)
    
    
    def hitted(self):
        if self.hp:
            self.hp -= 1