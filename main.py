import pygame
import sys
import random
from player import Player
from board import Board
from pygame.locals import *


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ChaoticMaze")

FPS = pygame.time.Clock()
FPS.tick(60)

player1 = Player()
board1 = Board()
steps = 0

def check_win():
    if board1.goal[0] == player1.y and board1.goal[1] == player1.x:
        temp = random.randint(1, 10)
        if temp <= 7:
            print("You win")
        else:
            check = True
            while check:
                goal_x = random.randint(1, board1.size-1)
                goal_y = random.randint(1, board1.size-1)
                if board1.board[goal_y][goal_x] == 0:
                    check = False
            board1.setBoard(player1.x, player1.y)
            print("bruh, try again")
            
            
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if board1.board[player1.y-1][player1.x] != 1:
                    player1.move_up()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if board1.board[player1.y+1][player1.x] != 1:
                    player1.move_down()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if board1.board[player1.y][player1.x-1] != 1:
                    player1.move_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if board1.board[player1.y][player1.x+1] != 1:
                    player1.move_right()
            steps = random.randint(1, 10)
            check_win()
            if steps % 7 == 2:
                board1.setBoard(player1.x, player1.y)
        
    board1.draw()
    player1.draw()
    pygame.display.update()
