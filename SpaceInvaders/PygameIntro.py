import pygame,sys
import os
import math




pygame.init()

window =pygame.display.set_mode((500,500))
pygame.display.set_caption("My PyGame Tutorial!")

#Variables
# X=50
# Y=425
# WIDTH=64
# HEIGHT=64
# VELOCITY=10

# key_down=False
# IsJump=False
# JumpCount=10
# left =False
# right=False
# WalkCount=0
running=True
CLOCK=pygame.time.Clock()

#Images 
WalkLeft=[pygame.image.load("Game/L1.png"), 
         pygame.image.load("Game/L2.png"),
          pygame.image.load("Game/L3.png"),
           pygame.image.load("Game/L4.png"),
            pygame.image.load("Game/L5.png"),
            pygame.image.load("Game/L6.png"),
            pygame.image.load("Game/L7.png"),
            pygame.image.load("Game/L8.png"),
            pygame.image.load("Game/L9.png")]

WalkRight=[pygame.image.load("Game/R1.png"), 
         pygame.image.load("Game/R2.png"),
          pygame.image.load("Game/R3.png"),
           pygame.image.load("Game/R4.png"),
            pygame.image.load("Game/R5.png"),
            pygame.image.load("Game/R6.png"),
            pygame.image.load("Game/R7.png"),
            pygame.image.load("Game/R8.png"),
            pygame.image.load("Game/R9.png")]
background=pygame.image.load("Game/bg.jpg")
char = pygame.image.load("Game/standing.png")


#Functions/Classes

class Player: 
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.veloclty=5
        self.IsJump=False
        self.JumpCount=10
        self.left =False
        self.right=False
        self.WalkCount=0
        self.standing=True
        self.hitbox=(self.x,self.y,28,60)

        pass
    def draw(self,window): 
         # pygame.draw.rect(window,(224, 27, 182),(X,Y,WIDTH,HEIGHT))
        if not self.standing: 
            if(self.WalkCount+1>=27): 
                self.WalkCount=0
            if self.left: 
                window.blit(WalkLeft[self.WalkCount//3],(self.x,self.y))
                self.WalkCount+=1
            elif self.right: 
                window.blit(WalkRight[self.WalkCount//3], (self.x,self.y))
                self.WalkCount+=1
        else:
            if(self.right):
                window.blit(WalkRight[0],(self.x,self.y)) 
            elif(self.left): 
                window.blit(WalkLeft[0], (self.x,self.y))

        # window.blit(char,(self.x,self.y))
        self.hitbox=(self.x,self.y,28,60)
        pygame.draw.rect(window,(255,0,0),self.hitbox,2)

class Projectile: 
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius =radius
        self.color=color
        self.facing=facing
        self.velocity=5*facing
    def draw(self,window):
        pygame.draw.circle(window, self.color,(self.x,self.y), self.radius) 

class Enemy: 
     EWalkLeft=[pygame.image.load("Game/L1E.png"),
               pygame.image.load("Game/L2E.png"),
               pygame.image.load("Game/L3E.png"),
               pygame.image.load("Game/L4E.png"),
               pygame.image.load("Game/L5E.png"),
               pygame.image.load("Game/L6E.png"),
               pygame.image.load("Game/L7E.png"),
               pygame.image.load("Game/L8E.png"),
               pygame.image.load("Game/L9E.png"),
               pygame.image.load("Game/L10E.png"),
               pygame.image.load("Game/L11E.png")]
    
     EWalkRight=[pygame.image.load("Game/R1E.png"),
               pygame.image.load("Game/R2E.png"),
               pygame.image.load("Game/R3E.png"),
               pygame.image.load("Game/R4E.png"),
               pygame.image.load("Game/R5E.png"),
               pygame.image.load("Game/R6E.png"),
               pygame.image.load("Game/R7E.png"),
               pygame.image.load("Game/R8E.png"),
               pygame.image.load("Game/R9E.png"),
               pygame.image.load("Game/R10E.png"),
               pygame.image.load("Game/R11E.png")]
     def __init__(self,x,y,width,height,end): 
            self.x=x
            self.y=y
            self.width=width
            self.height=height
            self.left=False
            self.right=True
            self.end=end
            self.path=[self.x,self.end]
            self.WalkCount=0
            self.velocity=3
    
     def draw(self,window):
         self.move()
         if(self.WalkCount+1>=33): 
             self.WalkCount=0
         if(self.velocity>0): 
            window.blit(self.EWalkRight[self.WalkCount//3],(self.x,self.y))
            self.WalkCount+=1
         elif(self.velocity<0): 
            window.blit(self.EWalkLeft[self.WalkCount//3],(self.x,self.y))
            self.WalkCount+=1  

     def move(self):
        if self.velocity>0:
            if(self.x+self.velocity<=self.path[1]): 
                self.x+=self.velocity
            else: 
                self.velocity*=-1
                self.WalkCount=0
        else: 
            if(self.x-self.velocity>self.path[0]): 
                self.x+=self.velocity
            else: 
                self.velocity*=-1
                self.WalkCount=0
            

        


def UpdateTheWindow(): 
    window.blit(background,(0,0))
    man.draw(window) 
    villan.draw(window)
    for bullet in bullets: 
        bullet.draw(window)
    CLOCK.tick(27)
    pygame.display.update()
    

#main loop
man=Player(200,410,64,64)
villan=Enemy(100,410,64,64,450)
bullets=[]
while(running): 
    pygame.time.delay(50)
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            running=False

    for bullet in bullets: 
        if(bullet.x<500 and bullet.x>0): 
            bullet.x+=bullet.velocity
        else: 
            bullets.pop(bullets.index(bullet))
    keys=pygame.key.get_pressed() 
    if keys[pygame.K_s]: 
        if(man.left): 
            facing=-1
        elif(man.right): 
            facing=1
        if len(bullets)<5: 
            bullets.append(Projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))

    if keys[pygame.K_LEFT] and man.x>man.veloclty:
        man.x-=man.veloclty 
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<500-man.width-man.veloclty: 
        man.x+=man.veloclty 
        man.right=True
        man.left=False
        man.standing=False
    else: 
        man.standing=True
        man.WalkCount=0
    if not (man.IsJump): 
        if keys[pygame.K_SPACE]: 
            man.IsJump=True
            man.left=False
            man.right=False
            man.WalkCount=0    
    else: 
        if man.JumpCount>=-10: 
            neg=1
            if man.JumpCount<0:
                neg=-1
            man.y-=((man.JumpCount**2)/2)*neg
            man.JumpCount-=1
        else: 
            man.IsJump=False
            man.JumpCount=10        
    UpdateTheWindow()




#Our Character is not going to move up or down. Save This for now
        # if keys[pygame.K_UP] and Y>VELOCITY: 
        #     Y-=VELOCITY  
        # if keys[pygame.K_DOWN] and Y<500-HEIGHT-VELOCITY: 
        #     Y+=VELOCITY
    # window.fill((0,0,0))
    # pygame.draw.rect(window,(224, 27, 182),(X,Y,WIDTH,HEIGHT))
    # pygame.display.update()
