import pygame
import random

class Board:
    goal = [0, 0]
    size = 16 # num of tiles
    tile_size = 50
    surface = pygame.display.set_mode((size * tile_size, size * tile_size))
    def __init__(self):
        self.wall_color = (80, 80, 80)
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

        self.setBoard(1, 1)

    def setBoard(self, player_x, player_y):
        goal_x = random.randint(1, self.size-2)
        goal_y = random.randint(1, self.size-2)

        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                if (i == player_y and j == player_x):
                    self.board[i][j] = 0
                    continue
                num = random.randint(0,10)
                if (num < 7):
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = 1
        
        self.board[goal_y][goal_x] = 2
        self.goal[0] = goal_y
        self.goal[1] = goal_x
    
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

    