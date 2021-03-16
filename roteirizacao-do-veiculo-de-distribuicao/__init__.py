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
    def __init__(self, name, coordinate, was_visited):
        self.name = name
        self.coordinate = coordinate
        self.was_visited = was_visited

    def __str__(self):
        return "(" + self.name + " - " + self.coordinate.__str__() + ", was_visited: " + ("True" if self.was_visited else "False") + ")"

    def linearDistanceTo(self, other):
        return self.coordinate.linearDistanceTo(other.coordinate)


class State:
    def __init__(self, healthUnits):
        self.healthUnits = healthUnits

    def __str__(self):
        out = ""
        for i in self.healthUnits:
            out += i.__str__() + "\n"
        return out


us_01 = HealthUnit("US1", Coordinate(0, 0), False)
us_02 = HealthUnit("US2", Coordinate(2, 0), False)
us_03 = HealthUnit("US3", Coordinate(1, 1), False)
us_04 = HealthUnit("US4", Coordinate(2, 0), False)
us_05 = HealthUnit("US5", Coordinate(2, 2), False)


initial_state = State([
    us_01,
    us_02,
    us_03,
    us_04,
    us_05
])

# print(initial_state)

print(us_01.linearDistanceTo(us_02))
