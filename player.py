from board import Board
import pygame
import random

class Player(pygame.sprite.Sprite):
    x = 1
    y = 1
    speed = 1
    def move_right(self):
        if self.x == Board.size:
            self.x += self.speed
        
    def move_left(self):
        if self.x > 1:
            self.x -= self.speed
            
    def move_down(self):
        if self.y == Board.size:
            self.y += self.speed       
    
    def move_up(self):
        if self.y > 1:
            self.y -= self.speed
            
    def change_speed(self):
        number = random.randint(-3, 3)
        self.speed += number
        if self.speed == 0:
            self.speed = 1
        