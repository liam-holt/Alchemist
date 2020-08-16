from Alchemist import Alchemist
from Maps import Maps
#import Combat

ROWS = 5
COLUMNS = 10

FLOWER = '@'
BOTTLE = '%'
CATALYST = '!'
ANIMAL = '}'
BOSS = '?'

def move():
    valid = False

    while (not valid):
        choice = input("W = Up, A = Left, S = Down, D = right: ")

        choice = choice.upper()

        if choice == 'W' or choice == 'A' or choice == 'S' or choice == 'D':
            valid = True

    return choice

def check_pick_up(pick_up):
    if pick_up == FLOWER:
        print("You got a flower!")
    elif pick_up == BOTTLE:
        print("You got a bottle!")
    elif pick_up == CATALYST:
        print("You got a catalyst!")
    elif pick_up == ANIMAL:
        print("You got an animal part")
    elif pick_up == BOSS:
        print("uhoh!")
    else:
        pass

if __name__ == '__main__':
    game_over = False

    name = input("What is your name? ")

    alchemist = Alchemist(name)

    maps = Maps(ROWS, COLUMNS)
    maps.new_map(1)

    while (not game_over):
        potential_pick_up = maps.set_alchemist_position(alchemist)
        check_pick_up(potential_pick_up)
        maps.print_map()
        movement = move()
        is_new_map = alchemist.move(movement, ROWS, COLUMNS)
        if is_new_map:
            maps.new_map(0)
            potential_pick_up = maps.set_alchemist_position(alchemist)
