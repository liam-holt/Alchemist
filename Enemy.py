"""
Three enemy types, to be fought with brewed potions, etc
WIP
"""


class Enemy:
    def __init__(self, name):
        self.name = name


class Harpy(Enemy):
    def __init__(self):
        name = "Harpy"
        super().__init__(name)


class Wyvern(Enemy):
    def __init__(self):
        name = "Wyvern"
        super().__init__(name)


class Dragon(Enemy):
    def __init__(self):
        name = "Dragon"
        super().__init__(name)
