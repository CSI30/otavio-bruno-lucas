import genetic_algorithm as GA
from place import Place

# import matplotlib.pyplot as plt
# import numpy as np

# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

population_size = 20
number_of_parents = 5
probability_of_mutation = 0.01
verbose = False

origin, places = Place.from_file("places.txt")

for number_of_rounds in range(1, 1000, 1):
    population = GA.population(places, population_size, verbose)

    for i in range(number_of_rounds):
        population = GA.selection_and_crossover(
            population,
            number_of_parents,
            lambda x: GA.hs_fitness(x, origin),
            verbose
        )
        population = GA.mutation(
            population,
            number_of_parents,
            probability_of_mutation,
            verbose
        )

    route = GA.best_chromossome(
        population,
        lambda x: GA.hs_fitness(x, origin),
        verbose
    )

    x.append(number_of_rounds)
    y.append(GA.hs_fitness(route, None))


fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='number of rounds', ylabel='distance')
ax.grid()

# fig.savefig("test.png")
plt.show()


# plt.scatter(x, y)
# plt.show()
