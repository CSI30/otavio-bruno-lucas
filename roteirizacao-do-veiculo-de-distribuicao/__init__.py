from math import sqrt


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def linearDistanceTo(self, other):
        return sqrt(((self.x-other.x)**2) + ((self.y-other.y)**2))


class HealthUnit:
    def __init__(self, coordinate, wasVisited):
        self.coordinate = coordinate


class State:
    def __init__(self, healthUnits):
        self.healthUnits = healthUnits
