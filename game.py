import pygame
from pygame.locals import *
import random

pygame.init()

clock=pygame.time.Clock()
FPS=60

WIDTH=865
HEIGHT=964
GREEN=(0,255,0)

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

def draw_score(text,font,green,x,y):
    score_text=font.render(text,True,green)
    screen.blit(score_text,(x,y))

#bird
class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for num in range(1,4):
            img=pygame.image.load(f"images/bird{num}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False
    
    def update(self):
        if flying==True:
            #apply the gravity
            self.vel+=0.5
            if self.vel>8:
                self.vel=8
            
            if self.rect.bottom<768:
                self.rect.y+=int(self.vel)
        
        if game_over==False:
            #jump
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel-=10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        



