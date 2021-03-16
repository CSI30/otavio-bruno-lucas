from math import cos, asin, sqrt
from random import choice
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

        self.distance = u.haversineDistanceTo(v)
        self.u = u
        self.v = v

    def __str__(self):
        return "Route: (%s) -> (%s) | Distance: %s km" % (self.u.id, self.v.id, self.distance)


class GPS:
    next_id = 0

    def __init__(self, health_units):
        self.id = HealthUnit.next_id
        HealthUnit.next_id += 1

        self.health_units = health_units
        self.routes = []

    def __str__(self):
        out = ""
        for i in self.health_units:
            out += i.__str__() + "\n"

        out += "\n"
        for i in self.routes:
            out += i.__str__() + "\n"
        return out

    def addRoute(self, u, v):
        # TODO: Test if route already exists
        route = Route(u, v)
        self.routes.append(route)


class State:
    def __init__(self, gps):
        self.gps = gps

    def __str__(self):
        return str(self.gps)


us_01 = HealthUnit("São João Del Rey", Coordinate(-25.5376104, -49.2732949))
us_02 = HealthUnit("Waldemar Monastier", Coordinate(-25.4974949, -49.2274042))
us_03 = HealthUnit("Bacacheri", Coordinate(-25.4007554, -49.2395827))
us_04 = HealthUnit("Cajuru", Coordinate(-25.4521997, -49.2176676))
us_05 = HealthUnit("São Miguel", Coordinate(-25.480256, -49.3367166))


gps_01 = GPS([
    us_01,
    us_02,
    us_03,
    us_04,
    us_05
])

gps_01.addRoute(us_01, us_02)
gps_01.addRoute(us_01, us_03)
gps_01.addRoute(us_01, us_04)
gps_01.addRoute(us_01, us_05)

gps_01.addRoute(us_02, us_03)
gps_01.addRoute(us_02, us_04)
gps_01.addRoute(us_02, us_05)

gps_01.addRoute(us_03, us_04)
gps_01.addRoute(us_03, us_05)

gps_01.addRoute(us_04, us_05)


initial_state = State(gps_01)

print(initial_state)
