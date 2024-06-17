import random
options=("rock","paper","scissors")
ans='y'
while ans=='y':
    computer=random.choice(options)
    player=input("enter a choice from:{rock,paper,scissors}")
    print(computer)
    if player not in options:
          print("enter a valid choice")
    else :
        if player==computer:
            print("it's a draw")
        elif player=="rock" and computer=="scissors":
            print("you win")
        elif player=="paper" and computer=="rock":
            print("you win")
        elif player=="scissors" and computer=="paper":
            print("you win")
        else:
            print("you lost")
        ans=input("wanna play again:y/n")
            
    
                
                

    
