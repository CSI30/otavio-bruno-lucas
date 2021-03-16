class Coordinate():
    next_id = 0

    def __init__(self, latitude, longitude):
        self.id = Coordinate.next_id
        Coordinate.next_id += 1

        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.latitude == other.latitude and self.longitude == other.longitude

    def __str__(self):
        return "(%f, %f)" % (self.latitude, self.longitude)
