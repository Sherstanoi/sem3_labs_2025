from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle

rect = Rectangle(11,13, "blue")
sq = Square(24, "red")
circ = Circle(24, "green")

print(rect.__repr__())
print(sq.__repr__())
print(circ.__repr__())

hex_str =b"hii"
hexxed = hex_str.hex()
print(hexxed)