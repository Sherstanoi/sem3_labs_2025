class ShapeColour():
    def __init__(self):
        self.Colour = None;

    @property
    def Shape_Colour(self):
        return self.Colour

    @Shape_Colour.setter
    def Shape_Colour(self, value):
        self.Colour = value

