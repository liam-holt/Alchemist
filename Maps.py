#import Ingredient
#import Enemy
from Alchemist import Alchemist
import random

FLOWER = '@'
BOTTLE = '%'
CATALYST = '!'
ANIMAL = '}'
BOSS = '?'


class Maps:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.current_map = \
            [[' ' for row in range(columns)] for column in range(rows)]

    def print_map(self):
        """
        Displays the game board
        :return: none
        """
        for row in range(len(self.current_map)):
            for column in range(len(self.current_map[0])):
                print(self.current_map[row][column], end = "")
            print()

    def set_alchemist_position(self, alchemist):
        """
        updates the icon placement for the player
        :param alchemist: the player character class
        :return: a character representing any potential items picked up
        """
        for row in range(self.rows):
            for column in range(self.columns):
                if self.current_map[row][column] == alchemist.icon:
                    self.current_map[row][column] = ' '

        potential_pick_up = self.current_map[alchemist.row][alchemist.column]
        self.current_map[alchemist.row][alchemist.column] = alchemist.icon

        return potential_pick_up

    def new_map(self, is_new):
        """
        randomizes the items scattered around the map
        :return:
        """

        if not is_new:
            print("The winds are heavy and the sand thick;"
                  " you aren't sure which way you came from...")

        self.current_map = \
            [[' ' for row in range(self.columns)] \
             for column in range(self.rows)]

        is_boss = False

        for row in range(self.rows):
            for column in range(self.columns):
                percent_chance = random.randint(0, 100)



                if 0 <= percent_chance < 90:
                    pass
                elif 91 <= percent_chance < 93:
                    self.current_map[row][column] = FLOWER
                elif 94 <= percent_chance < 96:
                    self.current_map[row][column] = ANIMAL
                elif 97 <= percent_chance < 98:
                    self.current_map[row][column] = CATALYST
                elif 99 <= percent_chance < 99:
                    self.current_map[row][column] = BOTTLE
                elif percent_chance == 100:
                    if not is_boss:
                        self.current_map[row][column] = BOSS
                        is_boss = True
                    else:
                        pass
