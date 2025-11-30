import pygame
from pygame.locals import *
import random

pygame.init()

clock=pygame.time.Clock()
FPS=60

WIDTH=865
HEIGHT=964

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("flappy bird")
font=pygame.font.SysFont("Arial",60)

#game variables
ground_scroll=0
scroll_speed=4
flying=False
game_over=False
pipe_gap=150
pipe_frequency=1500
last_pipe=pygame.time.get_ticks()-pipe_frequency
score=0
pass_pipe=False

#load the images
bg=pygame.image.load("images/bg.png")
ground=pygame.image.load("images/ground.png")
restart_img=pygame.image.load("images/restart.png")


