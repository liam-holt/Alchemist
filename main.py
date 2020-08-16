"""
Author: Liam Trotter
Date: August 2020
Description:
    A simple game to practice Python syntax for Classes
    You play as an Alchemist, collect ingredients and mix them
    together to fight off a Harpy, then a Wyvern, then a Dragon
    WIP
"""


from Alchemist import Alchemist
from Maps import Maps

# import Combat

ROWS = 5
COLUMNS = 10

FLOWER = '@'
CONTAINER_OR_CATALYST = '?'
ANIMAL_PARTS = '%'
BOSS = '!'


def user_choice():
    valid = False
    valid_choices = ("W", "A", "S", "D", "E")

    while not valid:
        choice = input("W = Up, A = Left, S = Down, D = right,"
                       " E = Open Inventory: ")

        choice = choice.upper()

        if choice in valid_choices:
            valid = True

    return choice


def check_pick_up(pick_up):
    if pick_up == FLOWER:
        alchemist.inventory.add_ingredient(FLOWER)
    elif pick_up == CONTAINER_OR_CATALYST:
        alchemist.inventory.add_ingredient(CONTAINER_OR_CATALYST)
    elif pick_up == ANIMAL_PARTS:
        alchemist.inventory.add_ingredient(ANIMAL_PARTS)
    elif pick_up == BOSS:
        print("boss code for later")
        # pause for user
        input()
    else:
        pass


if __name__ == '__main__':
    game_over = False
    first_map = True

    name = input("What is your name? ")

    alchemist = Alchemist(name)

    maps = Maps(ROWS, COLUMNS)
    maps.new_map(first_map)

    while not game_over:
        first_map = False
        potential_pick_up = maps.set_alchemist_position(alchemist)
        check_pick_up(potential_pick_up)
        maps.print_map()
        choice = user_choice()
        is_new_map = alchemist.user_choice(choice, ROWS, COLUMNS)
        if is_new_map:
            maps.new_map(first_map)
            potential_pick_up = maps.set_alchemist_position(alchemist)
