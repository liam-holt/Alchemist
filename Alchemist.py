"""
The main character
Handles position on the gameboard and other user input
WIP
"""

from Inventory import Inventory


class Alchemist:
    def __init__(self, name):
        self.name = name
        self.icon = name[0]
        self.row = 0
        self.column = 0
        self.inventory = Inventory()

    def user_choice(self, choice, rows, columns):
        """
        Moves the player according to user input
        :param choice: the direction moved (WASD) or inventory (E)
        :param rows: number of rows on the map
        :param columns: number of columns on the map
        :return: a boolean for if the player walked off the map (zoning)
        """
        is_new_map = False

        if choice == 'E':
            self.inventory.print_inventory()
        elif choice == 'W' and self.row > 0:
            self.row -= 1
        elif choice == 'W':
            self.row = rows - 1
            is_new_map = True
        elif choice == 'A' and self.column > 0:
            self.column -= 1
        elif choice == 'A':
            self.column = columns - 1
            is_new_map = True
        elif choice == 'S' and self.row < rows - 1:
            self.row += 1
        elif choice == 'S':
            self.row = 0
            is_new_map = True
        elif choice == 'D' and self.column < columns - 1:
            self.column += 1
        elif choice == 'D':
            self.column = 0
            is_new_map = True

        return is_new_map
