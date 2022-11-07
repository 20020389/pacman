
class Position:
    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y
        pass

    def get(self):
        return self.x, self.y
