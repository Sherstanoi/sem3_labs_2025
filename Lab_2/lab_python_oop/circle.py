from .figure import GeomFigure
from .ShapeColour import ShapeColour
import math

class Circle(GeomFigure):
    def __init__(self, radius, colour = ShapeColour):
        self.radius = radius
        self.colour = ShapeColour
        self.colour = colour
        self.Name = "circle"

    def figureName(self):
        return self.Name

    def area(self):
        return math.pi*self.radius**2

    def __repr__(self):
        return f"{self.Name}, {self.radius}, {self.colour}, {self.area()}"