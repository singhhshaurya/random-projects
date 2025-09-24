#Rock Paper and Scissors
import random
import time
p1=0
p2=0

ch=''
while ch!='q':
    ch=input("Type Rock/Paper/Scissors or q to Quit. \n")
    print("Computer is thinking...")
    time.sleep(3)
    print("")
    ch=ch.lower()
    p=['rock', 'paper', 'scissors']
    comp=random.randint(0, 2)
    compc=p[comp]
    if ch not in p and ch!='q':
        print("Type correctly.")
        continue
    
    if ch!='q':
        print("Computer choose: ", compc.title())
    else:
        print(f"Your total points:{p1}, computer's total points:{p2}")
        if p1>p2:
            print("You won the game!")
        elif p2>p1:
            print("Computer won the game. Better luck next time")
        else:
            print("The game was drawn!")
        print("Thank you. Now get lost.")

    if ch==compc:
        print("Draw, nobody wins")
        print("Your points:", p1)
        print("Computer's points:",p2)
    elif ch.lower()=='rock' and compc=='paper':
        print("Computer wins!")
        p2+=1
        print("Your points:", p1)
        print("Computer's points:",p2)

    elif ch.lower()=='rock' and compc=='scissors':
        print("You win!")
        p1+=1
        print("Your points:", p1)
        print("Computer's points:",p2)
    elif ch.lower()=='paper' and compc=='rock':
        print("You win!")
        p1+=1
        print("Your points:", p1)
        print("Computer's points:",p2)
    elif ch.lower()=='paper' and compc=='scissors':
        print("Computer wins!")
        p2+=1
        print("Your points:", p1)
        print("Computer's points:",p2)

    elif ch.lower()=='scissors' and compc=='paper':
        print("You win!")
        p1+=1
        print("Your points:", p1)
        print("Computer's points:",p2)
    elif ch.lower()=='scissors' and compc=='rock':
        print("Computer wins!")
        p2+=1
        print("Your points:", p1)
        print("Computer's points:",p2)
