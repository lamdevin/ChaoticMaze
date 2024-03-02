import pygame
import random

class Board:
    size = 8
    surface = pygame.display.set_mode((size * 100, size * 100))
    def __init__(self):
        self.size = 8
        self.surface = pygame.display.set_mode((self.size * 100, self.size * 100))
        self.wall_color = (255, 0, 0)
        self.goal_color = (255, 255, 0)
        self.empty_color = (255, 255, 255)
        
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

        self.setBoard()

    def setBoard(self):
        goal_x = random.randint(1, self.size-1)
        goal_y = random.randint(1, self.size-1)

        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                if (i == goal_x and j == goal_y):
                    self.board[i][j] = 2
                else:
                    num = random.randint(0,1)
                    self.board[i][j] = num
    
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
                else:
                    pygame.draw.rect(self.surface, self.empty_color, pygame.Rect(pos_x, pos_y, rect_size, rect_size))
                pos_x += rect_size
            pos_x = 0
            pos_y += rect_size

    