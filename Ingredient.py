"""
The items you pick up on the Map
Mixed together in Inventory to make potions to fight Enemies
"""
import random

FLOWER = '@'
CONTAINER_OR_CATALYST = '?'
ANIMAL_PARTS = '%'
FLOWER_TYPE = 'flower'
ANIMAL_PARTS_TYPE = 'animal part'
CATALYST_TYPE = 'catalyst'
CONTAINER_TYPE = 'container'


class Ingredient:
    """
    Flowers(@), Animal Parts(%), Containers and Catalysts(?)
    Combined in Inventory to make potions for Combat against
    Enemies
    """

    def __init__(self, type):
        self._name = None
        try:
            if type == FLOWER:
                self._type = FLOWER_TYPE
            elif type == ANIMAL_PARTS:
                self._type = ANIMAL_PARTS_TYPE
            elif type == CONTAINER_OR_CATALYST:
                chance = random.randint(1, 100)
                if chance > 70:
                    self._type = CATALYST_TYPE
                else:
                    self._type = CONTAINER_TYPE
            else:
                raise Exception('Invalid Type')
        except Exception as instance:
            x = instance.args
            print(f"x = {x}")
            print(instance.args)
            print(instance)

        self._quantity = 1
        # placeholder names
        self._possible_flower = ["F", "f"]
        self._possible_animal_part = ["A", "a"]
        self._possible_catalyst = ["C", "c"]
        self._possible_container = ["B", "c"]

        try:
            if self._type == FLOWER_TYPE:
                self._possible_name = self._possible_flower
            elif self._type == ANIMAL_PARTS_TYPE:
                self._possible_name = self._possible_animal_part
            elif self._type == CATALYST_TYPE:
                self._possible_name = self._possible_catalyst
            elif self._type == CONTAINER_TYPE:
                self._possible_name = self._possible_container
            else:
                raise Exception('Invalid Type')
        except Exception as instance:
            x = instance.args
            print(f"x = {x}")
            print(instance.args)
            print(instance)

        # randint is [a,b] and not [a,b) turns out, so minus 1
        random_name = random.randint(0, len(self._possible_name) - 1)
        name = self._possible_name[random_name]

        # placeholder
        print(f"You found {name}!")
        # pause for user
        input()

        Ingredient.name.fset(self, name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
