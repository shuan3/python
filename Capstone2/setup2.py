# from card_utils import Player, Card, Deck,playing
import random
from constants import values, ranks, suits


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop(0)
        return single_card


test_deck = Deck()
test_deck.shuffle()
test_deck.shuffle()
print(len(test_deck.deck))
lol = []
print(test_deck.deck.pop(0))
lol.append(test_deck.deck.pop(0))
# test_deck.deal()
print(lol)
print(len(test_deck.deck))


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        # if total value >21 and i still have ac
        # then change my ace to be a instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()
test_deck.shuffle()
test_player = Hand()
pulled_card = test_deck.deal()
pulled_card = test_deck.deck.pop(0)
print(pulled_card, "pulled_card")
test_player.add_card(pulled_card)
print(f"now test player has card {test_player.value}")
print(test_player.cards)


kk = []
lol = [1, 2, 3, 4, 5]
s = lol.pop()
kk.append(s)
print(kk)


class Chips:
    def __init__(self, total=100) -> None:
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("how many chis would you like to bet?"))
        except:
            print("Sorrty a bet must be an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global palying
    while True:
        x = input("Hit or stand? Enter h or s")
        if x[0].lower() == "h":
            hit(deck, hand)
        elif x[0].lower * () == "s":
            print("player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry,please try again")
            continue
        break


def show_some(player, dealer):
    print("\n Dealer's hand:")
    print("first card hidden!")
    print(dealer.cards[1])
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print(f"\n Value of Dealers hand is {dealer.value}")

    print("\n Player's hand")
    for card in player.cards:
        print(card)
    print(f"\n Value of Players hand is {player.value}")
