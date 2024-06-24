import pygame,sys
from pygame.locals import *
import time
import math 
import random

SIZE=40
BACKGROUND_COLOR=(173, 3, 252)
class Apple:
    def __init__(self,parent_screen): 
        self.parent_screen=parent_screen
        self.AppleImage=pygame.image.load("apple.jpg")
        self.x=SIZE*3
        self.y=SIZE*3

    def draw(self):  
          #self.parent_screen.fill((177,3,252))
          self.parent_screen.blit(self.AppleImage,(self.x,self.y))
          pygame.display.flip()

    def IsCollision(self,x1,y1,x2,y2):
        if(x1>=x2 and x1<=x2+SIZE): 
            if(y1>=y2 and y1<=y2+SIZE): 
                return True   

    def move(self): 
         self.x=random.randint(0,24)*SIZE
         self.y=random.randint(0,19)*SIZE       
         

class Snake: 
    def __init__(self,parent_screen,length): 
        self.length=length
        self.parent_screen=parent_screen
        self.square1=pygame.image.load("block.jpg")
        pygame.display.set_caption("Snake Game!")
        self.x=[SIZE]*length
        self.y=[SIZE]*length
        self.direction='down'
        
        
    def draw(self): 
       self.parent_screen.fill(BACKGROUND_COLOR)
        
       for i in range(self.length): 
          self.parent_screen.blit(self.square1,(self.x[i],self.y[i]))
       pygame.display.flip()

    def MoveLeft(self): 
        self.direction="left"
    def MoveRight(self): 
        self.direction="right"
    def MoveUp(self): 
        self.direction="up"
    def MoveDown(self): 
       self.direction="down"

    def IncreaseSize(self): 
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def SnakeWalks(self):
        for i in range(self.length-1,0,-1): 
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]       
        if self.direction=="up": 
            self.y[0]-=SIZE
        elif self.direction=="down": 
            self.y[0]+=SIZE
        elif self.direction=="right": 
            self.x[0]+=SIZE
        elif self.direction=="left": 
            self.x[0]-=SIZE
        self.draw()
        




class Game: 
    def __init__(self): 
        pygame.init()
        self.WindowSurface=pygame.display.set_mode((1000,800))
        self.WindowSurface.fill((173, 3, 252))
        self.PlayBackgroundMusic()
        self.snake = Snake(self.WindowSurface,1)
        self.snake.draw()
        self.apple=Apple(self.WindowSurface)
        self.apple.draw()

    def PlayBackgroundMusic(self): 
        pygame.mixer.music.load("Super Mario Bros. medley.mp3")
        pygame.mixer.music.play()

    def RenderBackground(self): 
        bg=pygame.image.load("Sand.jpg")
        pygame.transform.scale(bg,(1000,800))
        self.WindowSurface.blit(bg,(0,0))
       
    def DisplayScore(self): 
        font=pygame.font.SysFont('arial',30)
        score=font.render(f"Score: {self.snake.length}",True,(255,255,255))
        self.WindowSurface.blit(score,(800,10))
        title=font.render("SNAKE GAME",True,(255,255,255))
        self.WindowSurface.blit(title,(10,800))
        pygame.display.flip()

    def ShowGameOver(self): 
        self.WindowSurface.fill(BACKGROUND_COLOR)
        font2=pygame.font.SysFont('arial',30)
        line1=font2.render(f"GAME OVER! Your Score is {self.snake.length}",True,(255,255,255))
        self.WindowSurface.blit(line1,(200,300))
        line2=font2.render("Play Again? Press ENTER for yes or ESC for no.",True,(255,255,255))
        self.WindowSurface.blit(line2,(200,350))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset(self): 
        self.snake = Snake(self.WindowSurface,1)
        self.apple=Apple(self.WindowSurface)

    def run(self): 
        run=True
        pause=False
        while(run):
            for event in pygame.event.get(): 
                    if event.type==KEYDOWN:
                        if event.key==K_RETURN: 
                             pause=False
                             pygame.mixer.music.play()
                        if event.key==K_ESCAPE: 
                            exit(0)
                        if not pause:
                            if event.key==K_UP: 
                                self.snake.MoveUp()
                            if event.key==K_DOWN: 
                                self.snake.MoveDown()
                            if event.key==K_RIGHT: 
                                self.snake.MoveRight()
                            if event.key==K_LEFT: 
                                self.snake.MoveLeft()
                    elif event.type==QUIT: 
                        run=False
            try: 
                if not pause: 
                    self.play()
            except Exception as e: 
                self.ShowGameOver()
                sound=pygame.mixer.Sound("super-mario-death-sound-sound-effect.mp3")
                pause=True
                pygame.mixer.Sound.play(sound)
                self.reset()
           
            time.sleep(0.1)

    def play(self): 
        self.snake.SnakeWalks()
        self.apple.draw()
        self.DisplayScore()
        pygame.display.flip()
        #snake eating the apple 
        if self.apple.IsCollision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y): 
            sound=pygame.mixer.Sound("mario_coin_sound.mp3")
            self.snake.IncreaseSize()
            pygame.mixer.Sound.play(sound)
            self.apple.move()

        # snake colliding with itself 
        for i in range(3, self.snake.length): 
            if self.apple.IsCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
               raise "Game Over"


if __name__=="__main__": 
    g=Game()
    g.run()                

   
       


    




