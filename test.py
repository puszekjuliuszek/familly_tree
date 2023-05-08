from enum import Enum

from enum import Enum


class Color(Enum):
    RED = (1, "czerwony")
    GREEN = (2, "zielony")
    BLUE = (3, "niebieski")

    def next_color(self):
        if self == Color.RED:
            return Color.GREEN
        elif self == Color.GREEN:
            return Color.BLUE
        elif self == Color.BLUE:
            return Color.RED
        else:
            raise ValueError("Unknown color")

    def __str__(self):
        return self.name

    @property
    def description(self):
        return self.value[1]


print(Color.RED.description)