import pygame
import sys
from player import Player
from pygame.locals import *


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ChaoticMaze")

FPS = pygame.time.Clock()
FPS.tick(60)

player1 = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player1.move_up()
                print("press up")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player1.move_down()
                print("press don")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player1.move_left()
                print("press left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player1.move_right()
                print("press right")
    pygame.display.update()
