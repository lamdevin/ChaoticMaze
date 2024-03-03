from board import Board
import pygame
import random

class Player(pygame.sprite.Sprite):
    x = 1
    y = 1
    speed = 1
    player_size = 50
    player_color = (0, 255, 0)
    def move_right(self):
        temp = self.x + self.speed
        if temp >= Board.size - 1:
            self.x = Board.size - 2
        else:
            self.x = temp
        
    def move_left(self):
        temp = self.x - self.speed
        if temp <= 1:
            self.x = 1
        else:
            self.x = temp
            
    def move_down(self):
        temp = self.y + self.speed
        if temp >= Board.size - 1:
            self.y = Board.size - 2
        else:
            self.y = temp  
    
    def move_up(self):
        temp = self.y - self.speed
        if temp <= 1:
            self.y = 1
        else:
            self.y = temp
            
    def random_change_speed(self):
        number = random.randint(-2, 2)
        self.speed = number
        if self.speed == 0:
            self.speed = 1
        