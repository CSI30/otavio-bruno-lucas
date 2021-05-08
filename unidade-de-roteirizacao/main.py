from random import shuffle, randint, sample, choice, random
import sys
from math import cos, asin, sqrt
from functools import reduce
from copy import copy


class Coordinate:
    next_id = 0

    def __init__(self, latitude, longitude):
        self.id = Coordinate.next_id
        Coordinate.next_id += 1

        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def haversine_distance_between(c1, c2):
        p = 0.017453292519943295
        a = 0.5 - cos((c2.latitude - c1.latitude) * p)/2 + cos(c1.latitude * p) * \
            cos(c2.latitude * p) * \
            (1 - cos((c2.longitude - c1.longitude) * p)) / 2
        return 12742 * asin(sqrt(a))

    def __eq__(self, other):
        return self.latitude == other.latitude and self.longitude == other.longitude

    def __str__(self):
        return "(%f, %f)" % (self.latitude, self.longitude)


class Health_unit:
    next_id = 0

    def __init__(self, name, coordinate):
        self.id = Health_unit.next_id
        Health_unit.next_id += 1

        self.name = name
        self.coordinate = coordinate

    def __eq__(self, other):
        return self.coordinate == other.coordinate and self.name == other.name

    def __str__(self):
        return "Health Unit: %s | %s | %s" % (self.id, self.coordinate.__str__(), self.name)


class Chromosome:
    next_id = 0

    def __init__(self, health_units):
        self.id = Chromosome.next_id
        Chromosome.next_id += 1

        self.components = list(health_units)

    def shuffled(self):
        shuffle(self.components)
        return self

    @staticmethod
    def generate_population(health_units, size):
        return [Chromosome(health_units).shuffled() for i in range(size)]

    def __eq__(self, other):
        for i in range(len(self.components)):
            if self.components[i] != other.components[i]:
                return False
        return True

    def __str__(self):
        return "Chromosome: %s | %s" % (self.id, list(map(lambda x: x.id, self.components)))


class Genetic_algorithm:

    @ staticmethod
    def fitness(origin, chromosome):
        fitness = Coordinate.haversine_distance_between(
            origin.coordinate, chromosome.components[0].coordinate)
        for i in range(len(chromosome.components)):
            if i == len(chromosome.components)-1:
                break
            fitness += Coordinate.haversine_distance_between(
                chromosome.components[i].coordinate, chromosome.components[i+1].coordinate)
        return fitness

    @ staticmethod
    def selection_and_crossover(population, parents):
        print('\nSelection \n')
        scored_population = [(Genetic_algorithm.fitness(origin, i), i)
                             for i in population]
        scored_population = [i[1]
                             for i in sorted(scored_population, reverse=True)]

        selected_chromosomes = scored_population[(
            len(scored_population) - parents):]

        for i in range(len(selected_chromosomes)):
            print(selected_chromosomes[i])

        print('\nCrossover \n')

        for i in range(len(scored_population) - parents):
            point = randint(1, len(scored_population[i].components) - 1)
            shuffle(selected_chromosomes)
            new_components = list(selected_chromosomes[0].components)

            for j in range(len(scored_population[i].components[:point])):
                new_components.remove(
                    scored_population[i].components[:point][j])

            scored_population[i].components[point:] = new_components

            print('point:', point,
                  '|', list(
                      map(lambda x: x.id, scored_population[i].components[:point])),
                  '-\\-', list(map(lambda x: x.id, new_components)))

        return scored_population

    @ staticmethod
    def mutation(population, parents, probability):
        print('\nMutation \n')
        mutated_population = list(population)

        for i in range(len(mutated_population) - parents):
            if (random() <= probability):
                index = randint(0, len(mutated_population[i].components) - 2)
                mutated_population[i].components[index], mutated_population[i].components[index +
                                                                                          1] = mutated_population[i].components[index+1], mutated_population[i].components[index]

        return mutated_population


# implementation
origin = Health_unit("Centro de Distribuição",
                     Coordinate(-25.4367623, -49.259514))
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

population = Chromosome.generate_population(health_units, 100)

for i in range(1000):
    population = Genetic_algorithm.selection_and_crossover(population, 10)
    population = Genetic_algorithm.mutation(population, 10, 0.01)

for i in range(len(population)):
    print(population[i], Genetic_algorithm.fitness(origin, population[i]))

best_response = [(Genetic_algorithm.fitness(origin, i), i) for i in population]
best_response = [i[1] for i in sorted(best_response)]

print('Melhor Caminho: ', best_response[0])
