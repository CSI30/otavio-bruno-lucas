from path import Path


class Road_network:
    next_id = 0

    def __init__(self, health_units):
        self.id = Road_network.next_id
        Road_network.next_id += 1

        self.health_units = health_units
        self.paths = []  # Calcular todos os paths

        self.calculate_paths()

    def calculate_paths(self):
        for i in range(0, len(self.health_units)):
            for j in range(i + 1, len(self.health_units)):
                self.paths.append(
                    Path(self.health_units[i], self.health_units[j]))

    def __str__(self):
        out = ""
        for i in self.health_units:
            out += i.__str__() + "\n"

        out += "\n"
        for i in self.paths:
            out += i.__str__() + "\n"
        return out
