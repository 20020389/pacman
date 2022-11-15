
import src.variables as variables


class Position:
    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y
        pass

    def get(self):
        return self.x, self.y

class Animate:
    __time: int = 0
    __status: int = 0
    __infinity: bool = True
    __limit: int = 2

    def __init__(self) -> None:
        self.__speed = variables.ANIMATE_SPEED
        pass

    def run(self):
        self.__time += 1

        if self.__time % self.__speed == 0:
            if self.__status < self.__limit:
                self.__status += 1

        if self.__infinity and self.__status == self.__limit:
            self.__status = 0

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value: int):
        self.__limit = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: int):
        if value >= 0 and value <= 1:
            self.__status = value
    
    def set_infinity(self, value: bool):
        self.__infinity = value

    def isFinish(self):
        return self.__status == self.__limit

    def set_speed(self, value: bool):
        self.__speed = value
