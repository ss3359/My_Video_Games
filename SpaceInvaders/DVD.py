import pygame,sys 
import os 



#Start The Game
pygame.init()

#Constants
WIDTH=800
HEIGHT=600
SQUARE_WIDTH=100
SQUARE_HEIGHT=100
XVELOCITY=1
YVELOCITY=1
LOGOS=[(227, 11, 11), (156, 237, 17), (17, 237, 208),(138, 17, 237)]


#Global Variables
x=400
y=300
running=True
position=0
stop=False

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DVD LOGO")
pygame.display.update()



#Functions: 
def UpdateWindow(x,y,pos):
    global XVELOCITY
    global YVELOCITY
    global stop
    while x>=0 and x<=WIDTH-SQUARE_WIDTH and y >=0 and y<=HEIGHT-SQUARE_HEIGHT:
        if(x+SQUARE_WIDTH==WIDTH or x==0):    
                XVELOCITY=-XVELOCITY
                pos+=1
        elif(y+SQUARE_HEIGHT==HEIGHT or y==0): 
            YVELOCITY=-YVELOCITY
            pos+=1
        x+=XVELOCITY
        y+=YVELOCITY  
        window.fill((0,0,0))
        pygame.draw.rect(window,LOGOS[pos%4],(x,y,SQUARE_WIDTH,SQUARE_HEIGHT))
        pygame.display.flip() 



    # while x>=0 and x<=WIDTH-SQUARE_WIDTH and y >=0 and y<=HEIGHT-SQUARE_HEIGHT:
        
        # elif(x+SQUARE_WIDTH==WIDTH  and y+SQUARE_HEIGHT==HEIGHT): 
        #     XVELOCITY=-XVELOCITY
        #     YVELOCITY=-YVELOCITY
        #     pos+=1
        # elif(x+SQUARE_WIDTH==WIDTH  and y==0): 
        #     XVELOCITY=-XVELOCITY
        #     pos+=1
        # elif(x==0 and y+SQUARE_HEIGHT==HEIGHT): 
        #     YVELOCITY=-YVELOCITY
        #     XVELOCITY=-XVELOCITY
        #     pos+=1

       
        
        
            
    


while(running): 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            running=False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: 
            running=False
            
    UpdateWindow(x,y,position)
        
        

