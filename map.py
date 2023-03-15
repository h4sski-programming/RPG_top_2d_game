from pygame import Rect, draw

from settings import Settings


class Map():
    def __init__(self) -> None:
        # values:
        # -1 player spawn position
        # 0 empty (free) space
        # 1 wall
        self.map01 = [[1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],     #1
                      [1,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  1],     #2
                      [1,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  1],     #3
                      [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  0,  0,  1],     #4
                      [1,  0, -1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1],     #5
                      [1,  0,  0,  1,  0,  0,  1,  1,  1,  0,  0,  0,  1],     #6
                      [1,  1,  1,  1,  0,  0,  1,  0,  0,  0,  0,  0,  1],     #7
                      [1,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  1],     #8
                      [1,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1],     #9
                      [1,  0,  0,  0,  0,  0,  0,  1,  0,  1,  1,  1,  1],     #10
                      [1,  0,  0,  0,  1,  0,  0,  1, 30,  0,  0,  0,  1],     #11
                      [1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1],     #12
                      [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],     #last
                      ]
        self.map02 = [[1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],     #1
                      [1,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  1],     #2
                      [1,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  1],     #3
                      [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  1],     #4
                      [1,  0, -1,  1,  0,  0,  1,  0,  0,  0,  0,  0,  1],     #5
                      [1,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  1],     #6
                      [1,  1,  1,  0,  1,  0,  1,  0,  0,  1,  0,  1,  1],     #7
                      [1,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  1],     #8
                      [1,  0,  0,  0,  0,  0,  1,  0,  1,  0,  0,  0,  1],     #9
                      [1,  0,  0,  1,  1,  0,  1,  0,  1,  0,  1,  1,  1],     #10
                      [1,  0,  0,  0,  1,  0,  0,  0,  1,  0, 30,  0,  1],     #11
                      [1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1],     #12
                      [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],     #last
                      ]
        
        self.map = self.map01
        self.rows = len(self.map)
        self.columns = len(self.map[0])
        
        self.cell_color = 'green'
        self.row_height = Settings.height / self.rows
        self.column_width = Settings.width / self.columns
        
        self.walls = []
        self.generate_walls()
        
    
    
    def draw_map(self, surface):
        for wall in self.walls:
            draw.rect(surface=surface, color=self.cell_color, rect=wall)
    
    
    def generate_walls(self):
        for i, row in enumerate(self.map):
            for j, column in enumerate(row):
                # no value means not drawing
                if 0 >= column or column >= 30:
                    continue
                rectangle = self.generate_rectangle(j * self.column_width, i * self.row_height)
                self.walls.append(rectangle)
    
    
    def generate_rectangle(self, x_pos, y_pos):
        return Rect(x_pos, y_pos, self.column_width, self.row_height)
    
    
    def collidete_with_object(self, object, move_direction):
        object_rect = object.get_rect()
        object_rect_moved = object_rect.move(move_direction[0], move_direction[1])
        
        for wall in self.walls:
            if object_rect_moved.colliderect(wall):
                return False
        return True
    
    def get_player_position(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.map[row][column] == -1:
                    return (column * self.column_width, row * self.row_height)
    
    
    
    def get_enemy_position(self, enemy_id):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.map[row][column] == enemy_id:
                    self.map[row][column] = 0
                    return (column * self.column_width, row * self.row_height)
    