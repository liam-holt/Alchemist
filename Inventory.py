"""
The main character's inventory, to include mixing options
WIP
"""

from Ingredient import *


class Inventory:
    """
    The Alchemist's inventory
    """
    def __init__(self):
        self.inventory = []

    def print_inventory(self):
        """
        Displays Inventory and gives option of Mix()
        :return: None
        """
        for item in self.inventory:
            print(f"{item.quantity} {item.name}")
            # start mixing
            choice = input("Would you like to mix? ")
            choice = choice.upper()
            valid_choices = ['y', 'yes', 'n', 'no']
            while choice not in valid_choices:
                choice = input("Would you like to mix? ")
                choice = choice.upper()
            if choice == 'y' or choice == 'yes':
                self.mix()
            else:
                pass

    def mix(self):
        """
        WIP
        :return:
        """
        # for mixing ingredients
        pass

    def add_ingredient(self, ingredient_type):
        """
        Adds picked up item
        :param ingredient_type: type of item picked up
        :return: None
        """
        ingredient = Ingredient(ingredient_type)

        in_inventory = False

        for item in self.inventory:
            if item.name == ingredient.name:
                in_inventory = True

                item.quantity += 1
        if not in_inventory:
            self.inventory.append(ingredient)
