import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def area(self):
        return math.pi * (self.diameter / 2) ** 2


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2



aplis = Circle(5)
kvadrats = Square(5)




class Square: 
    def __init__(self, side):
        self.side = side
        self