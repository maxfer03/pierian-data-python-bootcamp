from doctest import FAIL_FAST
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
    'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        print("Shuffling deck...")
    
    def deal_one(self): 
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0 
    
    def remove_one(self):
        return self.hand.pop()

    def add_cards(self, new_cards):
        if(type(new_cards) == type([])):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)
            self.score += new_cards.value
            if self.name != 'Dealer': 
                print(f"{self.name}'s Card: {new_cards}")
                print(f"{self.name}'s Score: {self.score}")


    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'



print('Creating new deck...')
deck = Deck()
deck.shuffle()

dealer = Player('Dealer')

player_name = input("Player Name: ")

player = Player(player_name)
print(f'Player {player.name} created.')

dealer_stands = False
while True:
    action = input('Stand or hit? ')
    if(action == 'hit'):
        player.add_cards(deck.deal_one())
        if dealer.score < 19:
            dealer.add_cards(deck.deal_one())
        else: 
            if dealer_stands == False:
                print('The dealer stands.')
                dealer_stands = True
        if player.score == 21:
            print("BLACKJACK!")
            break
        elif player.score > 21:
            print("You lost!")
            break
        elif dealer.score == 21:
            print("Dealer has 21 points. BLACKJACK!\nYou lost!")
            break
        elif dealer.score > 21:
            print("Dealer's score higher than 21.\n You won!")
            break
    if(action == 'stand'):
        print(f'You stand with {player.score} points.')
        print(f'The dealer has {dealer.score} points.')

        if player.score > dealer.score: print("You won!")
        elif player.score == dealer.score: print("Tie!")
        else: print("You lost!")

        break


