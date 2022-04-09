class Point:
    def __init__(self, x, y, z, k):
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
        self.k = k

    def get_distance(self, origin=None):
        if origin is not None:
            distance_square = (origin.x - self.x) * (origin.x - self.x) + \
                              (origin.y - self.y) * (origin.y - self.y) + \
                              (origin.z - self.z) * (origin.z - self.z)
        else:
            distance_square = self.x * self.x + \
                              self.y * self.y + \
                              self.z * self.z

        distance = pow(distance_square, 0.5)
        return distance

    def __str__(self):
        output = 'Point: (' + str(self.x) + ', ' + \
                 str(self.y) + ', ' + str(self.z) + ')'
        return output
