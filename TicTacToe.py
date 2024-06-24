import random 
import pygame
import math
import threading


# Global Variables
NewBoard=[["$","$","$"], 
          ["$","$","$"], 
          ["$","$","$"]]

def DrawBoard(NewBoard): 
    print(NewBoard[0][0]+"|"+NewBoard[0][1]+"|"+NewBoard[0][2])
    print("-|-|-")
    print(NewBoard[1][0]+"|"+NewBoard[1][1]+"|"+NewBoard[1][2])
    print("-|-|-")
    print(NewBoard[2][0]+"|"+NewBoard[2][1]+"|"+NewBoard[2][2])
    print()

def PlayerTurn(board,marker): 
    turn=True
    while(turn): 
        print("Put a marker on the board")
        number1=int(input())
        number2=int(input())

        if(board[number1][number2]!="$"): 
            print("That spot has already been taken! Enter another spot")
        else: 
            board[number1][number2]=marker
            turn=False
def ComputerTurn(board,marker): 
    j=0
    result=True
    number=1
    while(result==True and number<=9): 
        number1 = random.randint(0,2)
        number2=random.randint(0,2)
        if(board[number1][number2]=="$"): 
            board[number1][number2]=marker
            result=False
        else: 
            number+=1

def CoinToss(): 
    coin=random.randint(0,1)
    if coin==0: 
        return True
    return False

def CheckRow(NewBoard,marker):
    j=0
    for i in range(0,len(NewBoard[0])): 
            if NewBoard[i][j]==marker and NewBoard[i][j+1]==marker and NewBoard[i][j+2]==marker : 
                return True
            else: 
                j=0
    return False         

def CheckColumn(NewBoard,marker):
    i=0
    for j in range(0,len(NewBoard[0])): 
            if NewBoard[i][j]==marker and NewBoard[i+1][j]==marker and NewBoard[i+2][j]==marker : 
                return True
            else: 
                i=0
    return False  
   
def CheckDiagonal(NewBoard,marker): 
    if(NewBoard[0][0]==marker and NewBoard[1][1]==marker and NewBoard[2][2]==marker): 
        return True 
    elif(NewBoard[2][0]==marker and NewBoard[1][1]==marker and NewBoard[0][2]==marker): 
        return True 
    else: 
        return False  


def IsThereThreeInARow(NewBoard,marker): 
    if(CheckDiagonal(NewBoard,marker) or CheckRow(NewBoard,marker) or CheckColumn(NewBoard,marker)): 
        return True
    return False

def PlayTicTacToe(PlayerMark,ComputerMark,PlayerFirst): 
    EndGame=False
    while(EndGame==False):
        if(PlayerFirst==True):
            PlayerTurn(NewBoard,PlayerMark)
            if(IsThereThreeInARow(NewBoard,PlayerMark)==True): 
                print("Three Marks For Player Found")
                EndGame=True
            DrawBoard(NewBoard)
            ComputerTurn(NewBoard,ComputerMark)
            if(IsThereThreeInARow(NewBoard,ComputerMark)==True): 
                print("Three Marks For Computer Found")
                EndGame=True
            DrawBoard(NewBoard)
        elif(PlayerFirst==False):
            ComputerTurn(NewBoard,ComputerMark)
            if(IsThereThreeInARow(NewBoard,ComputerMark)==True): 
                print("Three Marks For Computer Found")
                EndGame=True
            DrawBoard(NewBoard)

            PlayerTurn(NewBoard,PlayerMark)
            if(IsThereThreeInARow(NewBoard,PlayerMark)==True): 
                print("Three Marks For Player Found")
                EndGame=True
            DrawBoard(NewBoard)

 



       

def main():
    decision=True
    PlayerFirst=CoinToss()
    while(decision): 
        if(PlayerFirst==True): 
            PlayerMark="X"
            ComputerMark="O"
            PlayerFirst=True
        else: 
            ComputerMark="X"
            PlayerMark="O"
            PlayerFirst=False
            
        PlayTicTacToe(PlayerMark,ComputerMark,PlayerFirst)

        print("Would you like to play again?")
        StringDecision=input()
        if(StringDecision=="yes" or StringDecision=='y' or StringDecision=="YES"): 
            decision=False



main()




