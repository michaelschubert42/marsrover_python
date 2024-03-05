class Position:
    x = 0
    y = 0

    def up(self):
        return Position(self.x, self.y - 1)

    def down(self):
        return Position(self.x, self.y + 1)

    def left(self):
        return Position(self.x - 1, self.y)

    def right(self):
        return Position(self.x + 1, self.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f'x:{self.x}, y:{self.y}'

    def __hash__(self):
        return self.x + self.y