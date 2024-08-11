def display_game(game_list):
    print("Here is the current list")
    print(game_list)



def position_choice():
    choice='wrong'
    while choice not in ['1','2','0']:
        choice=input("Pick a position 1 ,2 0")
        if choice not in ['1','2','0']:
            print('Sorry')
    return int(choice)

def replement_choice(game_list,position):
    user_placement=input("Type a string at a position ")
    game_list[position]=user_placement
    return game_list


def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input("keep playing?")
        if choice not in ['Y','N']:
            print('Sorry')
    if choice=="Y":
        return True
    else:
        return False

game_on=True
game_list=[0,1,2]
while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=replement_choice(game_list,position)
    display_game(game_list)
