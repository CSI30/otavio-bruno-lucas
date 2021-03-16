from random import shuffle
import sys

from coordinate import Coordinate
from health_unit import Health_unit
from road_network import Road_network

from google_maps import Google_maps

health_units = []

f = open("health_units.txt", "r")
lines = f.readlines()

for line in lines:
    line_tokens = line.split(";")
    name = line_tokens[0]
    latitude = float(line_tokens[1])
    longitude = float(line_tokens[2].replace("\n", ""))
    health_units.append(Health_unit(name, Coordinate(latitude, longitude)))

f.close()

road_network = Road_network(health_units)
print(road_network)


# Random Route Exemple
random_order = road_network.health_units
shuffle(random_order)

for i in range(0, len(random_order)):
    Google_maps.addWaipoint(
        random_order[i].coordinate.latitude, random_order[i].coordinate.longitude
    )
print(Google_maps.buildUrl())
