import pygame
import sys
import random
from player import Player
from board import Board
from pygame.locals import *


pygame.init()
game_font = pygame.font.SysFont('Comic Sans MS', 30)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ChaoticMaze")

FPS = pygame.time.Clock()
FPS.tick(60)

player1 = Player()
board1 = Board()
steps = 0

player_image = pygame.image.load("assets/chaotic_player.png")
goal_image = pygame.image.load("assets/goal.png")

player_image = pygame.transform.scale(player_image, (player1.player_size, player1.player_size))
goal_image = pygame.transform.scale(goal_image, (board1.tile_size, board1.tile_size))
pygame.display.set_icon(player_image)

def check_win():
    if board1.goal[0] == player1.y and board1.goal[1] == player1.x:
        temp = random.randint(1, 10)
        if temp <= 7:
            return 1
            
        else:
            check = True
            while check:
                goal_x = random.randint(1, board1.size-1)
                goal_y = random.randint(1, board1.size-1)
                if board1.board[goal_y][goal_x] == 0:
                    check = False
            board1.setBoard(player1.x, player1.y)
            return -1
            
def drawPlayer():
    screen.blit(player_image, (player1.x * player1.player_size, player1.y * player1.player_size))

def drawGoal():
    screen.blit(goal_image, (board1.goal[1] * board1.tile_size, board1.goal[0] * board1.tile_size))

def renderMessage(string):
    text_surface = game_font.render(string, True, (255,255,255))
    screen.blit(text_surface, (10,5))

message = "Chaotic Maze"
player_won = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                temp = player1.y-player1.speed
                if temp <= 1:
                    continue
                elif board1.board[temp][player1.x] != 1:
                    player1.move_up()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                temp = player1.y+player1.speed
                if temp >= board1.size-1:
                    continue
                elif board1.board[temp][player1.x] != 1:
                    player1.move_down()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                temp = player1.x-player1.speed
                if temp <= 1:
                    continue
                if board1.board[player1.y][temp] != 1:
                    player1.move_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                temp = player1.x+player1.speed
                if temp >= board1.size-1:
                    continue
                if board1.board[player1.y][temp] != 1:
                    player1.move_right()
            steps = random.randint(1, 10)
            change_speed = random.randint(1, 10)
            player_won = check_win()
            if (player_won == 1):
                message = "You won, Press q to quit or press arrow keys to start again"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        board1.setBoard(1,1)
                        message = ""
            elif (player_won == -1):
                message = "Try again"
            if steps % 7 == 2:
                board1.setBoard(player1.x, player1.y)
            if change_speed <= 3:
                player1.random_change_speed()
        
    board1.draw()
    drawGoal()
    drawPlayer()
    renderMessage(message)
    pygame.display.update()
