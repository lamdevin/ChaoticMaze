import pygame

class Board:
    size = 8
    surface = pygame.display.set_mode((size * 100, size * 100))
    def __init__(self):
        self.size = 8
        self.surface = pygame.display.set_mode((self.size * 100, self.size * 100))
        self.wall_color = (255, 0, 0)
        self.goal_color = (255, 255, 0)
        
        self.board = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 2, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
    
    def draw(self):
        pos_x = 0
        pos_y = 0
        rect_size = 100
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    pygame.draw.rect(self.surface, self.wall_color, pygame.Rect(pos_x, pos_y, rect_size, rect_size))
                elif self.board[i][j] == 2:
                    pygame.draw.rect(self.surface, self.goal_color, pygame.Rect(pos_x, pos_y, rect_size, rect_size))
                pos_x += rect_size
            pos_x = 0
            pos_y += rect_size

    