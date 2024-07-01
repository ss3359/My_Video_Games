import pygame, sys 
import math
import numpy
import random 
import time 
import os


# Space Invaders 



if __name__=="__main__": 
    pygame.init()
# Load The Images
RED_SPACE_SHIP=pygame.image.load(os.path.join("SpaceInvaders/assets","pixel_ship_red_small.png"))
GREEN_SPACE_SHIP=pygame.image.load(os.path.join("SpaceInvaders/assets","pixel_ship_green_small.png"))
BLUE_SPACE_SHIP=pygame.image.load(os.path.join("SpaceInvaders/assets","pixel_ship_blue_small.png"))

#Player Spaceship
YELLOW_SPACE_SHIP=pygame.image.load(os.path.join("SpaceInvaders/assets","pixel_ship_yellow.png"))
#Background Image
BACKGROUND=pygame.image.load(os.path.join("SpaceInvaders/assets","stars.jpg"))

#Display The Window
window=pygame.display.set_mode((1198,694))
window.blit(BACKGROUND,(1198,694))
# window.fill((245, 179, 66)) 
pygame.display.set_caption("Space Invaders")
pygame.display.flip()

Run=True



while(Run): 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            Run=False

