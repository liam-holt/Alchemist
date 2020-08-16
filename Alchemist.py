#import Inventory


class Alchemist:
    def __init__(self, name):
        self.name = name
        self.icon = name[0]
        self.row = 0
        self.column = 0

    def move(self, move, rows, columns):
        """
        Moves the player according to user input
        :param move: the direction moved (WASD)
        :param rows: number of rows on the map
        :param columns: number of columns on the map
        :return: a boolean for if the player walked off the map (zoning)
        """
        is_new_map = False

        if move == 'W' and self.row > 0:
            self.row -= 1
        elif move == 'W':
            self.row = rows - 1
            is_new_map = True
        elif move == 'A' and self.column > 0:
            self.column -= 1
        elif move == 'A':
            self.column = columns - 1
            is_new_map = True
        elif move == 'S' and self.row < rows - 1:
            self.row += 1
        elif move == 'S':
            self.row = 0
            is_new_map = True
        elif move == 'D' and self.column < columns - 1:
            self.column += 1
        elif move == 'D':
            self.column = 0
            is_new_map = True

        return is_new_map

