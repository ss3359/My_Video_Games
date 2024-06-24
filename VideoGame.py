
import pygame 
import math 
import random


# Pygame setup 
pygame.init() 
SCREEN_WIDTH=500
SCREEN_HEIGHT=500

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock() 
run=True
player_pos =pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
dt=0
while(run==True): 
    #poll for events 
    #pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get(): 
        if event.type== pygame.QUIT: 
            run=False 
    # Fill the screen with a color to wipe away anything from the last frame. 
    screen.fill("red")
    pygame.draw.circle(screen,"green",player_pos,40)

    #Render your game here
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP]: 
        player_pos.y-=300*dt
    if keys[pygame.K_DOWN]: 
        player_pos.y+=300*dt
    if keys[pygame.K_LEFT]: 
        player_pos.x-=300*dt
    if keys[pygame.K_RIGHT]: 
        player_pos.x+=300*dt

    #flip() the display to put your work on the screen. 
    pygame.display.flip() 


    #limits FPS to 60
    #dt is the delta time in seconds since last frame, used for framerate
    # independent physics 
    dt = clock.tick(60)/1000 
pygame.quit()
    
     

