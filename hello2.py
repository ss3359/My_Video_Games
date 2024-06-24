import math
import random

#constant variables
N=6; 

guess=0 
attempts=1
GuessNumber=0
ActualNumber=random.randint(1,100)

#Start The Game
print("What is your name? ")
name=input(); 

print("Welcome "+name+" to Guess My Number! ")
print("Please Pick a Number between 1 and 100"); 

while(attempts<=N): 
    GuessNumber=int(input())
    if(GuessNumber<ActualNumber): 
        print("Your guess is too low")
    elif(GuessNumber>ActualNumber): 
        print("Your guess is too high")
    else:
        break; 
    attempts=attempts+1

if(GuessNumber==ActualNumber): 
    print("Congratulations! You have guessed correctly in "+ str(attempts)+" guesses")
elif(GuessNumber!=ActualNumber): 
    print("Ooh sorry! You did not guess correctly within "+ str(attempts)+" guesses")
    print("The number I am thinking of was "+ str(ActualNumber))
 
