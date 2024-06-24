import pygame,sys
import math
import random 
import threading
from tkinter import * 

from pygame.locals import *


#Set up pygame
pygame.init()

# Set up the window.
WindowSurface=pygame.display.set_mode((500,500))
FONT=pygame.font.SysFont(None,50)
ICON=pygame.image.load('/Users/owner/Desktop/VideoGamePy/snake.png')

#Snake Head, Snake Body, and Food
SnakeBody=[1]  # This is an array
SnakeFood=-1  # Integer Variable
GREEN = (0, 255, 0)
RED = (255, 0, 0)
clock=pygame.time.Clock()
dt=0

#Functions To Use: 
    # def MoveSnake(DRow,DCol)
    # def IsSnakeEatsFood()
    # def IsSnakeRunsBoundary()
    # def IsSnakeRunsItself()
    # def DisplaySnake(snake)
    # ##


# def MoveSnake(DRow,DColumn):



#Variables For The Window
Destination=pygame.math.Vector2(0,0)
Food=pygame.math.Vector2((WindowSurface.get_width()/2,WindowSurface.get_height()/2))
Snake=pygame.math.Vector2((0, 0))
RectangleRed=pygame.Rect((Food.x-1,Food.x+1,Food.y-1,Food.y+1))
RectangleGreen=pygame.Rect((Snake.x-1, Snake.x+1, Snake.y-1, Snake.y+1))

#Display The Window
pygame.display.set_caption("Snake!")
pygame.display.set_icon(ICON)
# pygame.draw.rect(WindowSurface,GREEN,Snake,RectangleGreen)




# Run The Window
IS_RUNNING=True

while(IS_RUNNING): 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            IS_RUNNING=False

        WindowSurface.fill("black")
        pygame.draw.rect(WindowSurface,'red',Food,40)


        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]: 
            Food.y+=300*dt
        if keys[pygame.K_DOWN]: 
            Food.y-=300*dt 
        if keys[pygame.K_RIGHT]: 
            Food.x+=300*dt
        if keys[pygame.K_LEFT]: 
            Food.x-=300*dt

        pygame.display.flip()

        #limits FPS to 60
        #dt is the delta time in seconds since last frame, used for framerate
        # independent physics
        dt = clock.tick(60)/1000 
    


pygame.quit()      


