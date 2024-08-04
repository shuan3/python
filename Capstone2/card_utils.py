# import values
from constants import values, ranks,suits
import random
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank+" of "+self.suit
    
two_hearts=Card("Hearts","Two")
print(two_hearts.value)
# print(values)


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

new_deck=Deck()
first_card=new_deck.all_cards[-1]
print(first_card)
new_deck.shuffle()

first_card=new_deck.all_cards[-1]
print(first_card)






class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)}"
    
new_palyer=Player("Jose")
print(new_palyer)
