import math


class Circle:
    def __init__(self, x, y, r):
        if not isinstance(x, float):
            raise TypeError
        if not isinstance(y, float):
            raise TypeError
        if not isinstance(r, float):
            raise TypeError
        if r <= 0:
            raise ValueError
        self.x = x
        self.y = y
        self.radius = r

    def get_area(self):
        area = 3.14 * self.radius * self.radius
        return area

    def get_distance(self, x, y):
        if not isinstance(x, float):
            raise TypeError
        if not isinstance(y, float):
            raise TypeError
        distance_square = (x - self.x) ** 2 + \
                          (y - self.y) ** 2
        distance = math.sqrt(distance_square)
        return distance

    def __str__(self):
        output = 'Circle: center at (' + str(self.x) + ', ' + \
                 str(self.y) + ') with radius ' + str(self.radius)
        return output
