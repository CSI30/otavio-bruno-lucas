from random import shuffle, randint, random

from coordinate import haversine
from place import Place
from google_maps import Google_maps


def print_population(population):
    for i in range(len(population)):
        print(list(map(lambda x: x.id, population[i])))


def print_places(places):
    for i in range(len(places)):
        print(places[i])


# bp - best population
# br - best route
def print_result(population, traffic_multiplier):
    print('\nBEST ROUTE:')

    bp = [(fitness(i, traffic_multiplier), i) for i in population]
    bp = [i[1] for i in sorted(bp)]
    br = bp[0]

    print(
        'c:',
        list(map(lambda x: x.id, br)),
        'fitness:',
        fitness(br, traffic_multiplier),
        '\n'
    )
    print_places(br)

    for i in range(len(br)):
        Google_maps.addWaipoint(
            br[i].coordinate.latitude, br[i].coordinate.longitude
        )
    print(Google_maps.buildUrl())


def population(places, size):
    population = [list(places) for i in range(size)]
    for i in population:
        shuffle(i)
    return population


def fitness(places, traffic_multiplier):
    fitness = 0
    for i in range(len(places)):
        if i == len(places)-1:
            break
        fitness += haversine(places[i].coordinate,
                             places[i+1].coordinate) * traffic_multiplier
    return fitness


# sp - scored population
# sc - selected chromosome
# nc - new componenets
def selection_and_crossover(population, parents, traffic_multiplier):
    sp = [(fitness(i, traffic_multiplier), i) for i in population]
    sp = [i[1] for i in sorted(sp, reverse=True)]
    sc = sp[(len(sp) - parents):]

    print('\nSELECTED CHROMOSOMES:')
    print_population(sc)

    print('\nCROSSOVER:')

    for i in range(len(sp) - parents):
        point = randint(1, len(sp[i]) - 1)
        shuffle(sc)
        nc = list(sc[0])
        for j in range(len(sp[i][:point])):
            nc.remove(sp[i][:point][j])
        sp[i][point:] = nc

        print(
            'c:',
            list(map(lambda x: x.id, sp[i])),
            '& sc:',
            list(map(lambda x: x.id, sc[0])),
            'at:',
            point,
            '->',
            list(map(lambda x: x.id, sp[i][:point])),
            ' + ',
            list(map(lambda x: x.id, nc))
        )

    return sp


# mp - mutated population
def mutation(population, parents, probability):
    mp = list(population)

    print('\nMUTATION:')

    for i in range(len(mp) - parents):
        if (random() <= probability):
            j = randint(0, len(mp[i]) - 2)

            print(
                'c:',
                list(map(lambda x: x.id, mp[i])),
                'c[' + str(j) + ']=' + str(mp[i][j].id),
                '<-> c[' + str(j+1) + ']=' + str(mp[i][j+1].id),
                end=' '
            )

            mp[i][j], mp[i][j+1] = mp[i][j+1], mp[i][j]

            print(
                '->',
                list(map(lambda x: x.id, mp[i])),
            )
    return mp


# parameters
population_size = 100
number_of_parents = 5
probability_of_mutation = 0.1
traffic_multiplier = 1
number_of_rouds = 1000

origin, places = Place.from_file("places.txt")
print('\nORIGIN:')
print(origin)
print('\nHEALTH UNITS:')
print_places(places)


population = population(places, population_size)
print('\nINITIAL POPULATION:')
print_population(population)

for i in range(number_of_rouds):
    population = selection_and_crossover(
        population, number_of_parents, traffic_multiplier)
    population = mutation(population, number_of_parents,
                          probability_of_mutation)

print('\nRESULTANT POPULATION:')
print_population(population)

print_result(population, traffic_multiplier)
