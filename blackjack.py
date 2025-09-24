# BLACKJACK BAYBAY
import random
import time

cards = 'Ace.2.3.4.5.6.7.8.9.10.Jack.Queen.King'
cards1 = cards.split(".")
suits = ['Clubs', "Hearts", 'Spades', "Diamonds"]

values = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10
}

def get_card():
    return random.choice(cards1), random.choice(suits)

def hand_value(hand):
    value = sum(values[c[0]] for c in hand)
    aces = sum(1 for c in hand if c[0] == 'Ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

print("SHUFFLING DECK...")
time.sleep(3)

player_hand = [get_card(), get_card()]
dealer_hand = [get_card(), get_card()]

print("Your cards:", player_hand, "Value:", hand_value(player_hand))
print("Dealer shows:", dealer_hand[0])

while hand_value(player_hand) < 21:
    print("Press 'W' to hit or 'S' to stand")
    move = input("").lower()
    if move == 'w':
        card = get_card()
        player_hand.append(card)
        print("You drew:", card, "Now you have:", player_hand, "Value:", hand_value(player_hand))
    elif move == 's':
        break
    else:
        print("W or S only.")

if hand_value(player_hand) > 21:
    print("You busted! Dealer wins.")
else:
    print("Dealer's turn...")
    time.sleep(2)
    print("Dealer has:", dealer_hand, "Value:", hand_value(dealer_hand))
    while hand_value(dealer_hand) < 17:
        time.sleep(2)
        card = get_card()
        dealer_hand.append(card)
        print("Dealer drew:", card, "Now dealer has:", dealer_hand, "Value:", hand_value(dealer_hand))

    if hand_value(dealer_hand) > 21:
        print("Dealer busted! You win.")
    elif hand_value(dealer_hand) > hand_value(player_hand):
        print("Dealer wins with", hand_value(dealer_hand))
    elif hand_value(dealer_hand) < hand_value(player_hand):
        print("You win with", hand_value(player_hand))
    else:
        print("It's a tie.")
