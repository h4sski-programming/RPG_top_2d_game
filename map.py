from pygame import Rect, draw

from settings import Settings

class Map():
    def __init__(self) -> None:
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],     #1
                    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],     #2
                    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],     #3
                    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],     #4
                    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],     #5
                    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],     #6
                    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],     #7
                    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],     #9
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],     #8
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],     #10
                    ]
        self.rows = len(self.map)
        self.columns = len(self.map[0])
        
        self.cell_color = 'green'
        
        self.row_height = Settings.height / self.rows
        self.column_width = Settings.width / self.columns
    
    
    def draw_map(self, surface):
        for i, row in enumerate(self.map):
            for j, column in enumerate(row):
                if column == 0:
                    continue
                cell = Rect(i * self.column_width, j * self.row_height,
                            self.row_height, self.column_width)
                draw.rect(surface=surface, color=self.cell_color, rect=cell)