from .figure import GeomFigure
from .ShapeColour import ShapeColour

class Rectangle(GeomFigure):
    def __init__(self, width, height, colour=ShapeColour):
        self.width = width
        self.height = height
        self.colour = ShapeColour
        self.colour = colour
        self.Name = "rectangle"

    def figureName(self):
        return self.Name

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.Name}, {self.width}, {self.height}, {self.colour}, {self.area()}"