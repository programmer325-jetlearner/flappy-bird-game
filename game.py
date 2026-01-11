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
            
            #handle the animation
            flap_cooldown=5
            self.counter+=1
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
                self.image=self.images[self.index]

            #rotate the bird
            self.image=pygame.transform.rotate(self.images[self.index],self.vel*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)



class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y, position):
        pygame.sprite.Sprite.__init__()
        self.image=pygame.image.load("images/pipe.png")
        self.rect=self.image.get_rect()
        #position 1 is from the top, -1 is from the bottom
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipe_gap/2)]
        elif position==-1:
            self.rect.topleft=[x,y+int(pipe_gap/2)]
    
    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()

class Button:
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    
    def draw(self):
        action=False
        #get mouse postion
        pos=pygame.mouse.get_pos()
        #check mouse over an clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

pipe_group=pygame.sprite.Group()
bird_group=pygame.sprite.Group()
flappy=Bird(100,int(HEIGHT/2))
bird_group.add(flappy)
restart_btn=Button(WIDTH/2-50,HEIGHT/2-50,restart_img)

#main game loop
running=True

while running:

    clock.tick(FPS)
    screen.blit(bg,(0,0))
    pipe_group.draw(screen)
    bird_group.draw(screen)
    #draw and scroll the ground
    screen.blit(ground,(ground_scroll,768))

    #check for score and pass pipe
    if len(pipe_group)>0:
        if(bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right>pipe_group.sprites()[0].rect.right and pass_pipe==False):
            pipe_pass=True
        if pass_pipe==True:
            if(bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.right):
                score+=1
                pass_pipe=False
    draw_score(str(score),font,GREEN,int(WIDTH/2),25)
    
    #check for collision
    if(pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top<0):
        game_over=True
    
    #once the game is over make sure the bird is not flying
    if flappy.rect.bottom>=768:
        game_over=True
        flying=False
     


    




    

        



