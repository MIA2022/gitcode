class Point:
    def __init__(self, x, y, z):
        if not isinstance(x, int):
            raise TypeError
        if not isinstance(y, int):
            raise TypeError
        if not isinstance(z, int):
            raise TypeError
        if x == '' or y == '' or z == '':
            raise ValueError

        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, origin=None, point2=None):
        if point2 is not None:
            distance_square = (point2.x - self.x) * (point2.x - self.x) + \
                              (point2.y - self.y) * (point2.y - self.y) + \
                              (point2.z - self.z) * (point2.z - self.z)
        else:
            distance_square = (origin.x - self.x) * (origin.x - self.x) + \
                              (origin.y - self.y) * (origin.y - self.y) + \
                              (origin.z - self.z) * (origin.z - self.z)

        distance = pow(distance_square, 0.5)
        return distance

    def __str__(self):
        output = 'Point: (' + str(self.x) + ', ' + \
                 str(self.y) + ', ' + str(self.z) + ')'
        return output
