from card_utils import Player, Card, Deck

one = "super_man"
two = "homelander"
player_one = Player(one)
player_two = Player(two)

new_deck = Deck()
new_deck.shuffle()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    if len(player_one.all_cards) == 0:
        print(f"{one} out of cards,{two} wins")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(f"{two} out of cards, {one} wins")
        game_on = False
        break
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR")
            if len(player_one.all_cards) < 3:
                print(f"{one} unable to declare war, {two} wins")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print(f"{two} unable to declare war, {one} wins")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
