# stone, paper, scissor game using Python
# coded with <3 by V01D.
# DasGeek (only added some flare to the win text and print out of the rock paper scissor options so user doesn't have to manually reference)
# All credit belongs to VO1D and head to https://inventyourshit.com/how-to-make-stone-paper-and-scissor-game-in-python/


import random                   # importing Random module 
import pyfiglet                 # importing Pyfiglet module

ascii_banner = pyfiglet.figlet_format("Stone , Paper & Scissor GAME ")  # ascii banner using Pyfiglet
print(ascii_banner)





print("\t Welcome to the Game \n")
print(" \tROCK PAPER & SCISSOR ")
print("........................................\n")


player1 = input("Enter your Name: ")
print("\n")


print("Playing Mode: ")
print("1. COM ")
print("2. Player 2 ")
print("\n")



mode = input("Enter your Choice: ")
mode = int(mode)
print("1=Stone, 2=Paper, 3=Scissors")
print("\n")

if(mode==1):                                #  mode 1 Vs COM
    point1=0
    point2=0

    while( point1<3 or point2<3):          # initializing a while loop till 3 points

        st = 1                             # stone = 1 ; stone is represented by 1 
        pa = 2                             # paper = 2 ; paper is represented by 2 
        sc = 3                             # scissor = 3 ; scissor is represented by 3

        chance1 = input("Player1: ")        # asking for input for player1
        chance1 = int(chance1)
        print("1=Stone, 2=Paper, 3=Scissors")
        print("\n")
        chance2 = 0                         # making chance2 variable to 0 so that it can become a int 
        chance2=random.randint(1, 3)        # using randint random number from random module with series btw 1 and 3 
        print("Player2: ",chance2)

    
        
    
        if(chance1==1 and chance2==3 or chance1==1 and chance2==3 or chance1==2 and chance2==1):    # winning condition for player1

            print("\n")
            print("Player1 got one point")
            point1=point1+1
            print("\n")
            
            if(point1==3):                                      # if condition is TRUE ; it will come out of loop
                print("\n")                                  
                player1win = pyfiglet.figlet_format("Player 1 Won!")  # ascii banner using Pyfiglet
                print(player1win)
                break
        elif(chance1==1 and chance2==1 or chance1==2 and chance2==2 or chance1==3 and chance2==3):
            print("No points won! ; Play Again")
                
        else:
            print("\n")
            print("player2 got one point")
            point2=point2+1
            print("\n") 
              
            if(point2==3):
                print("\n")
                player2win = pyfiglet.figlet_format("Player 2 Won!")  # ascii banner using Pyfiglet
                print(player2win)
                break   


elif(mode==2):                                # mode 2 vs Player 2
    point1=0
    point2=0

    while( point1<3 or point2<3):          # initializing a while loop till 3 points

        st = 1                             # stone = 1 ; stone is represented by 1 
        pa = 2                             # paper = 2 ; paper is represented by 2 
        sc = 3                             # scissor = 3 ; scissor is represented by 3

        chance1 = input("Player1: ")        # asking for input for player1
        chance1 = int(chance1)
        print("\n")

        chance2 = input("Player2: ")        # asking for input for player 2
        chance2 = int(chance2)
        print("\n")

    
        
    
        if(chance1==1 and chance2==3 or chance1==1 and chance2==3 or chance1==2 and chance2==1):    # winning condition for player1

            print("\n")
            print("Player1 got one point")
            point1=point1+1
            print("\n")
            
            if(point1==3):                                      # if condition is TRUE ; it will come out of loop
                print("\n")                                  
                print("\t........> Player1 won!!! ........")
                break
        else:
            print("\n")
            print("player2 got one point")
            point2=point2+1
            print("\n") 
              
            if(point2==3):
                print("\n")
                print("\t........> Player2 won!!! ........")
                break   






#   Thank You for reading this code. Orginally developed By "V01D" from www.inventyourshit.com