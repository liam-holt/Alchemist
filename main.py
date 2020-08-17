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
from Enemy import *
from Combat import Combat

# game board dimensions
ROWS = 5
COLUMNS = 10

# pick-up icons
FLOWER = '@'
CONTAINER_OR_CATALYST = '?'
ANIMAL_PARTS = '%'
BOSS = '!'

# boss enums
HARPY_BOSS = 1
WYVERN_BOSS = 2
DRAGON_BOSS = 3

def make_boss(boss_enum):
    """
    Makes a boss based on the current boss enum
    :param boss_enum: number representing the current boss
    :return: Enemy: The current boss fight
    """
    if boss_enum == HARPY_BOSS:
        return Harpy("Harpy")
    elif boss_enum == WYVERN_BOSS:
        return Wyvern("Wyvern")
    elif boss_enum == DRAGON_BOSS:
        return Dragon("Dragon")


def user_choice():
    """
    Take and validate user input
    :return: char: movement direction or open inventory
    """
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
    """
    Checks if something was picked up on movement
    :param pick_up: potential pickup (char of tile)
    :return: bool: was tile a boss?
    """
    if pick_up == FLOWER:
        alchemist.inventory.add_ingredient(FLOWER)
    elif pick_up == CONTAINER_OR_CATALYST:
        alchemist.inventory.add_ingredient(CONTAINER_OR_CATALYST)
    elif pick_up == ANIMAL_PARTS:
        alchemist.inventory.add_ingredient(ANIMAL_PARTS)
    elif pick_up == BOSS:
        return True
    else:
        pass

    return False


if __name__ == '__main__':
    game_over = False
    first_map = True

    # name Alchemist and set first letter of name to icon
    name = input("What is your name? ")
    alchemist = Alchemist(name)

    # start at boss 1
    boss_enum = HARPY_BOSS
    is_victory = False

    # create map object
    maps = Maps(ROWS, COLUMNS)
    maps.new_map()

    while boss_enum <= DRAGON_BOSS:
        # check if alchemist walked onto a pick-up
        potential_pick_up = maps.set_alchemist_position(alchemist)
        is_boss = check_pick_up(potential_pick_up)

        # if pick-up was a boss
        if is_boss:
            current_boss = make_boss(boss_enum)
            current_boss.appear()
            is_victory = Combat(alchemist, current_boss).fight()

        # if boss was killed
        if is_victory:
            boss_enum += 1

        # update map and prompt user input for move/inventory
        maps.print_map()
        choice = user_choice()

        # move alchemist and change map if zoned
        is_new_map = alchemist.user_choice(choice, ROWS, COLUMNS)
        if is_new_map:
            maps.new_map()
