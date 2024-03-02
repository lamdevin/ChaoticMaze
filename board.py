import pygame
import random

class Board:
    size = 16
    surface = pygame.display.set_mode((size * 50, size * 50))
    def __init__(self):
        self.wall_color = (255, 0, 0)
        self.goal_color = (255, 255, 0)
        self.empty_color = (255, 255, 255)
        
        self.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        self.setBoard()

    def setBoard(self):
        goal_x = random.randint(1, self.size-2)
        goal_y = random.randint(1, self.size-2)

        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                num = random.randint(0,10)
                if (num < 7):
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = 1
        
        self.board[goal_y][goal_x] = 2
    
    def draw(self):
        pos_x = 0
        pos_y = 0
        rect_size = 50
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    pygame.draw.rect(self.surface, self.wall_color, pygame.Rect(pos_x, pos_y, rect_size, rect_size))
                elif self.board[i][j] == 2:
                    pygame.draw.rect(self.surface, self.goal_color, pygame.Rect(pos_x, pos_y, rect_size, rect_size))
                else:
                    pygame.draw.rect(self.surface, self.empty_color, pygame.Rect(pos_x, pos_y, rect_size, rect_size))
                pos_x += rect_size
            pos_x = 0
            pos_y += rect_size

    