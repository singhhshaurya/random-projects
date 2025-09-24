import random
import time
'''  a="| 1 | 2 | 3 |"
     b="| 4 | 5 | 6 |"
     c='| 7 | 8 | 9 |  '''

f='| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |'
f1='|   |   |   |\n|   |   |   |\n|   |   |   |'
print("PRESS q TO QUIT")
print(f,"\n")

def toss():
    toss=['heads', 'tales']
    while True:
        a=input("Toss! Enter either heads or tales: ")
        if a in toss:
            break
        else:
            print("Enter only heads or tales.")
    
    c=random.choice(toss)
    print("Tossing....")
    time.sleep(3)
    if a.lower()==c:
        print(f"Its {c}, You won the toss! You will move first")
        return 0
    else:
        print(f"Its {c}, the computer will go first.")
        return 1

def win(moves):
    for i in [3,5,7]:
        if i not in moves:
            break
    else:
        return True
    for i in [1,5,9]:
        if i not in moves:
            break
    else:
        return True
    for i in range(1, 4):
        for j in range(3):
            val = i+j*3
            if val not in moves:
                break
        else:
            return True
    for i in range(1, 8, 3):
        for j in range(3):
            if i+j not in moves:
                break
        else:
            return True
    return False
        

def update(a, moves, moves2, f1, f, marker):
    a = int(a)
#     if a not in moves:
#         print("Enter a non-filled choice.")
#         return moves, moves2, f1
    moves.remove(a)
    ind = f.index(str(a))
    f1 = f1[:ind]+marker+f1[ind+1:]
    print(f1)
    print("")
    moves2.append(a)
    return moves, moves2, f1
    
    
    
def game(f, f1):
    BOLD = '\033[1m'
    END = '\033[0m'
    comp_moves = []
    your_moves = []
    moves = [1,2,3,4,5,6,7,8,9]
    toss1 = toss()
    if toss1 == 1:
        print("Computer is moving...")
        time.sleep(3)
        a = random.choice(moves)
        moves, comp_moves, f1 = update(a, moves, comp_moves, f1, f, 'X')
        if win(comp_moves):
            print("COMPUTER WON!")
    
    while True:
        a = (input("Your move. Enter your choice: "))
        if a == 'q':
            break
        elif a.isdigit():
            if int(a) not in moves:
                print("Enter a non-filled choice.")
                continue
            moves, your_moves, f1 = update(a, moves, your_moves, f1, f, 'O')
        else:
            print("ENTER A VALID NUMBER.")
            continue
            
        if win(your_moves):
            print("CONGRATS! YOU WIN.")
            break
        if moves == []:
            print("ITS A DRAW.")
            break
            
        print("Computer is moving...")
        time.sleep(3)
        a = random.choice(moves)
        moves, comp_moves, f1 = update(a, moves, comp_moves, f1, f, 'X')
        if win(comp_moves):
            print("COMPUTER WON! loser.")
            break
        
        
game(f, f1)
