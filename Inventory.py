"""
The main character's inventory, to include mixing options
WIP
"""

from Ingredient import *


class Inventory:
    def __init__(self):
        self.inventory = []

    def print_inventory(self):
        for item in self.inventory:
            print(f"{item.quantity} {item.name}")
            # pause for user
            input()

    def add_ingredient(self, type):
        ingredient = Ingredient(type)

        in_inventory = False

        for item in self.inventory:
            if item.name == ingredient.name:
                in_inventory = True

                item.quantity += 1
        if not in_inventory:
            self.inventory.append(ingredient)
