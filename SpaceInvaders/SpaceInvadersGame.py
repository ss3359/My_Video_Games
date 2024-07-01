import math 
import random
import pygame,sys
import os




#Run The Window
pygame.init()

#Constants
WIDTH=1000
HEIGHT=1000
DISTANCE_BETWEEN_ALIENS=30
VERTICAL_DISTANCE_BETWEEN_ALIENS=100
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
SPACE_VELOCITY=10
BULLET_VELOCITY=10
ALIEN_VELOCITY_X=10
ALIEN_VELOCITY_Y=20
COLORS=[(252, 99, 61),(207, 252, 40),(71, 252, 246),(252, 142, 40)]



#Global Varibales
x=500
y=900 
clock=pygame.time.Clock()

#Ailen Variables (Global)
XAlien1=20
YAlien1=20

XAlien2=20
YAlien2=60

XAlien3=20
YAlien3=140


XAlien4=20
YAlien4=200

XBarrier=20
YBarrier=800

Score=0
Lives=5

RedAliens=[]
GreenAliens=[]
BlueAliens=[]
PinkAiliens=[]


IsLeft=False
IsRight=False

ReachesEnds=False
pygame.display.set_caption("SPACE INVADERS")


#Functions/Classes

class Spaceship: 
    def __init__(self,x,y,width,height): 
        self.x=x
        self.y=y
        self.width=width
        self.height=height
       
    def MoveShipAndUpdateScreen(self,window,IsLeft,ISRight):
        global SPACE_VELOCITY
        if(IsLeft==True): 
            SPACE_VELOCITY*=-1
            self.x+=SPACE_VELOCITY
        elif(IsRight==True): 
            SPACE_VELOCITY*=1
            self.x+=SPACE_VELOCITY
   

class Alien:
    def __init__(self,x,y,color): 
        self.x=x
        self.y=y
        self.color=color
        self.radius=20
        self.yshift=10
        self.width=WIDTH/2

    def draw(self):  
        pygame.draw.circle(WINDOW,self.color,(self.x,self.y),self.radius)
          
class Barrier:
    def __init__(self,x,y,i):
        self.x=x
        self.y=y
        self.i=i
    def draw(self):  
        pygame.draw.polygon(WINDOW,(22, 232, 240),((self.x+200*self.i,self.y),((self.x+100)+200*self.i,self.y),((self.x +(self.x+100))/2+200*self.i,(self.y-100))))
                              
class Projectile: 
    def __init__(self,x,y): 
        self.x=x
        self.y=y
        self.color=(250, 10, 154)
        self.velocity=20
        self.radius=5
    def draw(self): 
        pygame.draw.circle(WINDOW,(250, 10, 154),(self.x,self.y),5)


def move(Aliens):
    global ALIEN_VELOCITY_X 
    for i in range(len(Aliens)): 
        Aliens[i].x+=ALIEN_VELOCITY_X
        if Aliens[i].x>800 or Aliens[i].x< 0:
            ALIEN_VELOCITY_X*=-1
            for i in range(len(Aliens)): 
                Aliens[i].y+=Aliens[i].yshift 
            continue
        pygame.time.delay(5)
        Aliens[i].draw()

 
for i in range(0,6): 
    RedAliens.append(Alien(XAlien1+3*i*DISTANCE_BETWEEN_ALIENS,YAlien1,COLORS[0]))
    GreenAliens.append(Alien(XAlien2+3*i*DISTANCE_BETWEEN_ALIENS,YAlien2,COLORS[1]))
    # BlueAliens.append(Alien(XAlien3+3*i*DISTANCE_BETWEEN_ALIENS,YAlien3,COLORS[2]))
    # PinkAiliens.append(Alien(XAlien4+3*i*DISTANCE_BETWEEN_ALIENS,YAlien4,COLORS[3]))

def ColorTheAliens():
    move(RedAliens)
    move(GreenAliens)
    # move(BlueAliens)
    # move(PinkAiliens)

def distance(x1,y1,x2,y2): 
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

def IsCollisionAlien(bullet, RedAliens,GreenAliens): 
    global Score       
    # for p in PinkAiliens:
    #     if(distance(bullet.x,bullet.y,p.x,p.y)<bullet.radius+p.radius): 
    #         print("Pink Crash")
    #         Score+=10
    #         bullets.pop(bullets.index(bullet))
    # for b in BlueAliens:
    #     if(distance(bullet.x,bullet.y,b.x,b.y)<bullet.radius+b.radius):
    #         print("Blue Crash")
    #         Score+=20 
    #         bullets.pop(bullets.index(bullet))
    for g in GreenAliens: 
        if(distance(bullet.x,bullet.y,g.x,g.y)<bullet.radius+g.radius):
            print("Green Crash")
            Score+=30 
            bullets.pop(bullets.index(bullet))
            g.radius*=0
            g.draw()
    for r in RedAliens:
        if(distance(bullet.x,bullet.y,r.x,r.y)<bullet.radius+r.radius):
            print("Red Crash")
            Score+=40
            r.radius*=2
            r.draw()
            bullets.pop(bullets.index(bullet))
    

def IsCollisionBarrier(bullet,bullets,Barriers):
    pass
    for barrier in Barriers: 
        if(bullet.x==barrier.x and bullet.y==barrier.y):
           print("Collision Barrier: "+barrier.x+" "+barrier.y)
            # Lives-=1
            # bullets.pop(bullets.index(bullet))

         


def UpdateTheWindow(bullets):
    for bullet in bullets: 
        bullet.draw()

def AddBarriers(): 
    for i in range(0,5): 
            b = Barrier(XBarrier,YBarrier,i)
            barriers.append(b)
            font=pygame.font.Font('freesansbold.ttf', 10)
            b.draw()

#Run The Game
spaceship=Spaceship(x,y,50,50)
bullets=[]
barriers=[]
run=True

while run==True: 
    for event in pygame.event.get(): 
        if(event.type==pygame.QUIT): 
            run=False 
        elif(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_SPACE): 
                bullets.append(Projectile(spaceship.x,spaceship.y))


    for bullet in bullets: 
            if(bullet.y<HEIGHT and bullet.y>0): 
               bullet.y-=BULLET_VELOCITY
               IsCollisionAlien(bullet, RedAliens,GreenAliens) 
               IsCollisionBarrier(bullet,bullets,barriers)  
            else: 
                bullets.pop(bullets.index(bullet))  


    keys=pygame.key.get_pressed()
    if(keys[pygame.K_LEFT]): 
        spaceship.x-=SPACE_VELOCITY
    elif(keys[pygame.K_RIGHT]): 
        spaceship.x+=SPACE_VELOCITY
    elif(keys[pygame.K_ESCAPE]): 
        run=False
    
    
    
    WINDOW.fill((0,0,0)) 
    pygame.draw.rect(WINDOW,(23, 230, 44),(spaceship.x,spaceship.y,spaceship.width,spaceship.height))
    ColorTheAliens()
    AddBarriers()
    UpdateTheWindow(bullets)
    pygame.display.update()
