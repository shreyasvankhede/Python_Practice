import random
import os
def highscore(score=-1):
    file1="highscore.txt"
    if not os.path.exists(file1):
        x=open(file1, 'w') # Create an empty file
        x.write("0")
        x.close()
    with open(file1) as f:
        high=f.read()
        high=int(high)
    if (score>high):
        f=open(file1,"w")
        f.write(str(score))
        f.close()
    with open(file1) as sc:
        hscore=sc.read()
    return hscore


def game(score=0):
    print('''
          RULES OF THE GAME:
          SNAKE BEATS WATER
          GUN BEATS SNAKE
          WATER BEATS GUN
          ''')
    d={
        1:"Snake",
        0:"Gun",
        -1:"Water"
    }
    while True:
        comp=random.randint(-1,1)
        you=int(input('''
1 For Snake
0 For Gun
-1 For Water
'''))
        if(you<-1 or you>1):
            print("Choose a valid input")
            game(score)
            
        print(f"You chose {d[you]} and Computer chose {d[comp]}")
        if (comp-you==-1) or (comp-you==2):
            print("You lose :( ")
            break
        elif(comp==you):
            print("Its a Draw")
        else:
            print("You win!")
            score+=1
    print(f"Your score streak was {score} !!!!")
    print(f"Highest score is {highscore(score)}")
    choice=input("Would you like to play again? Y/N? : ")
    if (choice=='y' or choice=="Y"):
        game()
    else:
        print("ThankYou for playing we wish to see you again soon :) ")
        return
        
game()

