class Combat:
    """
    Combat handler
    Alchemist (player) vs bosses
    """
    def __init__(self, alchemist, boss):
        self.alchemist = alchemist
        self.boss = boss

    def fight(self):
        """
        Begins main fight
        :return: bool: Boss killed?
        """
        is_victorious = False
        self.boss.begin_combat()

        print("WIP")

        if is_victorious:
            return True
        return False
