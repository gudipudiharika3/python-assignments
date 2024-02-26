"""
HW      # 3
Problem # 1 Composition
Author  # Gudipudi HarikaPadmini
"""


class Point:
    def __init__(self, X=0, Y=0):
        self._X = X
        self._Y = Y

    # getter for Xpoint
    def getX(self):
        return self._X

    # setter for Xpoint
    def setX(self, val):
        self._X = val

    # getter for Y point
    def getY(self):
        return self._Y

    # setter for Y point
    def setY(self, val):
        self._Y = val

    # Assigning new point
    def movePoint(self, x, y):
        self._X = x
        self._Y = y

    def __str__(self):
        return f"({self._X},{self._Y})"


class Circle:
    def __init__(self, radius, center_point=Point()):
        self._radius = radius
        self._point = center_point

    # moving the point
    def movePoint(self, x, y):
        self._point.movePoint(x, y)

    def __str__(self):
        return f"Circle with radius {self._radius} centered at {self._point}"


if __name__ == '__main__':
    p1 = Point(0, 0)
    c1 = Circle(5, p1)
    print('Before the move')
    print(c1)
    c1.movePoint(3, 2)
    print('After the move')
    print(c1)
