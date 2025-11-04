from .rectangle import Rectangle

from .figure import GeomFigure
from .ShapeColour import ShapeColour

class Square(Rectangle):
    def __init__(self, side, colour = ShapeColour):
        self.side = side
        self.colour = ShapeColour
        self.colour = colour
        self.Name = "square"

    def figureName(self):
        return self.Name

    def area(self):
        return self.side**2

    def __repr__(self):
        return f"{self.Name}, {self.side}, {self.colour}, {self.area()}"