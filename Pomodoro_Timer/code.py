import pygame
import os 

# Initilising the pygame 
pygame.init()

# color's
BEAUTIFUL = (51,255,255)
BLACK = (0,0,0)
ORANGE = (255,69,0)

WIDTH = 100 
HEIGHT = 100 

MAIN_WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FONT = pygame.font.SysFont('comicsans',50)

run = True 

SECONDS = 60 
MINUTES = 25
TIME = MINUTES*SECONDS

while run:

    MAIN_WIN.fill(BEAUTIFUL)
    pygame.time.wait(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    message = str(TIME//60).zfill(2) +':'+ str(TIME%60).zfill(2)
    txt = FONT.render(message,1,ORANGE)

    MAIN_WIN.blit(txt,(WIDTH//2-txt.get_width()//2,HEIGHT//2-txt.get_height()//2))
    TIME-=1
    if TIME<0:
        run = False 
    pygame.display.update()


    