import math 
import random
import pygame,sys
import os


WIDTH=500
HEIGHT=500
RADIUS=5
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")
Clock=pygame.time.Clock()

#Global Variables
x=30
y=30
velocity=10

#Run The Window
pygame.init()

run=True

while(run):
     
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            run=False

    while ( x >= 0 and y >= 0 and x<=300 and y<=300): 
        if x == 0 or x==300:
            y+=velocity
            velocity*=-1
        x+=velocity   
        
        Clock.tick(3)
        pygame.draw.circle(WINDOW,(71, 252, 246),(x,y),RADIUS)
        pygame.display.flip()