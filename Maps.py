"""
The game board
Walking "off" the grid will randomize the loot on the map ("zoning")
WIP
"""

#import Ingredient
#import Enemy
from Alchemist import Alchemist
import random

FLOWER = '@'
CONTAINER_OR_CATALYST = '?'
ANIMAL_PARTS = '%'
BOSS = '!'


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
            print('|')

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
                # 1% chance was too high for the boss
                # with 50 tiles its about a 40% spawnrate
                # 0.5% with 50 tiles is about 22%
                chance = random.randint(0, 200)

                if 0 <= chance < 185:
                    pass
                elif 186 <= chance < 191:
                    self.current_map[row][column] = FLOWER
                elif 192 <= chance < 196:
                    self.current_map[row][column] = ANIMAL_PARTS
                elif 197 <= chance < 199:
                    self.current_map[row][column] = CONTAINER_OR_CATALYST
                elif chance == 199:
                    if not is_boss:
                        self.current_map[row][column] = BOSS
                        is_boss = True
                    else:
                        pass
