"""
Three enemy types, to be fought with brewed potions, etc
WIP
"""


class Enemy:
    """
    abstract class for bosses
    """
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Harpy(Enemy):
    """
    The first boss
    """
    def __init__(self, name):
        super().__init__(name)
        print("debug: spawned harpy")

    @staticmethod
    def begin_combat():
        """
        flavor text at combar start
        :return: None
        """
        print("The harpy slashes at you!\n")

    @staticmethod
    def appear():
        """
        Flavor text at spawn.
        :return: None
        """
        print("An ear piercing shriek deafens you!\n"
              "You stagger to your knees, holding your ears.\n")
        # pause for user
        input()


class Wyvern(Enemy):
    """
    The second boss
    """
    def __init__(self, name):
        super().__init__(name)
        print("debug: spawned wyvern")

    # flavor text at combat start
    @staticmethod
    def begin_combat():
        """
        Flavor text at comba start
        :return: None
        """
        print("The wyvern swoops down!\n")

    @staticmethod
    def appear():
        """
        Flavor text at spawn
        :return: None
        """
        print("A harsh beat of leathery wings.\n"
              "Sand flies all around you.\n")
        # pause for user
        input()


class Dragon(Enemy):
    """
    The third and final boss
    """
    def __init__(self, name):
        super().__init__(name)
        print("debug: spawned dragon")

    @staticmethod
    def begin_combat():
        """
        Flavor text at combat start
        :return: None
        """
        print("The mighty dragon breaths fire!\n")

    @staticmethod
    def appear():
        """
        Flavor text at spawn
        :return: None
        """
        print("As you cross the dune you freeze in terror.\n"
              "Too late. You can feel the impact of its roar.\n")
        # pause for user
        input()
