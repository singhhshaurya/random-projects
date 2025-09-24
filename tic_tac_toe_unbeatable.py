import random
import time

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
    wins = [(1,2,3),(4,5,6),(7,8,9),
            (1,4,7),(2,5,8),(3,6,9),
            (1,5,9),(3,5,7)]
    for a,b,c in wins:
        if a in moves and b in moves and c in moves:
            return True
    return False

def update(a, moves, moves2, f1, f, marker):
    a = int(a)
    moves.remove(a)
    ind = f.index(str(a))
    f1 = f1[:ind]+marker+f1[ind+1:]
    print(f1)
    print("")
    moves2.append(a)
    return moves, moves2, f1

def minimax(moves, comp_moves, your_moves, is_maximizing):
    if win(comp_moves):
        return 1
    if win(your_moves):
        return -1
    if not moves:
        return 0

    if is_maximizing:
        best = -999
        for m in moves:
            new_moves = moves[:]
            new_comp = comp_moves[:]
            new_your = your_moves[:]
            new_moves.remove(m)
            new_comp.append(m)
            score = minimax(new_moves, new_comp, new_your, False)
            best = max(best, score)
        return best
    else:
        best = 999
        for m in moves:
            new_moves = moves[:]
            new_comp = comp_moves[:]
            new_your = your_moves[:]
            new_moves.remove(m)
            new_your.append(m)
            score = minimax(new_moves, new_comp, new_your, True)
            best = min(best, score)
        return best

def best_move(moves, comp_moves, your_moves):
    best_score = -999
    move = None
    for m in moves:
        new_moves = moves[:]
        new_comp = comp_moves[:]
        new_your = your_moves[:]
        new_moves.remove(m)
        new_comp.append(m)
        score = minimax(new_moves, new_comp, new_your, False)
        if score > best_score:
            best_score = score
            move = m
    return move

def game(f, f1):
    comp_moves = []
    your_moves = []
    moves = [1,2,3,4,5,6,7,8,9]
    toss1 = toss()
    if toss1 == 1:
        print("Computer is moving...")
        time.sleep(2)
        a = best_move(moves, comp_moves, your_moves)
        moves, comp_moves, f1 = update(a, moves, comp_moves, f1, f, 'X')
        if win(comp_moves):
            print("COMPUTER WON!")
            return
    
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
        time.sleep(2)
        a = best_move(moves, comp_moves, your_moves)
        moves, comp_moves, f1 = update(a, moves, comp_moves, f1, f, 'X')
        if win(comp_moves):
            print("COMPUTER WON! loser.")
            break

game(f, f1)
