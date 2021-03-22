from random import uniform
from math import cos, asin, sqrt


class Path:
    next_id = 0

    def __init__(self, health_unit_1, health_unit_2,):
        self.id = Path.next_id
        Path.next_id += 1

        self.health_unit_1 = health_unit_1
        self.health_unit_2 = health_unit_2
        self.haversine_distance = Path.haversine_distance_between(
            health_unit_1.coordinate, health_unit_2.coordinate)
        self.accident_probability = uniform(0.0, 1.0)
        self.heavy_traffic_probability = uniform(0.0, 1.0)

    @staticmethod
    def haversine_distance_between(coordinate_1, coordinate_2):
        p = 0.017453292519943295
        a = 0.5 - cos((coordinate_2.latitude - coordinate_1.latitude) * p)/2 + cos(coordinate_1.latitude * p) * \
            cos(coordinate_2.latitude * p) * \
            (1 - cos((coordinate_2.longitude - coordinate_1.longitude) * p)) / 2
        return 12742 * asin(sqrt(a))

    def __str__(self):
        return "Path: (%s)-(%s) | haversine_distance: %s km | accident_probability: %s | heavy_traffic_probability: %s" % (self.health_unit_1.id, self.health_unit_2.id, self.haversine_distance, self.accident_probability, self.heavy_traffic_probability)
