# Genetic Algorithm - KNAPSACK_01
# genetic.py
# Created by Mauro José Pappaterra on 25 January 2021.
import create_dataset as ds
import random

def createInitialPool (object_list, size, capacity, pool_size, verbose):
    random_solutions = [[random.randint(0,1) for x in range(size)] for y in range(pool_size)]
    initialPool = []

    for genome in random_solutions:
        initialPool.append((genome, fitness(genome, object_list, capacity)))

    if (verbose):
        printPool("\nGENERATION 0 \nInitial solution pool:", initialPool)

    return initialPool

def fitness (genome, object_list, capacity):
    total_weight = sum([object_list[genome.index(x)].weight for x in genome if (x == 1)])

    if (total_weight > capacity):
        return 0

    total_profit = sum([object_list[genome.index(x)].profit for x in genome if (x == 1)])
    return total_profit

def naturalSelection (genome_pool, verbose):
    elitePool = [x for x in genome_pool if (x[1] > 0)]
    elitePool.sort(key=lambda x:x[1], reverse=True)

    if(verbose):
        printPool("\nAfter natural selection:", elitePool)

    return elitePool

def printPool (message, genomePool):
    print(message)
    for genome in genomePool:
        print(str(genome[0]) + "  >>  " + str(genome[1]))

def newGeneration (object_list, capacity, pool_size, elite_size, elite_pool, generation, verbose):
    # Keep best n solutions from previous generation elite pool
    new_generation = elite_pool[:elite_size]

    if (verbose):
        printPool("\nGENERATION " + str(generation) + "\nKeeping best " + str(elite_size) + " genome solutions from generation " + str(generation - 1), new_generation)

    # Generate pairs for single point crossover function
    pairs = generatePairs((pool_size - elite_size) / 2, len(elite_pool))

    for pair in pairs:
        new_generation = new_generation + crossover(elite_pool[pair[0]][0], elite_pool[pair[1]][0], object_list, capacity)

    if (verbose):
        printPool("\nSolution pool:", new_generation)

    return new_generation

def generatePairs (pool_size, elite_pool_size):
    pairs = []
    while (len(pairs) < pool_size):
        a = random.randint(0, elite_pool_size - 1)
        b = random.randint(0, elite_pool_size - 1)

        if (a != b):
            pairs.append((a, b))

    return pairs

def crossover (renome_a, genome_b, object_list, capacity):
    random_partition = random.randint(1, SIZE - 1)
    # print(random_partition)
    child_genome_a = renome_a[:random_partition] + genome_b[random_partition:]
    # print(child_genome_a)
    child_genome_b = genome_b[:random_partition] + renome_a[random_partition:]
    # print(child_genome_b)
    return [(child_genome_a,fitness(child_genome_a, object_list, capacity)), (child_genome_b,fitness(child_genome_b, object_list, capacity))]


def geneticAlgorithm (object_list, size, capacity, solution, pool_size, elite_size, verbose):
    # Create Initial Solution Pool
    generation = 0
    initialPool = createInitialPool(object_list, size, capacity, pool_size, verbose)

    # Elitism: delete unfit solutions keep best solutions
    elitePool = naturalSelection (initialPool, verbose)

    # Create new generation
    generation += 1
    newPool = newGeneration (object_list, capacity, pool_size, elite_size, elitePool, generation, verbose)
    elitePool = naturalSelection(newPool, verbose)

# Global variables
POOL_SIZE = 10
ELITE_SIZE = 2 # no. of solutions to keep from each generation after natural selection
VERBOSE = True

# Database variables
OBJECT_LIST, SIZE, CAPACITY, SOLUTION = ds.getDataset("KNAPSACK_01/", "1", VERBOSE)

geneticAlgorithm(OBJECT_LIST, SIZE, CAPACITY, SOLUTION, POOL_SIZE, ELITE_SIZE, VERBOSE)

# TESTING METHODS
#createInitialPool(10)
#fitness([1, 1, 1, 1, 0, 1, 0, 0, 0, 0])
#crossover([1, 1, 0, 1, 0, 0, 0, 0, 0, 0],[1, 0, 1, 0, 0, 1, 0, 0, 1, 1])