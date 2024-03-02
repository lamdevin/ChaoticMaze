import pygame
import sys
from player import Player
from board import Board
from pygame.locals import *


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ChaoticMaze")

FPS = pygame.time.Clock()
FPS.tick(60)

player1 = Player()
board1 = Board()
steps = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if board1.board[player1.y-1][player1.x] == 0:
                    player1.move_up()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if board1.board[player1.y+1][player1.x] == 0:
                    player1.move_down()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if board1.board[player1.y][player1.x-1] == 0:
                    player1.move_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if board1.board[player1.y][player1.x+1] == 0:
                    player1.move_right()
            steps += 1
            if steps == 5:
                board1.setBoard()
                steps = 0
    board1.draw()
    player1.draw()
    pygame.display.update()
