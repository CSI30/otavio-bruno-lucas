from math import cos, asin, sqrt
from random import uniform
import sys


class Coordinate():
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.latitude == other.latitude and self.longitude == other.longitude

    def __str__(self):
        return "(%f, %f)" % (self.latitude, self.longitude)

    def haversineDistanceTo(self, other):
        p = 0.017453292519943295
        a = 0.5 - cos((other.latitude - self.latitude) * p)/2 + cos(self.latitude * p) * \
            cos(other.latitude * p) * \
            (1 - cos((other.longitude - self.longitude) * p)) / 2
        return 12742 * asin(sqrt(a))


class HealthUnit:  # Node
    next_id = 0

    def __init__(self, name, coordinate):
        self.id = HealthUnit.next_id
        HealthUnit.next_id += 1

        self.name = name
        self.coordinate = coordinate

        self.was_visited = False

    def __str__(self):
        return "Health Unit: (%s) %s | Coordinate: %s | Was Visited: %s " % (self.id, self.name, self.coordinate.__str__(), self.was_visited)

    def haversineDistanceTo(self, other):
        return self.coordinate.haversineDistanceTo(other.coordinate)


class Route:  # Edge
    next_id = 0

    def __init__(self, u, v):
        self.id = Route.next_id
        Route.next_id += 1

        self.origin_id = u.id
        self.destination_id = v.id
        self.distance = u.haversineDistanceTo(v)
        self.weight = Route.calculateWeight()

    @staticmethod
    def calculateWeight():
        return uniform(0.0, 1.0)

    def __str__(self):
        return "Route: (%s) <-> (%s) | Distance: %s km | Weight: %s" % (self.origin_id, self.destination_id, self.distance, self.weight)


class GPS:
    next_id = 0

    def __init__(self, health_units):
        self.id = HealthUnit.next_id
        HealthUnit.next_id += 1

        self.health_units = health_units
        self.routes = []

    def addRoute(self, u, v):
        # TODO: Test if route already exists
        route = Route(u, v)
        self.routes.append(route)

    def calculateAllRoutes(self):
        for i in range(0, len(self.health_units)):
            for j in range(i + 1, len(self.health_units)):
                self.addRoute(self.health_units[i], self.health_units[j])

    def __str__(self):
        out = ""
        for i in self.health_units:
            out += i.__str__() + "\n"

        out += "\n"
        for i in self.routes:
            out += i.__str__() + "\n"
        return out


class State:
    def __init__(self, gps):
        self.gps = gps

    def __str__(self):
        return str(self.gps)


health_units = []

f = open("health-units.txt", "r")
lines = f.readlines()

for line in lines:
    line_tokens = line.split(";")

    name = line_tokens[0]
    latitude = float(line_tokens[1])
    longitude = float(line_tokens[2].replace("\n", ""))
    health_units.append(HealthUnit(name, Coordinate(latitude, longitude)))

f.close()

gps = GPS(health_units)
gps.calculateAllRoutes()

initial_state = State(gps)
print(initial_state)
